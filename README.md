# Sprint/Quarter Planning Template

A ready-to-use GitHub template for planning a quarter or a sprint on **GitHub Projects v2**.

Fork it (or click **Use this template**) and you get, in one click:

- a **Project v2 board** with `Status`, `Priority` and `Due Date` fields
- pre-filled **issue templates** for goals, tasks and weekly notes
- a **CI workflow** that validates every new goal has a deadline and an owner
- a **script** that builds the board from your issues with one command

---

## Quick start

```bash
# 1. Create the board and its fields
python scripts/setup_board.py --repo YOUR_USER/YOUR_REPO

# 2. Open the board
gh project list --owner YOUR_USER
```

Requires the `gh` CLI (authenticated, scope `project`) and Python 3.10+.

---

## The board

| Field | Type | Meaning |
|---|---|---|
| `Status` | single select | `Backlog` -> `In progress` -> `In review` -> `Done` |
| `Priority` | single select | `High` / `Medium` / `Low` |
| `Due Date` | date | the only field that is mandatory for a goal |

Views worth setting up:

1. **Quarter goals** — everything, grouped by `Status`, sorted by `Due Date`
2. **This week** — `In progress` + `In review`, sorted by `Due Date`
3. **Overdue** — anything with a `Due Date` in the past and `Status != Done`
4. **High priority** — `Priority = High`, grouped by `Status`

---

## Writing goals

Use the **Goal** issue template. A good goal has:

- a **verb** — *ship*, *grow*, *reduce*, not *improve*
- a **measurable outcome** — a number, a date, a percentage
- a **deadline** — the `Due Date` field
- an **owner** — one name, not a committee

Example:

> **Ship** the public beta of the app to 200 weekly active users by **2026-09-30**. Owner: @you.

---

## Weekly rhythm

1. Monday: move `Backlog` -> `In progress`, confirm this week's `Due Date`
2. Wednesday: re-sync the board with `python scripts/setup_board.py --repo OWNER/REPO --sync`
3. Friday: move finished items to `Done`, close their issues

---

## CI

`.github/workflows/goals-lint.yml` runs on every issue and pull request. It fails when a goal issue is missing its deadline or its owner. That single rule is what keeps a board from rotting.

---

## License

MIT — use it, fork it, adapt it.
