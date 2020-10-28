from conans import ConanFile, CMake, tools


class HelloConan(ConanFile):
    name = "HelloConan"
    version = "0.1"
    license = "MIT license"
    author = "kkimmy"
    description = "HelloConan package creation"
    topics = ("conan", "cmake")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": False}
    generators = ["cmake", "cmake_find_package"]
    exports_sources="main/*"

    # specify your dependency package here
    def requirements(self):
        self.requires("HelloCmake/0.1@myself/HelloCmake")

    # call your build system
    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="main")
        cmake.build()

    # specify what is to be packaged
    def package(self):
        self.copy("*.h", dst="include", src="main")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*", src="bin", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["HelloConan"]

