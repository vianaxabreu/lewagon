"""Dummy challenge for Kitt Demo"""

# $DELETE_BEGIN
import math
# $DELETE_END

def circle_area(radius):
    """Returns the area of the circle of given radius"""
    # $CHALLENGIFY_BEGIN
    if radius > 0:
        return radius * radius * math.pi
    return 0
    # $CHALLENGIFY_END
