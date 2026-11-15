---
name: Weekly note
about: A short status update for the week
title: "📝 "
labels: ["note"]
body:
  - type: input
    id: week
    attributes:
      label: Week of
      placeholder: "2026-W37"
    validations:
      required: true
  - type: textarea
    id: done
    attributes:
      label: What moved forward?
    validations:
      required: true
  - type: textarea
    id: stuck
    attributes:
      label: What is stuck, and what is needed to unblock it?
    validations:
      required: true
  - type: textarea
    id: next
    attributes:
      label: Focus for next week
    validations:
      required: false
