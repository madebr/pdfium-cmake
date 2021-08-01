# CMake build system for pdfium

This repo provides cmake build scripts for [pdfium](https://opensource.google/projects/pdfium).
The upstream project uses [gn](https://gn.googlesource.com/gn/), one of many symptoms of Google's NIH syndrome.

The aim of this repo is to ease building pdfium for multiple platforms.
Third party dependencies are provided by system packages, instead of vendored libraries.

## Usage

1. Download pdfium sources using the `download_pdfium.py` python script
2. Run cmake with the `PDFIUM_ROOT` configuration variable set to the location of the downloaded sources.
   It has some options to enable/disable features (not all features are currently supported).
   All pdfium related options have a `PDF_` prefix.

## Test coverage

### Tested platforms

The cmake scripts are tested by CI on:
- Linux
- Windows

Patches for testing + running on other platforms are welcome.

### Tested options

- Pdfium is built in static and shared configuration

Only the default options are currently tested.
Code for building pdfium sources making use of skia/v8 is implemented but not working.
Patches are welcome.
