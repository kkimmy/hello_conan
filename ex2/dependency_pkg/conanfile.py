from conans import ConanFile, CMake, tools


class HelloCmake(ConanFile):
    name = "HelloCmake"
    version = "0.1"
    license = "MIT license"
    author = "kkimmy"
    description = "HelloCmake package creation"
    topics = ("conan", "cmake")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = ["cmake", "cmake_find_package"]
    exports_sources="src/*"

    # call your build system
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    # specify what is to be packaged
    def package(self):
        self.copy("*.h", dst="include", src="src")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*", src="bin", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HelloCmake"]

