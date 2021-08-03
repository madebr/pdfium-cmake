#!/usr/bin/env python

import os
import pathlib
import subprocess
import tempfile
import yaml

PDFIUM_CMAKE_ROOT = pathlib.Path(__file__).resolve().parent
SOURCES_YML = PDFIUM_CMAKE_ROOT / "sources.yml"


def git_diff(sources, module):
    with tempfile.TemporaryDirectory() as tmpdir:
        print("="*40)
        print("module:", module)
        print("-"*40)
        print("Cloning git...")
        subprocess.check_call([
            "git", "clone",
            "-b", sources["branches"]["master"][module],
            sources["urls"][module]["git_url"],
            os.path.join(tmpdir, module),

        ])
        print("-"*40)
        print("Master git hash:")
        subprocess.check_call([
            "git", "rev-parse", "HEAD",
        ], cwd=os.path.join(tmpdir, module))
        print("(current is:", sources["branches"]["current"][module], ")")
        print("-"*40)
        print("git diff:")
        subprocess.call([
            "git", "diff",
            "{}..{}".format(
                sources["branches"]["current"][module],
                sources["branches"]["master"][module]),
            "--", "*.gn"
        ], cwd=os.path.join(tmpdir, module))
        print("="*40)

def main():
    sources = yaml.safe_load(SOURCES_YML.open())
    for module in sources["modules"]:
        git_diff(sources, module)


if __name__ == "__main__":
    main()
