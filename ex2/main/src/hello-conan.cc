#include <ctime>
#include <string>
#include <iostream>
#include "hello-cmake.h"

void print_localtime() {
  std::time_t result = std::time(nullptr);
  std::cout << std::asctime(std::localtime(&result));
}

int main(int argc, char** argv) {
  std::string who = "cmake";
  std::cout << "Hello conan!!" << std::endl;
  std::cout << get_cmake(who) << std::endl;
  print_localtime();
  return 0;
}
