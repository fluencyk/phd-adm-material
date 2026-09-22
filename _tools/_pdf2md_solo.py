"""
_pdf2md_solo.py

Convert a single reference PDF into Markdown format
using PyMuPDF4LLM.

@ Solo Converting Version (for dry-run testing only)
"""

from pathlib import Path

import pymupdf4llm as pf4llm

from _reference._ref_material_list import REF_MATERIALS


LLM_REF_DIR = Path("_llm_ref")
LLM_REF_DIR.mkdir(exist_ok=True)


while True:

    pdf_index = input(
        "Type the Converting-Ready PDF Index: "
    )

    if not pdf_index.isdigit():
        print("Please type a number.")
        continue

    pdf_index = int(pdf_index)

    if pdf_index in range(len(REF_MATERIALS)):
        break

    print("Not a right index number, try again!")


pdf_path = Path(REF_MATERIALS[pdf_index])
md_path = LLM_REF_DIR / pdf_path.with_suffix(".md").name

md_path.write_text(
    pf4llm.to_markdown(pdf_path),
    encoding="utf-8"
)

print(f"[OK] {pdf_path} -> {md_path}")
