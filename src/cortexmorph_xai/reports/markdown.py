from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


def write_markdown_report(
    output_path: str | Path,
    title: str,
    sections: dict[str, dict[str, object] | str],
) -> None:
    lines = [f"# {title}", "", f"Created: {datetime.now(timezone.utc).isoformat()}", ""]

    for section_title, content in sections.items():
        lines.append(f"## {section_title}")
        lines.append("")

        if isinstance(content, str):
            lines.append(content)
        else:
            for key, value in content.items():
                lines.append(f"- **{key}**: {value}")

        lines.append("")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
