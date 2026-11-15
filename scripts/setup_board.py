#!/usr/bin/env python3
"""Create or sync a GitHub Projects v2 board from a repository's issues.

Usage:
    python scripts/setup_board.py --repo OWNER/REPO [--title "Quarter Goals"] [--sync]

Requires:
    * gh CLI, authenticated:  gh auth login
    * gh CLI with the `project` scope:  gh auth refresh -s project
    * Python 3.10+
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

STATUS_OPTIONS = ["Backlog", "In progress", "In review", "Done"]
PRIORITY_OPTIONS = ["High", "Medium", "Low"]


def gh(*args: str, check: bool = True) -> str:
    result = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and result.returncode != 0:
        sys.exit("gh " + " ".join(args) + " failed:\n" + result.stderr.strip())
    return result.stdout


def gh_json(*args: str) -> object:
    return json.loads(gh(*args))


def owner_of(repo: str) -> str:
    return repo.split("/")[0]


def list_issues(repo: str) -> list[dict]:
    raw = gh(
        "issue", "list",
        "--repo", repo,
        "--state", "open",
        "--limit", "200",
        "--json", "number,title,body,labels,url",
    )
    return json.loads(raw)


def pick_due(body: str) -> str:
    marker = body.lower().find("due date")
    if marker == -1:
        return ""
    for line in body[marker:].splitlines()[1:]:
        line = line.strip()
        if line:
            return line
    return ""


def pick_owner(body: str) -> str:
    for line in body.splitlines():
        if "@" in line:
            return line.strip().lstrip("*").strip()
    return ""


def find_project(owner: str, title: str) -> int | None:
    for project in gh_json("project", "list", "--owner", owner, "--format", "json"):
        if project.get("title") == title:
            return int(project["number"])
    return None


def create_project(owner: str, title: str) -> int:
    out = gh_json("project", "create", "--owner", owner, "--title", title, "--format", "json")
    return int(out["number"])


def field_ids(project_number: int) -> dict:
    fields = gh_json("project", "field-list", str(project_number), "--format", "json")
    return {f.get("name"): f.get("id") for f in fields.get("fields", [])}


def add_issue_to_board(project_number: int, owner: str, url: str) -> str | None:
    out = gh_json(
        "project", "item-add", str(project_number),
        "--owner", owner,
        "--url", url,
        "--format", "json",
    )
    return out.get("id")


def set_field(project_number: int, item_id: str, field_id: str, value: str) -> None:
    gh(
        "project", "item-edit",
        "--id", item_id,
        "--project-id", str(project_number),
        "--field-id", field_id,
        "--text", value,
        check=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo", required=True, help="OWNER/REPO")
    parser.add_argument("--title", default="Quarter Goals")
    parser.add_argument("--sync", action="store_true", help="only update an existing board")
    args = parser.parse_args()

    owner = owner_of(args.repo)

    number = find_project(owner, args.title)
    if number is None:
        if args.sync:
            sys.exit("Project " + repr(args.title) + " not found. Run without --sync first.")
        number = create_project(owner, args.title)
        print("Created project #" + str(number) + ": " + args.title)
    else:
        print("Using project #" + str(number) + ": " + args.title)

    fields = field_ids(number)
    for name in ("Status", "Priority", "Due Date"):
        if name not in fields:
            print("Field " + repr(name) + " is missing — create it in the project UI once.")

    for issue in list_issues(args.repo):
        labels = [l.get("name", "").lower() for l in issue.get("labels", [])]
        body = issue.get("body") or ""
        item_id = add_issue_to_board(number, owner, issue.get("url", ""))
        if not item_id:
            continue
        due = pick_due(body)
        if due and "Due Date" in fields:
            set_field(number, item_id, fields["Due Date"], due)
        print("Added issue #" + str(issue.get("number")) + ": " + issue.get("title", ""))

    print("Done. Open the board with: gh project view " + str(number) + " --owner " + owner)


if __name__ == "__main__":
    main()
