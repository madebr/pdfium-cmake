add_library(pdfium_core_fpdfapi_edit OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_contentstream_write_utils.cpp"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_contentstream_write_utils.h"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_creator.cpp"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_creator.h"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_pagecontentgenerator.cpp"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_pagecontentgenerator.h"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_pagecontentmanager.cpp"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_pagecontentmanager.h"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_stringarchivestream.cpp"
    "${PDFIUM_ROOT}/core/fpdfapi/edit/cpdf_stringarchivestream.h"
)
add_library(pdfium::core_fpdfapi_edit ALIAS pdfium_core_fpdfapi_edit)
target_link_libraries(pdfium_core_fpdfapi_edit
    PRIVATE
        pdfium::strict_config
    PUBLIC
        pdfium::thirdparty_skia_shared
        pdfium::core_fxcrt
        pdfium::core_fpdfapi_font
        pdfium::core_fpdfapi_page
        pdfium::core_fpdfapi_parser
)
