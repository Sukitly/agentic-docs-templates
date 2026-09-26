# Deployment

> Document deploy targets, runtime configuration, smoke tests, and rollback notes. Keep this file current-state only; do not append deployment history.

---

<!-- CUSTOMIZE: Replace placeholder content with the project's actual deployment model. If the project has no deployment target, write "N/A — local/library project" with a short reason. -->

## Targets

| Component | Platform | Domain / Entry | Deploy Source |
|---|---|---|---|
| [Component] | [Platform] | [Domain or entry point] | [CI workflow / manual command / platform build] |

## Environments

| Environment | Purpose | Data Source | Notes |
|---|---|---|---|
| Local | Development | [Local DB / mocks / remote test service] | [Notes] |
| Staging | Pre-production validation | [Data source] | [Notes] |
| Production | User-facing runtime | [Data source] | [Notes] |

## Required Configuration

| Variable / Secret | Environment | Purpose | Owner / Where Set |
|---|---|---|---|
| `[NAME]` | [local/staging/prod] | [Purpose] | [Where to configure] |

## Deploy Commands

```bash
# Build
# <build command>

# Deploy
# <deploy command>
```

## Smoke Tests

```bash
# <smoke test command>
```

| Check | Expected Result |
|---|---|
| [Check] | [Expected result] |

## Rollback / Recovery

| Fault | Action |
|---|---|
| [Fault mode] | [Rollback or recovery action] |

## External Platform Checklist

- [ ] [External DNS / auth callback / webhook / storage / monitoring configuration item]
