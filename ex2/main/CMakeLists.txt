cmake_minimum_required(VERSION 3.18.2)
project(helloconan)
add_definitions("-std=c++11")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

find_package(HelloCmake 0.1 REQUIRED)

add_executable(helloconan src/hello-conan.cc)
target_link_libraries(helloconan hellocmake)
