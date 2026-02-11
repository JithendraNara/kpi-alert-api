from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_EXPORT_DIR = BASE_DIR.parent / "lakehouse-analytics-platform" / "data" / "exports"


def get_export_dir() -> Path:
    return Path(os.getenv("LAKEHOUSE_EXPORT_DIR", DEFAULT_EXPORT_DIR))
