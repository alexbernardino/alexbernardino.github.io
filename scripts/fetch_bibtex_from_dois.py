#!/usr/bin/env python3
"""
Fetch BibTeX records for a list of DOIs.

Usage:
  python3 fetch_bibtex_from_dois.py journal_dois.txt publications_journals.bib

The input file should contain one DOI per line, for example:
  10.1016/j.robot.2021.103857
  https://doi.org/10.1016/j.robot.2021.103857
"""

from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DOI_RE = re.compile(r"(10\.\d{4,9}/\S+)", re.IGNORECASE)


def normalize_doi(line: str) -> str | None:
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    line = line.replace("https://doi.org/", "")
    line = line.replace("http://doi.org/", "")
    line = line.replace("https://www.doi.org/", "")
    line = line.replace("http://www.doi.org/", "")
    line = line.replace("doi:", "")
    line = line.strip().rstrip(" .;,")

    m = DOI_RE.search(line)
    if not m:
        return None

    return m.group(1).rstrip(" .;,")


def fetch_bibtex(doi: str, email: str | None = None) -> str:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://doi.org/{encoded}"

    headers = {
        "Accept": "application/x-bibtex; charset=utf-8",
        "User-Agent": "doi-bibtex-fetcher/1.0",
    }
    if email:
        headers["User-Agent"] += f" (mailto:{email})"

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request, timeout=30) as response:
        data = response.read()
        return data.decode("utf-8", errors="replace").strip()


def add_url_if_missing(bibtex: str, doi: str) -> str:
    # Many DOI BibTeX records include doi but not url. For your Jekyll template,
    # adding url makes the [paper] link straightforward.
    if re.search(r"\n\s*url\s*=", bibtex, re.IGNORECASE):
        return bibtex

    doi_url = f"https://doi.org/{doi}"
    idx = bibtex.rfind("}")
    if idx == -1:
        return bibtex

    insertion = f",\n  url = {{{doi_url}}}\n"
    return bibtex[:idx].rstrip().rstrip(",") + insertion + bibtex[idx:]


def main() -> int:
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_bibtex_from_dois.py journal_dois.txt publications_journals.bib")
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2])
    failed_path = output_path.with_suffix(".failed.txt")

    raw_lines = input_path.read_text(encoding="utf-8").splitlines()
    dois = []
    seen = set()

    for line in raw_lines:
        doi = normalize_doi(line)
        if doi and doi.lower() not in seen:
            dois.append(doi)
            seen.add(doi.lower())

    print(f"Found {len(dois)} unique DOIs")

    bib_entries: list[str] = []
    failed: list[str] = []

    for i, doi in enumerate(dois, start=1):
        print(f"[{i}/{len(dois)}] {doi}")
        try:
            bib = fetch_bibtex(doi)
            bib = add_url_if_missing(bib, doi)
            bib_entries.append(bib)
        except urllib.error.HTTPError as e:
            failed.append(f"{doi}\tHTTP {e.code}: {e.reason}")
            print(f"  FAILED: HTTP {e.code}: {e.reason}")
        except Exception as e:
            failed.append(f"{doi}\t{type(e).__name__}: {e}")
            print(f"  FAILED: {type(e).__name__}: {e}")

        # Be polite to DOI/Crossref infrastructure.
        time.sleep(0.3)

    output_path.write_text("\n\n".join(bib_entries) + "\n", encoding="utf-8")
    failed_path.write_text("\n".join(failed) + ("\n" if failed else ""), encoding="utf-8")

    print()
    print(f"Wrote: {output_path}")
    print(f"Failed: {len(failed)}")
    if failed:
        print(f"See: {failed_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
