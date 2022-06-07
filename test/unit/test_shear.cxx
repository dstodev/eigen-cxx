#include <gtest/gtest.h>

#include <shear.hxx>

TEST(Shear, zero_magnitudes)
{
	my::point_t const expected {1.0f, 2.0f};
	my::point_t point = expected;

	my::shear(point, 0, 0);

	ASSERT_EQ(expected, point);
}

TEST(Shear, x_magnitude_2)
{
	// x' = x + shear[x] * y
	//    = 1 + 2        * 2
	//    = 5
	my::point_t const expected {5.0f, 2.0f};
	my::point_t point {1.0f, expected[1]};

	my::shear(point, 2, 0);

	ASSERT_EQ(expected, point);
}

TEST(Shear, y_magnitude_2)
{
	// y' = y + shear[y] * x
	//    = 2 + 2        * 1
	//    = 4
	my::point_t const expected {1.0f, 4.0f};
	my::point_t point {expected[0], 2.0f};

	my::shear(point, 0, 2);

	ASSERT_EQ(expected, point);
}

TEST(Shear, both_magnitudes_2)
{
	// x' = 5
	// y' = 4
	my::point_t const expected {5.0f, 4.0f};
	my::point_t point {1.0f, 2.0f};

	my::shear(point, 2, 2);

	ASSERT_EQ(expected, point);
}
