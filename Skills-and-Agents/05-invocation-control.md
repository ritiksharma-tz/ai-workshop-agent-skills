# Invocation Control — Who Triggers a Skill?

By default, **both the user and the AI model** can invoke any skill. Two frontmatter fields let you restrict this.

## The Invocation Matrix

```
                            USER CAN INVOKE?
                          YES               NO
                     ┌──────────────┐  ┌──────────────┐
            YES      │   DEFAULT    │  │  Background   │
                     │              │  │  Knowledge    │
   MODEL             │  Both can    │  │              │
   CAN               │  invoke      │  │  user-       │
   INVOKE?           │              │  │  invocable:  │
                     │  /review     │  │  false       │
                     │  /explain    │  │              │
                     │  /test-gen   │  │  legacy-     │
                     │              │  │  system-ctx  │
                     ├──────────────┤  ├──────────────┤
            NO       │  Manual      │  │  Disabled    │
                     │  Trigger     │  │  (not useful)│
                     │  Only        │  │              │
                     │              │  │              │
                     │  disable-    │  │              │
                     │  model-      │  │              │
                     │  invocation  │  │              │
                     │  : true      │  │              │
                     │              │  │              │
                     │  /deploy     │  │              │
                     │  /release    │  │              │
                     │  /db-migrate │  │              │
                     └──────────────┘  └──────────────┘
```

## When to Use Each Mode

| Mode | Frontmatter | Use For | Examples |
|------|-------------|---------|----------|
| **Default** | *(none)* | Safe, general-purpose skills | `/code-review`, `/explain-code`, `/test-gen` |
| **Manual only** | `disable-model-invocation: true` | Side effects, destructive ops, timing-sensitive | `/deploy`, `/release`, `/send-slack`, `/db-migrate` |
| **Background** | `user-invocable: false` | Context the model needs but users shouldn't invoke | `legacy-system-context`, `security-policies`, `internal-apis` |

## Example: Manual-Only Deploy Skill

You don't want the AI deciding to deploy because your code "looks ready":

```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
---

Deploy $ARGUMENTS to production:
1. Run the test suite
2. Build the application
3. Push to the deployment target
4. Verify the deployment succeeded
```

## Example: Background Knowledge Skill

Context the model should know, but not something a user would invoke as a command:

```yaml
---
name: legacy-payment-system
description: >
  Context about the legacy payment processing system (PaymentV1).
  Relevant when working on payment code, billing, or checkout flows.
user-invocable: false
---

# Legacy Payment System (PaymentV1)

## Important context
- PaymentV1 uses SOAP, not REST
- All amounts are in cents (integer), never decimals
- Transaction IDs follow format: TXN-{YYYYMMDD}-{UUID}
- The system has a 30-second timeout — never make synchronous calls
- Database is Oracle 12c — use Oracle-specific SQL syntax when needed

## Known quirks
- Refunds must be processed within the same billing cycle
- The `status` field uses integer codes, not strings (see mapping below)
- Always check `is_test_mode` before processing — test transactions exist in prod
```
