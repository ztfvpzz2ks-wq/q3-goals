---
name: Task
about: A concrete step that contributes to a goal
title: "🛠 "
labels: ["task"]
body:
  - type: input
    id: title
    attributes:
      label: Task
      description: A single actionable step.
      placeholder: "Wire the billing webhook into the checkout flow"
    validations:
      required: true
  - type: input
    id: goal
    attributes:
      label: Parent goal
      description: "Issue number of the goal this serves, e.g. #12"
      placeholder: "#12"
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
      placeholder: "2026-09-15"
    validations:
      required: false
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
    id: notes
    attributes:
      label: Notes
    validations:
      required: false
