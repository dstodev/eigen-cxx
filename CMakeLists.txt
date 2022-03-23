cmake_minimum_required(VERSION 3.14)
project(EigenSample)

option(BUILD_SHARED_LIBS "Build shared libraries." OFF)

set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)

# For more information: https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#output-artifacts
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")  # e.g. .a, .lib
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")  # e.g. .so, .dylib
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")  # e.g. .exe, .dll

# Using approach from:
# https://docs.conan.io/en/latest/integrations/build_system/cmake/cmake_find_package_generator.html#in-a-conanfile-txt
include(${PROJECT_BINARY_DIR}/conan_paths.cmake)

list(APPEND CMAKE_PREFIX_PATH "${CMAKE_CURRENT_LIST_DIR}/lib/cmake")

include(CPack)
include(CTest)

add_subdirectory(src)
add_subdirectory(test)
