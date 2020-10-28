cmake_minimum_required(VERSION 3.18.2)
project(helloconan)
add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_library(hellocmake src/hello-cmake.cc)

