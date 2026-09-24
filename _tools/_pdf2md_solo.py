"""
_pdf2md_solo.py

Convert a single reference PDF into Markdown format
using PyMuPDF4LLM.

@ Solo Converting Version (for dry-run testing only)
"""

from pathlib import Path

import pymupdf4llm as pf4llm

from _reference._ref_material_list import REF_MATERIALS

import sys


LLM_REF_MAP = {

    "profile":
    "_llm_ref/_hair_profile",

    "research":
    "_llm_ref/_hair_research",

    "submitted_docs":
    "_llm_ref/_hair_submitted_docs"

}


category = sys.argv[1]
index = int(sys.argv[2])


LLM_REF_DIR = Path(
    LLM_REF_MAP[category]
)

LLM_REF_DIR.mkdir(
    parents=True,
    exist_ok=True
)


pdf_path = Path(REF_MATERIALS[category][index])
md_path = LLM_REF_DIR / pdf_path.with_suffix(".md").name


if not pdf_path.is_file():
    raise FileNotFoundError(
        f"Reference PDF not found: {pdf_path}"
    )


md_path.write_text(
    pf4llm.to_markdown(pdf_path),
    encoding="utf-8"
)

print(f"[OK] {pdf_path} -> {md_path}")
