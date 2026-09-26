"""
_git_ops.py

Minimal Git operations for controlled repository publishing.

This module knows Git.
It does not know HAIR, Markdown, PDF, or application-specific concepts.
"""

from pathlib import Path
import subprocess


COMMIT_MESSAGE = (
    "Update Human-AI Alignment Context"
)


def _run_git(*args):

    return subprocess.run(
        ["git", *args],
        check=True,
        text=True
    )


def git_publish(
    paths,
    commit_message=COMMIT_MESSAGE
):

    repo_root = Path(
        subprocess.check_output(
            [
                "git",
                "rev-parse",
                "--show-toplevel"
            ],
            text=True
        ).strip()
    )

    print(
        f"[Git] Repository: {repo_root}"
    )


    print("\n[Git] Current status:")

    _run_git(
        "status",
        "--short"
    )


    print("\n[Git] Fetching remote state...")

    _run_git(
        "fetch"
    )


    local_head = subprocess.check_output(
        [
            "git",
            "rev-parse",
            "HEAD"
        ],
        text=True
    ).strip()


    remote_head = subprocess.check_output(
        [
            "git",
            "rev-parse",
            "@{u}"
        ],
        text=True
    ).strip()


    print(
        f"\n[Git] Local HEAD : {local_head}"
    )

    print(
        f"[Git] Remote HEAD: {remote_head}"
    )


    if local_head != remote_head:

        raise RuntimeError(
            "Local and remote repositories "
            "are not synchronized."
        )


    print(
        "\n[Git] Local and remote are synchronized."
    )


    print(
        "\n[Git] Human Inspection Gate"
    )


    confirmation = input(
        'Press "Y" + Enter to commit and push: '
    )


    if confirmation != "Y":

        print(
            "\n[Git] Exit without commit or push."
        )

        return


    _run_git(
        "add",
        *paths
    )


    _run_git(
        "commit",
        "-m",
        commit_message
    )


    _run_git(
        "push"
    )


    print(
        "\n[Git] Commit and push completed."
    )
