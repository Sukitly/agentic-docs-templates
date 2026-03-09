#!/usr/bin/env python3
"""
Documentation integrity checker.

Checks:
1. All relative markdown links in docs/, ARCHITECTURE.md, AGENTS.md point to existing files
2. exec-plans/index.md and design-docs/index.md cover all files in their directories
3. Exec plan structure validation (required frontmatter fields and sections)
4. ARCHITECTURE.md references existing paths
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []


# ── Helpers ──────────────────────────────────────────────────────────


def strip_html_comments(content: str) -> str:
    """Remove HTML comment blocks from content."""
    return re.sub(r"<!--.*?-->", "", content, flags=re.DOTALL)


def extract_markdown_links(content: str) -> list[str]:
    """Extract relative markdown links from content, skipping external/anchor links and HTML comments."""
    content = strip_html_comments(content)
    links = []
    for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", content):
        link = match.group(1)
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        # Strip anchor fragment and query string
        link = link.split("#")[0].split("?")[0]
        if link:
            links.append(link)
    return links


def relative(path: Path) -> str:
    """Return path relative to ROOT."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def check_links_in_file(file_path: Path) -> None:
    """Check all relative markdown links in a file point to existing targets."""
    content = file_path.read_text(encoding="utf-8")
    links = extract_markdown_links(content)
    file_dir = file_path.parent

    for link in links:
        resolved = (file_dir / link).resolve()
        if not resolved.exists():
            errors.append(
                f'Broken link in {relative(file_path)}: "{link}" → {relative(resolved)} not found'
            )


# ── Check 1: All markdown links ─────────────────────────────────────

print("📄 Checking markdown links...")

md_files = list(ROOT.glob("docs/**/*.md"))
for top_level in ["ARCHITECTURE.md", "AGENTS.md"]:
    p = ROOT / top_level
    if p.exists():
        md_files.append(p)

for f in md_files:
    check_links_in_file(f)


# ── Check 2: Index coverage ─────────────────────────────────────────

print("📋 Checking index coverage...")


def check_index_covers_dir(index_path: str, dir_path: str, label: str) -> None:
    full_index = ROOT / index_path
    full_dir = ROOT / dir_path

    if not full_index.exists():
        errors.append(f"Missing index: {index_path}")
        return
    if not full_dir.exists():
        return

    index_content = full_index.read_text(encoding="utf-8")
    md_files_in_dir = [
        f.name for f in full_dir.iterdir() if f.suffix == ".md" and f.name != "index.md"
    ]

    for file_name in md_files_in_dir:
        if (
            f"({file_name})" not in index_content
            and f"/{file_name})" not in index_content
        ):
            errors.append(f'{label}: "{file_name}" not listed in {index_path}')


check_index_covers_dir(
    "docs/exec-plans/index.md", "docs/exec-plans/active", "exec-plans/active"
)
check_index_covers_dir(
    "docs/exec-plans/index.md", "docs/exec-plans/completed", "exec-plans/completed"
)
check_index_covers_dir("docs/design-docs/index.md", "docs/design-docs", "design-docs")


# ── Check 3: Exec plan structure validation ──────────────────────────

print("📐 Checking exec-plan structure...")

REQUIRED_FRONTMATTER = ["Created", "Last updated", "Status"]
REQUIRED_FRONTMATTER_ACTIVE = ["Priority"]
REQUIRED_SECTIONS_ACTIVE = ["## Progress Log", "## Decision Log"]

for dir_name in ["docs/exec-plans/active", "docs/exec-plans/completed"]:
    full_dir = ROOT / dir_name
    if not full_dir.exists():
        continue
    is_active = "active" in dir_name
    for f in full_dir.glob("*.md"):
        content = f.read_text(encoding="utf-8")
        file_name = relative(f)

        for field in REQUIRED_FRONTMATTER:
            if f"**{field}**" not in content:
                errors.append(
                    f'{file_name}: missing required frontmatter field "{field}"'
                )

        if is_active:
            for field in REQUIRED_FRONTMATTER_ACTIVE:
                if f"**{field}**" not in content:
                    errors.append(
                        f'{file_name}: missing required frontmatter field "{field}"'
                    )
            for section in REQUIRED_SECTIONS_ACTIVE:
                if section not in content:
                    errors.append(f'{file_name}: missing required section "{section}"')


# ── Check 4: ARCHITECTURE.md path references ────────────────────────

print("🏗️  Checking ARCHITECTURE.md path references...")

arch_file = ROOT / "ARCHITECTURE.md"
if arch_file.exists():
    arch_content = arch_file.read_text(encoding="utf-8")
    # Extract backtick-quoted paths (e.g., `src/server/`, `lib/utils.ts`)
    for match in re.finditer(r"`([a-zA-Z][a-zA-Z0-9_\-./]+/?)`", arch_content):
        path_ref = match.group(1)
        # Only check paths that look like file/directory references (contain /)
        if "/" not in path_ref:
            continue
        # Skip if inside a <!-- CUSTOMIZE --> comment block or example
        if path_ref.startswith("#"):
            continue
        full_path = ROOT / path_ref.rstrip("/")
        if not full_path.exists():
            errors.append(f'ARCHITECTURE.md references non-existent path: "{path_ref}"')


# ── Results ──────────────────────────────────────────────────────────

print()
if errors:
    print(f"❌ Found {len(errors)} documentation issue(s):\n", file=sys.stderr)
    for error in errors:
        print(f"  • {error}", file=sys.stderr)
    sys.exit(1)
else:
    print("✅ All documentation checks passed.")
