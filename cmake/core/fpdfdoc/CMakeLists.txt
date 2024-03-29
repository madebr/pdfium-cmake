add_library(pdfium_core_fpdfdoc OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_aaction.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_aaction.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_action.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_action.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_annot.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_annot.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_annotlist.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_annotlist.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_apsettings.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_apsettings.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bafontmap.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bafontmap.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bookmark.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bookmark.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bookmarktree.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_bookmarktree.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_color_utils.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_color_utils.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_defaultappearance.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_defaultappearance.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_dest.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_dest.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_filespec.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_filespec.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_formcontrol.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_formcontrol.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_formfield.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_formfield.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_generateap.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_generateap.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_icon.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_icon.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_iconfit.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_iconfit.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_interactiveform.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_interactiveform.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_link.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_link.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_linklist.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_linklist.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_metadata.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_metadata.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_nametree.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_nametree.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_numbertree.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_numbertree.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_pagelabel.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_pagelabel.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_structelement.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_structelement.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_structtree.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_structtree.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_viewerpreferences.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpdf_viewerpreferences.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_floatrect.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_fontmap.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_fontmap.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_line.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_lineinfo.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_section.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_section.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_variabletext.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_variabletext.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_word.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_wordinfo.cpp"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_wordinfo.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_wordplace.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/cpvt_wordrange.h"
    "${PDFIUM_ROOT}/core/fpdfdoc/ipvt_fontmap.h"
)
add_library(pdfium::core_fpdfdoc ALIAS pdfium_core_fpdfdoc)
target_link_libraries(pdfium_core_fpdfdoc
    PRIVATE
        pdfium::strict_config
    PUBLIC
        pdfium::constants
        pdfium::core_fpdfapi_font
        pdfium::core_fpdfapi_page
        pdfium::core_fpdfapi_parser
        pdfium::core_fpdfapi_render
        pdfium::core_fxcrt
        pdfium::core_fxge
)
