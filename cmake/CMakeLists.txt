cmake_minimum_required(VERSION 3.15)
project(pdfium)

set(PDFIUM_ROOT "${CMAKE_CURRENT_SOURCE_DIR}/../pdfium" CACHE PATH "Location of pdfium source tree")

include(CMakeDependentOption)
include(GNUInstallDirs)

if(NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_SYSTEM_NAME MATCHES "Linux")
    set(LINUX ON)
endif()
if(ANDROID OR APPLE OR CHROMEOS OR LINUX)
    set(POSIX ON)
endif()

option(BUILD_SHARED_LIBS "Build shared libs" OFF)

option(PDF_ENABLE_CLICK_LOGGING "Generate logging messages for click events that reach PDFium" OFF)

option(PDF_ENABLE_V8 "Build PDFium either with or without v8 support." OFF)
option(PDF_ENABLE_XFA "Build PDFium either with or without XFA Forms support." OFF)
cmake_dependent_option(PDF_ENABLE_XFA_BMP "If XFA, also support bmp codec." ON PDF_ENABLE_XFA OFF)
cmake_dependent_option(PDF_ENABLE_XFA_GIF "If XFA, also support gif codec." ON PDF_ENABLE_XFA OFF)
cmake_dependent_option(PDF_ENABLE_XFA_PNG "If XFA, also support png codec." ON PDF_ENABLE_XFA OFF)
cmake_dependent_option(PDF_ENABLE_XFA_TIFF "If XFA, also support tiff codec." ON PDF_ENABLE_XFA OFF)

option(PDF_USE_SKIA "Build PDFium against Skia (experimental) rather than AGG. Use Skia to draw everything." OFF)
option(PDF_USE_SKIA_PATHS "Build PDFium against Skia (experimental) rather than AGG. Use Skia to draw paths." OFF)
cmake_dependent_option(PDF_USE_GDI "Build PDFium with or without experimental win32 GDI APIs." ON WIN32 OFF)

option(PDF_IS_STANDALINE "Build PDFium standalone." OFF)
option(PDF_IS_COMPLETE_LIB "Build a complete static library." OFF)

include("${CMAKE_CURRENT_LIST_DIR}/patch_sources.cmake")

if(BUILD_SHARED_LIBS)
    set(CMAKE_POSITION_INDEPENDENT_CODE ON)
endif()
add_definitions(-DFPDF_IMPLEMENTATION -DCOMPONENT_BUILD)

set(CMAKE_C_VISIBILITY_PRESET hidden)
set(CMAKE_CXX_VISIBILITY_PRESET hidden)

if(WIN32)
    add_definitions(
        -DUNICODE -D_UNICODE
        -DWIN32_LEAN_AND_MEAN
        -DNOMINMAX
    )
endif()
if(MSVC)
    add_compile_options(
        /wd4324
        /wd4577
    )
endif()

set(pdfium_public_headers_impl
    "${PDFIUM_ROOT}/public/cpp/fpdf_deleters.h"
    "${PDFIUM_ROOT}/public/cpp/fpdf_scopers.h"
    "${PDFIUM_ROOT}/public/fpdf_annot.h"
    "${PDFIUM_ROOT}/public/fpdf_attachment.h"
    "${PDFIUM_ROOT}/public/fpdf_catalog.h"
    "${PDFIUM_ROOT}/public/fpdf_dataavail.h"
    "${PDFIUM_ROOT}/public/fpdf_doc.h"
    "${PDFIUM_ROOT}/public/fpdf_edit.h"
    "${PDFIUM_ROOT}/public/fpdf_ext.h"
    "${PDFIUM_ROOT}/public/fpdf_flatten.h"
    "${PDFIUM_ROOT}/public/fpdf_formfill.h"
    "${PDFIUM_ROOT}/public/fpdf_fwlevent.h"
    "${PDFIUM_ROOT}/public/fpdf_javascript.h"
    "${PDFIUM_ROOT}/public/fpdf_ppo.h"
    "${PDFIUM_ROOT}/public/fpdf_progressive.h"
    "${PDFIUM_ROOT}/public/fpdf_save.h"
    "${PDFIUM_ROOT}/public/fpdf_searchex.h"
    "${PDFIUM_ROOT}/public/fpdf_signature.h"
    "${PDFIUM_ROOT}/public/fpdf_structtree.h"
    "${PDFIUM_ROOT}/public/fpdf_sysfontinfo.h"
    "${PDFIUM_ROOT}/public/fpdf_text.h"
    "${PDFIUM_ROOT}/public/fpdf_transformpage.h"
    "${PDFIUM_ROOT}/public/fpdfview.h"
)

add_library(pdfium_public_headers INTERFACE)
add_library(pdfium::public_headers ALIAS pdfium_public_headers)
target_link_libraries(pdfium_public_headers INTERFACE
    pdfium::public_config
    pdfium::implementation_config
)

add_library(pdfium_implementation_config INTERFACE)
add_library(pdfium::implementation_config ALIAS pdfium_implementation_config)
target_compile_definitions(pdfium_implementation_config INTERFACE
    FPDF_IMPLEMENTATION
)

add_library(pdfium_public_config INTERFACE)
add_library(pdfium::public_config ALIAS pdfium_public_config)
target_compile_definitions(pdfium_public_config INTERFACE
    $<$<BOOL:${PDF_ENABLE_V8}>:
        PDF_ENABLE_V8
        $<$<BOOL:${PDF_ENABLE_XFA}>:
            PDF_ENABLE_XFA
            $<$<BOOL:${PDF_ENABLE_XFA_BMP}>:PDF_ENABLE_XFA_BMP>
            $<$<BOOL:${PDF_ENABLE_XFA_GIF}>:PDF_ENABLE_XFA_GIF>
            $<$<BOOL:${PDF_ENABLE_XFA_PNG}>:PDF_ENABLE_XFA_PNG>
            $<$<BOOL:${PDF_ENABLE_XFA_TIFF}>:PDF_ENABLE_XFA_TIFF>
        >
    >
    $<$<BOOL:${PDF_USE_WIN32_GDI}>:PDFIUM_PRINT_TEXT_WITH_GDI>
)

add_library(pdfium_common_config INTERFACE)
add_library(pdfium::common_config ALIAS pdfium_common_config)
target_include_directories(pdfium_common_config INTERFACE
    "${PDFIUM_ROOT}"
)
target_compile_definitions(pdfium_common_config INTERFACE
    PNG_PREFIX
    PNG_USE_READ_MACROS
    $<$<BOOL:${PDF_ENABLE_CLICK_LOGGING}>:PDF_ENABLE_CLICK_LOGGING>
    $<$<BOOL:${PDF_USE_SKIA}>:_SKIA_SUPPORT_>
    $<$<BOOL:${PDF_USE_SKIA_PATHS}>:_SKIA_SUPPORT_PATHS_>
)
target_compile_options(pdfium_common_config INTERFACE
    $<$<BOOL:${MSVC}>:/utf-8
        /wd4324
        /wd4577
    >
    #$<$<CXX_COMPILER_ID:Clang>:
    #    -Wc++-narrowing
    #    -Wdeprecated-copy
    #
    #>
)

add_library(pdfium_core_config INTERFACE)
add_library(pdfium::core_config ALIAS pdfium_core_config)
target_link_libraries(pdfium_core_config INTERFACE
    pdfium::common_config
    pdfium::public_config
    # noshadowing
    # no_size_t_to_int_warning
)
target_compile_options(pdfium_core_config INTERFACE
    $<$<BOOL:${MSVC}>:
        /wd4324
        /wd4577
    >
)

add_library(pdfium_strict_config INTERFACE)
add_library(pdfium::strict_config ALIAS pdfium_strict_config)
target_link_libraries(pdfium_strict_config INTERFACE
    pdfium::core_config
    # wexit_time_destructors
    # wglobal_constructors
)
file(WRITE null.cpp "")
add_library(pdfium
    null.cpp
)
add_library(pdfium::pdfium ALIAS pdfium)
target_include_directories(pdfium
    INTERFACE
        "$<BUILD_INTERFACE:${PDFIUM_ROOT}/public>"
        "$<INSTALL_INTERFACE:${CMAKE_INSTALL_INCLUDEDIR}>"
)
target_link_libraries(pdfium
    PRIVATE
        pdfium::strict_config
    PRIVATE
        pdfium::public_config
    PRIVATE
        pdfium::constants
        pdfium::core_fpdfapi_page
        pdfium::core_fpdfapi_parser
        pdfium::core_fpdfdoc
        pdfium::core_fxcodec
        pdfium::core_fxge
        pdfium::fpdfsdk
        pdfium::fpdfsdk_formfiller
        pdfium::fxjs
        pdfium::thirdparty_pdfium_base
        pdfium::thirdparty_skia_shared
    PRIVATE
        pdfium::core_fxcrt
    PRIVATE
        pdfium::common_config
    PRIVATE
        # FIXME: https://gitlab.kitware.com/cmake/cmake/-/issues/18090
        pdfium::fpdfsdk_pwl
        pdfium::core_fdrm
        pdfium::core_fpdfapi_cmaps
        pdfium::core_fpdfapi_edit
        pdfium::core_fpdfapi_font
        pdfium::core_fpdfapi_render
        pdfium::core_fpdftext
        pdfium::thirdparty_fx_agg
)
if(PDF_ENABLE_XFA)
    target_link_libraries(pdfium
        PRIVATE
            pdfium::fpdfsdk_fpdfxfa
            pdfium::xfa_xfa
            pdfium::xfa_parser
    )
endif()
if(WIN32)
    target_link_libraries(pdfium
        PRIVATE
            advapi32
            gdi32
            user32
    )
endif()
if(APPLE)
    target_link_libraries(pdfium
        PRIVATE
            -framework AppKit
            -framework CoreFoundation
    )
endif()
set_target_properties(pdfium PROPERTIES
    EXPORT_NAME "Pdfium"
    PUBLIC_HEADER "${pdfium_public_headers_impl}"
)

add_subdirectory(constants)
add_subdirectory(core)
add_subdirectory(fpdfsdk)
add_subdirectory(fxjs)
add_subdirectory(third_party)

install(TARGETS pdfium EXPORT pdfiumTargets
    PUBLIC_HEADER DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}"
    ARCHIVE DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}"
    RUNTIME DESTINATION "${CMAKE_INSTALL_BINDIR}"
)

