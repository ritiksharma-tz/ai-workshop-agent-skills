---
name: react-component
description: >
  Scaffolds a new React component with TypeScript, test file,
  Storybook story, and barrel export. Use when the user wants
  to create a new component, add a component, or scaffold UI elements.
allowed-tools: Read Glob Write
---

# React Component Scaffolder

## Arguments
$ARGUMENTS should be the component name in PascalCase (e.g., SearchBar).

## Steps

1. **Determine the component location**
   - Check if `src/components/` exists; if so, use it
   - Otherwise check for `components/` at the project root
   - Ask the user if neither exists

2. **Create the component directory**
   Create `<location>/$ARGUMENTS/`

3. **Component file** (`$ARGUMENTS.tsx`)
   - Functional component with TypeScript props interface
   - Follow pattern in [examples/Example.tsx](examples/Example.tsx)

4. **Test file** (`$ARGUMENTS.test.tsx`)
   - Import from `@testing-library/react`
   - Include a render test and a basic interaction test
   - Follow pattern in [examples/Example.test.tsx](examples/Example.test.tsx)

5. **Story file** (`$ARGUMENTS.stories.tsx`)
   - Use Component Story Format (CSF) 3.0
   - Include Default and WithProps stories

6. **Barrel export** (`index.ts`)
   - Re-export the component as both named and default

7. **Update parent barrel**
   - If a parent `index.ts` exists, add the new export line
