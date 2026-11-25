import os
from pathlib import Path

LINE = "Meeting Dodger: an agent that sits through your meetings, nods wisely, and reports back 'nothing happened'."

def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
