---
name: Goal
about: A measurable outcome with a deadline and an owner
title: "🎯 "
labels: ["goal"]
body:
  - type: input
    id: outcome
    attributes:
      label: Outcome
      description: One sentence, starting with a verb, with a number in it.
      placeholder: "Ship the public beta to 200 weekly active users"
    validations:
      required: true
  - type: input
    id: metric
    attributes:
      label: How will we measure it?
      placeholder: "200 WAU, measured in the analytics dashboard"
    validations:
      required: true
  - type: input
    id: owner
    attributes:
      label: Owner
      placeholder: "@your-username"
    validations:
      required: true
  - type: input
    id: due
    attributes:
      label: Due date
      description: "ISO format, e.g. 2026-09-30 — this is what the CI checks"
      placeholder: "2026-09-30"
    validations:
      required: true
  - type: dropdown
    id: priority
    attributes:
      label: Priority
      options:
        - High
        - Medium
        - Low
    validations:
      required: true
  - type: textarea
    id: scope
    attributes:
      label: What is explicitly out of scope?
      description: The strongest goals are narrow. Say what you will NOT do.
      placeholder: "No iOS app, no payments, no third-party integrations"
    validations:
      required: false
  - type: textarea
    id: notes
    attributes:
      label: Notes
    validations:
      required: false
