"""
pdf2md.py

Convert reference PDF materials into Markdown format
using PyMuPDF4LLM.
"""

from pathlib import Path
import sys

import pymupdf4llm as pf4llm

from _reference._ref_material_list import REF_MATERIALS


LLM_REF_DIR = Path("_llm_ref")
LLM_REF_DIR.mkdir(exist_ok=True)


def convert_pdf(pdf_path):
    pdf_path = Path(pdf_path)
    md_path = LLM_REF_DIR / pdf_path.with_suffix(".md").name

    md_path.write_text(
        pf4llm.to_markdown(pdf_path),
        encoding="utf-8"
    )

    print(f"[OK] {pdf_path} -> {md_path}")


if len(sys.argv) > 1:
    convert_pdf(sys.argv[1])
else:
    for pdf in REF_MATERIALS:
        convert_pdf(pdf)
