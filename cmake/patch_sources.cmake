# Allow pure static libraries on Windows:
file(READ "${PDFIUM_ROOT}/public/fpdfview.h" _fpdfview_h)
if(BUILD_SHARED_LIBS)
    string(REPLACE "#define FPDF_EXPORT // __declspec(dllexpert)" "#define FPDF_EXPORT __declspec(dllexport)" _new_fpdfview_h "${_fpdfview_h}")
    string(REPLACE "#define FPDF_EXPORT // __declspec(dllimport)" "#define FPDF_EXPORT __declspec(dllimport)" _new_fpdfview_h "${_new_fpdfview_h}")
else()
    string(REPLACE "#define FPDF_EXPORT __declspec(dllexport)" "#define FPDF_EXPORT // __declspec(dllexpert)" _new_fpdfview_h "${_fpdfview_h}")
    string(REPLACE "#define FPDF_EXPORT __declspec(dllimport)" "#define FPDF_EXPORT // __declspec(dllimport)" _new_fpdfview_h "${_new_fpdfview_h}")
endif()
if(NOT _fpdfview_h STREQUAL _new_fpdfview_h)
    file(WRITE "${PDFIUM_ROOT}/public/fpdfview.h" "${_new_fpdfview_h}")
endif()

# don't use vendored abseil
file(READ "${PDFIUM_ROOT}/third_party/base/optional.h" _base_optional_h)
string(REPLACE "#include \"third_party/abseil-cpp/absl/types/optional.h\"" "#include <absl/types/optional.h>" _base_optional_h "${_base_optional_h}")
file(WRITE "${PDFIUM_ROOT}/third_party/base/optional.h" "${_base_optional_h}")

# missing <cstdint> header
file(READ "${PDFIUM_ROOT}/core/fxcodec/fx_codec.h" _fx_codec_h)
file(WRITE "${PDFIUM_ROOT}/core/fxcodec/fx_codec.h" "#include<cstdint>\n${_fx_codec_h}")
