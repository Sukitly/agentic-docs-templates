# Architecture

> This document is the architecture map of the codebase.
> The agent should understand module structure and dependency rules here before diving into specific code.
>
> **Last updated**: YYYY-MM-DD

---

## High-level Architecture

<!-- CUSTOMIZE: Describe your application's high-level architecture -->
<!-- Example:
```
User Request → Middleware (auth + routing)
             → Application Layer
             → Business Logic
             → Data Layer (Database)
```
-->

---

## Directory Structure & Responsibilities

<!-- CUSTOMIZE: Map out your project's directory structure and each directory's role -->
<!-- Example:
```
src/
├── app/               # Entry points / routes
├── server/            # Server-side logic
├── components/        # Shared UI components
├── lib/               # Shared utilities
└── types/             # Shared type definitions
```
-->

---

## Layering Rules

<!-- CUSTOMIZE: Define dependency direction rules between layers -->
<!-- Example:
- UI layer → Business logic → Data layer (never reverse)
- Shared utilities can be imported by any layer
- Data layer must not import from UI layer
-->

---

## Cross-cutting Concerns

<!-- CUSTOMIZE: Describe how the following are handled across the codebase -->
<!-- Topics to consider:
- Authentication & Authorization
- Error handling
- Logging
- Input validation
- Internationalization
-->

---

## Key Conventions

<!-- CUSTOMIZE: List important conventions that affect architecture decisions -->
