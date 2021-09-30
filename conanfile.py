from conans import CMake, ConanFile, tools
from conans.errors import ConanInvalidConfiguration
import os
import shutil
import textwrap

required_conan_version = ">=1.33.0"


class PdfiumConan(ConanFile):
    name = "pdfium"
    description = "PDF generation and rendering library."
    license = "BSD-3-Clause"
    topics = ("conan", "pdfium", "generate", "generation", "rendering", "pdf", "document", "print")
    homepage = "https://opensource.google/projects/pdfium"
    url = "https://github.com/conan-io/conan-center-index"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_libjpeg": ["libjpeg", "libjpeg-turbo"],
    }
    default_options = {
        "shared": False,
        "fPIC": True,
        "with_libjpeg": "libjpeg",
    }

    generators = "cmake", "cmake_find_package", "pkg_config"
    no_copy_source = True

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC

    def requirements(self):
        self.requires("abseil/20210324.2")
        self.requires("freetype/2.10.4")
        self.requires("icu/69.1")
        self.requires("lcms/2.11")
        self.requires("openjpeg/2.4.0")
        if self.options.with_libjpeg == "libjpeg":
            self.requires("libjpeg/9d")
        elif self.options.with_libjpeg == "libjpeg-turbo":
            self.requires("libjpeg-turbo/2.1.0")

    def build_requirements(self):
        self.build_requires("pkgconf/1.7.4")

    def validate(self):
        if self.settings.compiler.cppstd:
            tools.check_min_cppstd(self, 17)
        minimum_compiler_versions = {
            "gcc": 8,
            "Visual Studio": 15,
        }
        min_compiler_version = minimum_compiler_versions.get(str(self.settings.compiler))
        if min_compiler_version:
            if tools.Version(self.settings.compiler.version) < min_compiler_version:
                raise ConanInvalidConfiguration("pdfium needs at least compiler version {}".format(min_compiler_version))

    def export_sources(self):
        shutil.copytree("pdfium", os.path.join(self.export_sources_folder, "pdfium"))
        shutil.copytree("cmake", os.path.join(self.export_sources_folder, "cmake"))

    def build(self):
        tools.save("CMakeLists.txt", textwrap.dedent("""\
            cmake_minimum_required(VERSION 3.0)
            project(cmake_wrapper)

            include(conanbuildinfo.cmake)
            conan_basic_setup(TARGETS)

            add_subdirectory({cmake_folder} pdfium_cmake)
        """).format(
            cmake_folder=os.path.join(self.source_folder, "cmake").replace("\\", "/"),
        ))

        cmake = CMake(self)
        cmake.verbose = True
        cmake.definitions["PDFIUM_ROOT"] = os.path.join(self.source_folder, "pdfium").replace("\\", "/")
        cmake.definitions["USE_LIBJPEG_TURBO"] = self.options.with_libjpeg == "libjpeg-turbo"
        cmake.configure(source_folder=self.build_folder)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["pdfium"]
        if tools.is_apple_os(self.settings.os):
            self.cpp_info.frameworks.extend(["Appkit", "CoreFoundation", "CoreGraphics"])

        stdcpp_library = tools.stdcpp_library(self)
        if stdcpp_library:
            self.cpp_info.system_libs.append(stdcpp_library)
