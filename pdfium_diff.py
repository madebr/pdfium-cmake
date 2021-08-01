#!/usr/bin/env python

import os
import pathlib
import subprocess
import tempfile
import yaml

PDFIUM_CMAKE_ROOT = pathlib.Path(__file__).resolve().parent
SOURCES_YML = PDFIUM_CMAKE_ROOT / "sources.yml"

def main():
    sources = yaml.safe_load(SOURCES_YML.open())

    with tempfile.TemporaryDirectory() as tmpdir:
        subprocess.check_call(["git", "clone", sources["urls"][0]["git_url"], os.path.join(tmpdir, "pdfium")])
        subprocess.check_call(["git", "diff", "{}..{}".format(sources["branches"]["current"]["pdfium"], sources["branches"]["master"]["pdfium"]), "--", "*.gn"], cwd=os.path.join(tmpdir, "pdfium"))

if __name__ == "__main__":
    main()
