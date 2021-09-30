add_library(pdfium_constants OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/constants/access_permissions.h"
    "${PDFIUM_ROOT}/constants/annotation_common.cpp"
    "${PDFIUM_ROOT}/constants/annotation_common.h"
    "${PDFIUM_ROOT}/constants/annotation_flags.h"
    "${PDFIUM_ROOT}/constants/appearance.cpp"
    "${PDFIUM_ROOT}/constants/appearance.h"
    "${PDFIUM_ROOT}/constants/ascii.h"
    "${PDFIUM_ROOT}/constants/form_fields.cpp"
    "${PDFIUM_ROOT}/constants/form_fields.h"
    "${PDFIUM_ROOT}/constants/form_flags.h"
    "${PDFIUM_ROOT}/constants/page_object.cpp"
    "${PDFIUM_ROOT}/constants/page_object.h"
    "${PDFIUM_ROOT}/constants/stream_dict_common.cpp"
    "${PDFIUM_ROOT}/constants/stream_dict_common.h"
    "${PDFIUM_ROOT}/constants/transparency.cpp"
    "${PDFIUM_ROOT}/constants/transparency.h"
)
add_library(pdfium::constants ALIAS pdfium_constants)
target_link_libraries(pdfium_constants
    PRIVATE
        pdfium::strict_config
)
