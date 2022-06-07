find_package(AddGoogleExecutable CONFIG REQUIRED)
find_package(Eigen3 REQUIRED)

add_google_executable(link_gtest TEST
	SOURCES
		link_gtest.cxx
)

add_google_executable(link_benchmark TEST BENCHMARK
	SOURCES
		link_benchmark.cxx
)

add_google_executable(link_eigen TEST
	SOURCES
		link_eigen.cxx

	LIBRARIES
		Eigen3::Eigen
)

add_google_executable(link_shear TEST
	SOURCES
		link_shear.cxx

	LIBRARIES
		shear
)
