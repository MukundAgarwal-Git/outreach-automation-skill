#!/usr/bin/env python3
"""
Package the outreach-skill directory into a .skill file for distribution.
"""

import os
import zipfile
from pathlib import Path


def package_skill(skill_dir: str, output_dir: str = "."):
    """
    Package a skill directory into a .skill zip file.

    Args:
        skill_dir: Path to the skill directory
        output_dir: Where to save the .skill file
    """
    skill_path = Path(skill_dir)
    if not skill_path.exists():
        raise FileNotFoundError(f"Skill directory not found: {skill_dir}")

    # Read SKILL.md to get the skill name
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        raise FileNotFoundError("SKILL.md not found in skill directory")

    # Extract skill name from frontmatter
    import yaml
    with open(skill_md, 'r') as f:
        content = f.read()
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 2:
                frontmatter = yaml.safe_load(parts[1])
                skill_name = frontmatter.get('name', skill_path.name)
            else:
                skill_name = skill_path.name
        else:
            skill_name = skill_path.name

    # Create output filename
    output_path = Path(output_dir) / f"{skill_name}.skill"

    # Files to include
    include_patterns = [
        "SKILL.md",
        "README.md",
        "scripts/**/*",
        "references/**/*",
        "tests/**/*",
    ]

    # Files to exclude
    exclude_patterns = [
        ".claudeignore",
        "__pycache__",
        "*.pyc",
        ".git",
        ".DS_Store",
        "*.log",
        "temp",
        "data/",
        "attachments/",
    ]

    def should_include(filepath: Path) -> bool:
        rel_path = filepath.relative_to(skill_path)
        str_path = str(rel_path)

        # Check exclusions
        for pattern in exclude_patterns:
            if pattern.endswith('/'):
                if str_path.startswith(pattern):
                    return False
            elif pattern in str_path:
                return False

        # Check inclusions
        for pattern in include_patterns:
            if pattern.endswith('/**/*'):
                prefix = pattern[:-5]
                if str_path.startswith(prefix):
                    return True
            elif str_path == pattern or str_path.startswith(pattern + '/'):
                return True

        return False

    # Create zip file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for filepath in skill_path.rglob('*'):
            if filepath.is_file() and should_include(filepath):
                arcname = filepath.relative_to(skill_path)
                zf.write(filepath, arcname)
                print(f"Added: {arcname}")

    print(f"\nSkill packaged successfully: {output_path}")
    print(f"Size: {output_path.stat().st_size / 1024:.1f} KB")
    return output_path


if __name__ == "__main__":
    import sys
    skill_dir = sys.argv[1] if len(sys.argv) > 1 else "."
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    package_skill(skill_dir, output_dir)