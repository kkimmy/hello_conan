#include "hello-cmake.h"
#include <string>

std::string get_cmake(const std::string& who) {
  return "Hello " + who;
}
