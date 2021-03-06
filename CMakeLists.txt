cmake_minimum_required(VERSION 3.16)
project(EigenSample)

if (NOT CMAKE_BUILD_TYPE)
	#[[
		If the build is invoked without specifying CMAKE_BUILD_TYPE:

			cmake -B build_dir -S source_dir

		then CMAKE_BUILD_TYPE is still set in the CMake cache as an empty
		string by default.

		So we use FORCE here to overwrite it to a better default.
		(and Conan requires that it is NOT an empty string!)

		The default-when-unspecified value for CMAKE_BUILD_TYPE is "", a falsy
		value (https://developer.mozilla.org/en-US/docs/Glossary/Falsy),
		so we use NOT.
	]]
	set(default_build_type Release)
	message(WARNING "CMAKE_BUILD_TYPE is not set. Forcing to: ${default_build_type}")
	set(CMAKE_BUILD_TYPE ${default_build_type} CACHE STRING "Build type (Debug, Release, ...)" FORCE)
endif()

option(BUILD_SHARED_LIBS "Build a shared artifact (.dll, .so, .dylib)?" TRUE)
option(CMAKE_EXPORT_COMPILE_COMMANDS "Generate compile_commands.json?" TRUE)

# https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html#output-artifacts
set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")  # .lib, .a, ...
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/lib")  # .so, .dylib, ...
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${PROJECT_BINARY_DIR}/bin")  # .exe, .dll, ...

list(APPEND CMAKE_PREFIX_PATH "${CMAKE_CURRENT_LIST_DIR}/lib/cmake")

# When building the `install` target, put artifacts in this directory.
set(CMAKE_INSTALL_PREFIX "${PROJECT_BINARY_DIR}/package_stage")  # https://cmake.org/cmake/help/latest/variable/CMAKE_INSTALL_PREFIX.html

include(CPack)
include(CTest)

# Using Conan integration approach from: https://github.com/conan-io/cmake-conan
include(lib/third-party/conan.cmake)

conan_cmake_autodetect(conan_settings)  # https://github.com/conan-io/cmake-conan#conan_cmake_autodetect
conan_cmake_install(PATH_OR_REFERENCE "${CMAKE_CURRENT_LIST_DIR}/conanfile.txt"  # https://github.com/conan-io/cmake-conan#conan_cmake_install
	BUILD missing
	REMOTE conancenter
	SETTINGS ${conan_settings}
)

add_subdirectory(src)
add_subdirectory(test)
