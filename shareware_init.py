#!/usr/bin/env python3
"""
shareware-init: Initialize a new repository with the RespectTheLoader pattern.

This is the MVP stub for what will eventually become `git shareware-init`.
It creates the basic structure needed to protect golden builds from accidental
modification while providing safe experimental spaces.

Usage:
    python shareware_init.py <target_directory>
    python shareware_init.py --help

Example:
    python shareware_init.py ./my-new-project

This will create:
    my-new-project/
    ├── shareware.yml      # Manifest for protected versions
    ├── archive/           # Protected golden builds directory
    │   └── README.md
    └── lab/               # Experimental workspace
        └── README.md
"""

import argparse
import os
import sys

__version__ = "1.0.0"

# Template content for the manifest
SHAREWARE_YML_TEMPLATE = """\
# RespectTheLoader Manifest
# Define your canonical versions here.
# Versions with `protected: true` should not be modified.

versions:
  v1-initial:
    path: archive/v1-initial
    entry: README.md
    role: initial-release
    protected: true
    placeholder: true  # Remove this line once you add actual content

# Add more versions as your project grows:
#   v2-feature:
#     path: archive/v2-feature
#     protected: true
"""

ARCHIVE_README_TEMPLATE = """\
# Archive Directory

This directory contains **protected golden builds**.

## Rules

1. Files in this directory should NOT be modified once committed
2. Each subdirectory represents a canonical version
3. Protection status is defined in `shareware.yml`
4. To experiment, use the `/lab/` directory instead

## Adding New Versions

1. Create your build in `/lab/` first
2. When ready, copy to `/archive/vX-name/`
3. Add entry to `shareware.yml` with `protected: true`
4. Commit and never modify again

*Respect the Loader. The archive is eternal.*
"""

LAB_README_TEMPLATE = """\
# Lab Directory

This is your **experimental workspace**.

## Rules

1. This directory is git-ignored by default
2. Feel free to experiment, break things, iterate
3. Nothing here is permanent or protected
4. When ready to preserve work, promote to `/archive/`

## Workflow

```bash
# Create an experiment
mkdir my-experiment
cd my-experiment
# ... do your work ...

# When ready to preserve
cp -r . ../../archive/vX-my-feature/
# Update shareware.yml with new version
```

*The lab is chaos. Embrace it.*
"""

GITIGNORE_ADDITION = """\
# RespectTheLoader: Ignore lab directory
/lab/*
!/lab/README.md
"""


def create_directory(path: str) -> None:
    """Create a directory if it doesn't exist."""
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"  Created: {path}/")


def write_file(path: str, content: str, overwrite: bool = False) -> None:
    """Write content to a file."""
    if os.path.exists(path) and not overwrite:
        print(f"  Skipped: {path} (already exists)")
        return

    with open(path, "w") as f:
        f.write(content)
    print(f"  Created: {path}")


def init_shareware_structure(target_dir: str) -> int:
    """
    Initialize a new directory with the RespectTheLoader structure.

    Args:
        target_dir: Path to the target directory

    Returns:
        0 on success, 1 on failure
    """
    target_dir = os.path.abspath(target_dir)

    print(f"\nInitializing RespectTheLoader structure in: {target_dir}\n")

    # Create target directory if needed
    create_directory(target_dir)

    # Create archive directory
    archive_dir = os.path.join(target_dir, "archive")
    create_directory(archive_dir)
    write_file(os.path.join(archive_dir, "README.md"), ARCHIVE_README_TEMPLATE)

    # Create lab directory
    lab_dir = os.path.join(target_dir, "lab")
    create_directory(lab_dir)
    write_file(os.path.join(lab_dir, "README.md"), LAB_README_TEMPLATE)

    # Create shareware.yml manifest
    write_file(os.path.join(target_dir, "shareware.yml"), SHAREWARE_YML_TEMPLATE)

    # Append to .gitignore if it exists, or create it
    gitignore_path = os.path.join(target_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            existing = f.read()
        if "/lab/" not in existing:
            with open(gitignore_path, "a") as f:
                f.write("\n" + GITIGNORE_ADDITION)
            print("  Updated: .gitignore (added lab/ exclusion)")
        else:
            print("  Skipped: .gitignore (lab/ already ignored)")
    else:
        write_file(gitignore_path, GITIGNORE_ADDITION)

    print("\n✓ RespectTheLoader structure initialized!")
    print("\nNext steps:")
    print("  1. Review shareware.yml and customize for your project")
    print("  2. Add your first golden build to archive/v1-initial/")
    print("  3. Update shareware.yml to remove 'placeholder: true'")
    print("  4. Commit your structure:")
    print("     git add . && git commit -m 'init: add RespectTheLoader structure'")
    print("\nLearn more: https://github.com/stusatwork-oss/respecttheloader")

    return 0


def main() -> int:
    """Main entry point for shareware-init CLI."""
    parser = argparse.ArgumentParser(
        description="Initialize a new repository with the RespectTheLoader pattern.",
        epilog="Example: python shareware_init.py ./my-project",
    )
    parser.add_argument(
        "target",
        nargs="?",
        default=".",
        help="Target directory to initialize (default: current directory)",
    )
    parser.add_argument(
        "--version", action="version", version=f"shareware-init {__version__}"
    )

    args = parser.parse_args()

    return init_shareware_structure(args.target)


if __name__ == "__main__":
    sys.exit(main())
