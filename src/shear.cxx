#include "shear.hxx"

void my::shear(my::point_t& point, float x_magnitude, float y_magnitude)
{
	static Eigen::Matrix2f shear {{1, 0}, {0, 1}};

	shear(0, 1) = x_magnitude;
	shear(1, 0) = y_magnitude;

	point = shear * point;
}

void my::link_symbol()
{}
