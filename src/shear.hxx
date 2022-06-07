#ifndef SHEAR_H
#define SHEAR_H

#include <Eigen/Dense>
#include <shear_export.h>

namespace my {

typedef Eigen::Vector2f point_t;

SHEAR_API void shear(point_t& point, float x_magnitude, float y_magnitude);

SHEAR_API void link_symbol();

}  // namespace my

#endif
