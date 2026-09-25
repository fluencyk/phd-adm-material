"""
_generate_hair_urls.py

Generate LLM-alignment URL manifest
from converted Markdown materials.

Input:
    _llm_ref/_hair_xxx/*.md

Output:
    _hair_urls_xxx.json

"""

from pathlib import Path
import json
import sys


HAIR_REF_MAP = {

    "profile":
        "_llm_ref/_hair_profile",

    "research":
        "_llm_ref/_hair_research",

    "submitted_docs":
        "_llm_ref/_hair_submitted_docs"

}


GITHUB_RAW_PREFIX = (
    "https://raw.githubusercontent.com/"
    "fluencyk/phd-adm-material/main/"
)



category = sys.argv[1]


if category not in HAIR_REF_MAP:

    raise ValueError(
        f"Unsupported category: {category}"
    )


target_dir = Path(
    HAIR_REF_MAP[category]
)


if not target_dir.exists():

    raise FileNotFoundError(
        f"Directory not found: {target_dir}"
    )


md_files = list(
    target_dir.glob("*.md")
)


if not md_files:

    raise FileNotFoundError(
        f"No markdown files found in {target_dir}"
    )


url_list = []


for md_file in md_files:

    path_as_str = md_file.as_posix()

    url = (
        GITHUB_RAW_PREFIX
        + path_as_str
    )

    url_list.append(url)



output_file = (
    target_dir
    /
    f"_hair_urls_{category}.json"
)


hair_urls = {
    category: url_list
}


json_text = json.dumps(
    hair_urls,
    indent=4,
    ensure_ascii=False
)


output_file.write_text(

    "\n"
    + json_text
    + "\n",
    encoding="utf-8"

)


print(
    f"[OK] Generated: {output_file}"
)


print("\n")
print(json_text)
print("\n")
