add_library(pdfium_core_fpdftext OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_linkextract.cpp"
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_linkextract.h"
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_textpage.cpp"
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_textpage.h"
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_textpagefind.cpp"
    "${PDFIUM_ROOT}/core/fpdftext/cpdf_textpagefind.h"
    "${PDFIUM_ROOT}/core/fpdftext/unicodenormalizationdata.cpp"
    "${PDFIUM_ROOT}/core/fpdftext/unicodenormalizationdata.h"
)
add_library(pdfium::core_fpdftext ALIAS pdfium_core_fpdftext)
target_link_libraries(pdfium_core_fpdftext
    PRIVATE
        pdfium::strict_config
    PUBLIC
        pdfium::constants
        pdfium::core_fpdfapi_font
        pdfium::core_fpdfapi_page
        pdfium::core_fpdfapi_parser
        pdfium::core_fxcrt
)
