#!/usr/bin/env python
import argparse
import os
import pathlib
import tarfile

import requests
import yaml

PDFIUM_CMAKE_ROOT = pathlib.Path(__file__).resolve().parent
SOURCES_YML = PDFIUM_CMAKE_ROOT / "sources.yml"


def main():
    parser = argparse.ArgumentParser(description="Download pdfium sources")
    parser.add_argument("--branch", default="current", help="What branch to download (see sources.yml)")
    parser.add_argument("--destination", default="pdfium", help="Where to extract pdfium")
    ns = parser.parse_args()

    sources = yaml.safe_load(SOURCES_YML.open())

    destination = ns.destination
    print(f"Extracting pdfium to {destination}")

    branches = sources["branches"][ns.branch]

    for source in sources["urls"]:
        name = source["name"]
        url = source["url_format"].format(branch=branches[name])
        print(f"Downloading {name} from {url}...")

        response = requests.get(url, stream=True)
        file = tarfile.open(fileobj=response.raw, mode="r|gz")
        file.extractall(path=os.path.join(destination, source["extract_path"]))


if __name__ == "__main__":
    main()
