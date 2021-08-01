find_package(PkgConfig REQUIRED)

add_library(pdfium_thirdparty INTERFACE)
add_library(pdfium::thirdparty ALIAS pdfium_thirdparty)
target_link_libraries(pdfium_thirdparty
    INTERFACE
        pdfium::thirdparty_pdfium_base
        pdfium::thirdparty_skia_shared
        pdfium::thirdparty_freetype
)

if(PDF_ENABLE_XFA)
    add_library(pdfium_thirdparty_bigint OBJECT EXCLUDE_FROM_ALL
        "${PDFIUM_ROOT}/third_party/bigint/BigInteger.cc"
        "${PDFIUM_ROOT}/third_party/bigint/BigInteger.hh"
        "${PDFIUM_ROOT}/third_party/bigint/BigIntegerLibrary.hh"
        "${PDFIUM_ROOT}/third_party/bigint/BigIntegerUtils.cc"
        "${PDFIUM_ROOT}/third_party/bigint/BigIntegerUtils.hh"
        "${PDFIUM_ROOT}/third_party/bigint/BigUnsigned.cc"
        "${PDFIUM_ROOT}/third_party/bigint/BigUnsigned.hh"
        "${PDFIUM_ROOT}/third_party/bigint/BigUnsignedInABase.cc"
        "${PDFIUM_ROOT}/third_party/bigint/BigUnsignedInABase.hh"
        "${PDFIUM_ROOT}/third_party/bigint/NumberlikeArray.hh"
    )
    add_library(pdfium::thirdparty_bigint ALIAS pdfium_thirdparty_biging)
    target_link_libraries(pdfium_thirdparty_bigint
        PUBLIC
            pdfium::thirdparty_config
    )
endif()

if(NOT PDF_USE_SKIA AND NOT PDF_USE_SKIA_PATHS)
    # FIXME: use third party agg
    add_library(pdfium_thirdparty_fx_agg OBJECT EXCLUDE_FROM_ALL
        "${PDFIUM_ROOT}/third_party/agg23/agg_basics.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_clip_liang_barsky.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_conv_dash.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_conv_stroke.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_curves.cpp"
        "${PDFIUM_ROOT}/third_party/agg23/agg_curves.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_path_storage.cpp"
        "${PDFIUM_ROOT}/third_party/agg23/agg_path_storage.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_rasterizer_scanline_aa.cpp"
        "${PDFIUM_ROOT}/third_party/agg23/agg_rasterizer_scanline_aa.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_renderer_scanline.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_rendering_buffer.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_scanline_u.h"
        "${PDFIUM_ROOT}/third_party/agg23/agg_vcgen_dash.cpp"
        "${PDFIUM_ROOT}/third_party/agg23/agg_vcgen_stroke.cpp"
    )
    add_library(pdfium::thirdparty_fx_agg ALIAS pdfium_thirdparty_fx_agg)
    target_link_libraries(pdfium_thirdparty_fx_agg
        PRIVATE
            pdfium::thirdparty_config
        PUBLIC
            pdfium::core_fxcrt
    )
endif()

# Don't add REQUIRED to external dependncies such that it is possible to have the minimum number of requirements.
# Use CMake targets everywhere (targets containing `::`) such that cmake will complain about missing targets.

add_library(pdfium_thirdparty_freetype INTERFACE)
add_library(pdfium::thirdparty_freetype ALIAS pdfium_thirdparty_freetype)
find_package(Freetype)
target_link_libraries(pdfium_thirdparty_freetype
    INTERFACE
        Freetype::Freetype
)

add_library(pdfium_thirdparty_config INTERFACE)
add_library(pdfium::thirdparty_config ALIAS pdfium_thirdparty_config)
target_link_libraries(pdfium_thirdparty_config
    INTERFACE
        pdfium::common_config
        pdfium::public_config
)

add_library(pdfium_thirdparty_libjpeg INTERFACE)
add_library(pdfium::thirdparty_libjpeg ALIAS pdfium_thirdparty_libjpeg)
option(PDF_LIBJPEG_TURBO "Use libjpeg-turbo" OFF)
if(PDF_LIBJPEG_TURBO)
    find_package(libjpeg-turbo)
    target_link_libraries(pdfium_thirdparty_libjpeg INTERFACE libjpeg-turbo::libjpeg-turbo)
    target_compile_definitions(pdfium_thirdparty_libjpeg INTERFACE USE_LIBJPEG_TURBO=1)
else()
    find_package(JPEG)
    target_link_libraries(pdfium_thirdparty_libjpeg INTERFACE JPEG::JPEG)
    target_compile_definitions(pdfium_thirdparty_libjpeg INTERFACE USE_SYSTEM_LIBJPEG)
endif()

add_library(pdfium_thirdparty_zlib INTERFACE)
add_library(pdfium::thirdparty_zlib ALIAS pdfium_thirdparty_zlib)
find_package(ZLIB)
target_link_libraries(pdfium_thirdparty_zlib INTERFACE ZLIB::ZLIB)
target_compile_definitions(pdfium_thirdparty_zlib INTERFACE USE_SYSTEM_ZLIB)

add_library(pdfium_thirdparty_lcms2 INTERFACE)
add_library(pdfium::thirdparty_lcms2 ALIAS pdfium_thirdparty_lcms2)
pkg_check_modules(LCMS2 IMPORTED_TARGET lcms2)
target_link_libraries(pdfium_thirdparty_lcms2 INTERFACE PkgConfig::LCMS2)
target_compile_definitions(pdfium_thirdparty_lcms2 INTERFACE USE_SYSTEM_LCMS2)

add_library(pdfium_thirdparty_libopenjpeg2 INTERFACE)
add_library(pdfium::thirdparty_libopenjpeg2 ALIAS pdfium_thirdparty_libopenjpeg2)
pkg_check_modules(LIBOPENJP2 IMPORTED_TARGET libopenjp2)
# FIXME: use find_package(OpenJPEG) + openjp2 target, needs https://github.com/uclouvain/openjpeg/pull/1370
target_link_libraries(pdfium_thirdparty_libopenjpeg2 INTERFACE PkgConfig::LIBOPENJP2)
target_compile_definitions(pdfium_thirdparty_libopenjpeg2 INTERFACE USE_SYSTEM_LIBOPENJPEG2)

add_library(pdfium_thirdparty_libpng INTERFACE)
add_library(pdfium::thirdparty_libpng ALIAS pdfium_thirdparty_libpng)
find_package(PNG)
target_link_libraries(pdfium_thirdparty_libpng INTERFACE PNG::PNG)
target_compile_definitions(pdfium_thirdparty_libpng INTERFACE USE_SYSTEM_LIBPNG)

if(PDF_ENABLE_XFA_TIFF)
    add_library(pdfium_thirdparty_tiff INTERFACE)
    add_library(pdfium::thirdparty_tiff ALIAS thirdparty_tiff)
    find_package(TIFF)
    target_link_libraries(pdfium_thirdparty_tiff INTERFACE TIFF::TIFF)
    target_compile_definitions(pdfium_thirdparty_tiff PUBLIC USE_SYSTEM_LIBTIFF)
endif()

add_library(pdfium_thirdparty_pdfium_base OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/address_space_randomization.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/address_space_randomization.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/oom.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/oom_callback.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/oom_callback.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator_constants.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator_internal.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_alloc.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_alloc.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_alloc_check.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_alloc_constants.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_bucket.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_bucket.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_cookie.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_direct_map_extent.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_freelist_entry.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_oom.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_oom.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_page.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_page.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_root_base.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/partition_root_base.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/random.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/random.h"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/spin_lock.cc"
    "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/spin_lock.h"
    "${PDFIUM_ROOT}/third_party/base/base_export.h"
    "${PDFIUM_ROOT}/third_party/base/bits.h"
    "${PDFIUM_ROOT}/third_party/base/check.h"
    "${PDFIUM_ROOT}/third_party/base/check_op.h"
    "${PDFIUM_ROOT}/third_party/base/compiler_specific.h"
    "${PDFIUM_ROOT}/third_party/base/containers/adapters.h"
    "${PDFIUM_ROOT}/third_party/base/containers/contains.h"
    "${PDFIUM_ROOT}/third_party/base/cxx17_backports.h"
    "${PDFIUM_ROOT}/third_party/base/debug/alias.cc"
    "${PDFIUM_ROOT}/third_party/base/debug/alias.h"
    "${PDFIUM_ROOT}/third_party/base/immediate_crash.h"
    "${PDFIUM_ROOT}/third_party/base/memory/aligned_memory.cc"
    "${PDFIUM_ROOT}/third_party/base/memory/aligned_memory.h"
    "${PDFIUM_ROOT}/third_party/base/no_destructor.h"
    "${PDFIUM_ROOT}/third_party/base/notreached.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/checked_math.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/checked_math_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/clamped_math.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/clamped_math_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_conversions.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_conversions_arm_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_conversions_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_math.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_math_arm_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_math_clang_gcc_impl.h"
    "${PDFIUM_ROOT}/third_party/base/numerics/safe_math_shared_impl.h"
    "${PDFIUM_ROOT}/third_party/base/optional.h"
    "${PDFIUM_ROOT}/third_party/base/span.h"
    "${PDFIUM_ROOT}/third_party/base/sys_byteorder.h"
    "${PDFIUM_ROOT}/third_party/base/template_util.h"
)
add_library(pdfium::thirdparty_pdfium_base ALIAS pdfium_thirdparty_pdfium_base)
if(WIN32)
    target_sources(pdfium_thirdparty_pdfium_base PRIVATE
        "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator_internals_win.h"
        "${PDFIUM_ROOT}/third_party/base/win/win_util.cc"
        "${PDFIUM_ROOT}/third_party/base/win/win_util.h"
    )
endif()
if(POSIX)
    target_sources(pdfium_thirdparty_pdfium_base PRIVATE
        "${PDFIUM_ROOT}/third_party/base/allocator/partition_allocator/page_allocator_internals_posix.h"
    )
endif()
target_link_libraries(pdfium_thirdparty_pdfium_base
    PRIVATE
        pdfium::thirdparty_config
)

add_library(pdfium_thirdparty_skia_shared OBJECT EXCLUDE_FROM_ALL
    "${PDFIUM_ROOT}/third_party/skia_shared/SkFloatToDecimal.cpp"
    "${PDFIUM_ROOT}/third_party/skia_shared/SkFloatToDecimal.h"
)
add_library(pdfium::thirdparty_skia_shared ALIAS pdfium_thirdparty_skia_shared)
target_link_libraries(pdfium_thirdparty_skia_shared
    PRIVATE
        pdfium::strict_config
)
