---
name: documentation
description: Generate comprehensive system documentation including architecture, data flows, sequence diagrams, PII data handling, security, features, modules, and configurable design documentation for any repository. All output goes to the docs/ directory. Use when asked to generate documentation, create system docs, document a codebase, produce architecture docs, create security documentation, generate PII documentation, or when the user wants comprehensive project documentation with Mermaid diagrams. Supports selective generation via arguments (e.g., "only architecture and security").
---

# System Documentation Generator

Generate production-quality system documentation for any software repository. Output location: `docs/` at the repository root.

## Arguments

- `$ARGUMENTS` — Optional: specify which documentation types to generate or provide context. If empty, generate all 9 core documents plus applicable domain-specific docs.

## Core Documents

| # | File | Content |
|---|------|---------|
| 1 | `ARCHITECTURE.md` | System architecture, tech stack, deployment topology |
| 2 | `DATA_FLOW.md` | Data flow diagrams and transformation pipelines |
| 3 | `SEQUENCE_DIAGRAMS.md` | Sequence diagrams for key workflows (min 5) |
| 4 | `PII_DATA.md` | PII classification, handling, compliance |
| 5 | `DATA_SECURITY.md` | Security architecture, auth, encryption, RBAC |
| 6 | `FEATURES_LIST.md` | Feature inventory with status (min 20 features) |
| 7 | `MODULES_LIST.md` | Module breakdown, responsibilities, dependencies |
| 8 | `CONFIGURABLE_DESIGN.md` | Configurable parameters, defaults, env vars |
| 9 | `README.md` | Documentation index with cross-references |

## Domain-Specific Documents (conditional)

Detect during repo analysis and generate if applicable:

| Condition | Document |
|-----------|----------|
| Business logic / rules engine present | `BUSINESS_LOGIC.md` or `RULE_ENGINE.md` |
| Mathematical computations / algorithms | `COMPUTATIONS.md` or `ALGORITHMS.md` |
| API-focused system | `API_REFERENCE.md` |
| Data-intensive system / complex models | `DATA_MODEL.md` |

## Execution

### Phase 1: Repository Analysis

1. **Structure scan** — Explore directory structure (depth 3), identify source code organization
2. **Tech stack detection** — Find config files (`package.json`, `pom.xml`, `requirements.txt`, `Cargo.toml`, `go.mod`, `*.csproj`, `Dockerfile`, etc.) to determine languages, frameworks, databases, infra
3. **System classification** — Classify as: Web App, API Service, Microservices, Monolith, Library, CLI Tool, Mobile App, or Desktop App
4. **Domain identification** — Analyze source code for: business logic components, data pipelines, integration points, user-facing features, background jobs, configuration systems
5. **Determine applicable domain docs** — Based on analysis, decide which domain-specific documents to generate

### Phase 2: Generate Core Documents

Create `docs/` directory if missing. Generate each document using templates from [references/core-templates.md](references/core-templates.md).

**Per-document requirements:**

- **ARCHITECTURE.md**: Min 1 Mermaid diagram showing system components. Document all technologies with versions, services/modules, ports, endpoints, deployment topology, security boundaries.
- **DATA_FLOW.md**: Min 3 detailed data flow scenarios. Include happy path and error flows, data transformations, batch processing if applicable, integration points.
- **SEQUENCE_DIAGRAMS.md**: Min 5 sequence diagrams covering: authentication, primary workflow, data creation/modification, background processing, error handling. Use `autonumber`, include `alt`/`opt` blocks.
- **PII_DATA.md**: Identify ALL PII fields, classify by sensitivity (HIGH/MEDIUM/LOW), document encryption, masking rules, retention, compliance mapping (GDPR/CCPA/HIPAA).
- **DATA_SECURITY.md**: Authentication mechanism, authorization model (RBAC/ABAC), encryption (at rest + in transit), network security, security headers, audit logging, incident response.
- **FEATURES_LIST.md**: Min 20 features categorized logically. Status indicators: IMPLEMENTED, IN PROGRESS, PLANNED, NOT PLANNED.
- **MODULES_LIST.md**: ALL modules/services with file/package structure, responsibilities, API endpoints, dependencies, database usage.
- **CONFIGURABLE_DESIGN.md**: ALL configurable parameters with defaults, valid ranges, config examples (YAML/JSON/env vars), best practices.
- **README.md**: Documentation index, quick reference by audience (developers, security/compliance), document summaries, diagram types used.

### Phase 3: Generate Domain-Specific Documents

If applicable, generate domain-specific documents using templates from [references/domain-templates.md](references/domain-templates.md).

### Phase 4: Quality Validation

**Completeness check** per document:
- All required sections present
- At least one Mermaid diagram
- All tables properly formatted
- No placeholder text (except `[TBD]` with reasons)
- Version history present

**Consistency check** across documents:
- Consistent technology naming
- Consistent service/module naming
- Valid cross-references
- No contradictory information

**Diagram validation:**
- Valid Mermaid syntax
- All nodes connected
- Meaningful labels
- Appropriate use of subgraphs

### Phase 5: Report

Output a summary:
- List of created documents
- Documented components summary
- Areas needing manual review
- Any `[TBD]` items with reasons

## Quality Standards

- **Comprehensive**: Document ALL components, not just major ones
- **Visual first**: Diagrams wherever possible
- **Actionable**: Information should be immediately useful
- **No implementation code** (pseudocode OK)
- **No sensitive data** — use placeholder values
- **Cross-reference** related documents
- **Progressive disclosure** — overview first, details follow
- **Mark unknowns**: Use `[TBD]` or `[NEEDS VERIFICATION]`, never fabricate
