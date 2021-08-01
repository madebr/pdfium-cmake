add_library(pdfium_core_fdrm OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/core/fdrm/fx_crypt.cpp"
    "${PDFIUM_ROOT}/core/fdrm/fx_crypt.h"
    "${PDFIUM_ROOT}/core/fdrm/fx_crypt_aes.cpp"
    "${PDFIUM_ROOT}/core/fdrm/fx_crypt_sha.cpp"
)
add_library(pdfium::core_fdrm ALIAS pdfium_core_fdrm)
target_link_libraries(pdfium_core_fdrm
    PRIVATE
        pdfium::strict_config
    PUBLIC
        pdfium::core_fxcrt
)
