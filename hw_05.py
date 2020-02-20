"""
HW 05 - Static Code Analysis
Zephyr Zambrano

"""


import unittest


def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """
    if side_a <= 0 or side_b <= 0 or side_c <= 0: # side can't have length of 0 or negative length
        return "Not A Triangle"
    elif side_a == side_b and side_a == side_c and side_b == side_c:
        return "Equilateral"
    elif side_a * side_a + side_b * side_b == side_c * side_c:
        return "Right"
    elif side_a != side_b and side_a != side_c and side_b != side_c:
        return "Scalene"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        return "Isoceles"
    else:
        return "Not A Triangle"


def run_classify_triangle(side_a, side_b, side_c):
    """ Runs the classify_triangle() method and prints the result to the user. """
    answer = classify_triangle(side_a, side_b, side_c)
    print(f"A triangle with sides of length {side_a}, {side_b}, and {side_c} is: {answer}")


class TestTriangles(unittest.TestCase):
    """ Tests the triangle classifications. """

    def test_classify_triangle(self):
        """ Tests the classify_triangle() method. """
        # the four different types of triangles
        self.assertEqual(classify_triangle(3, 4, 5), "Right")
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral")
        self.assertEqual(classify_triangle(3, 3, 7), "Isoceles")
        self.assertEqual(classify_triangle(3, 4, 6), "Scalene")

        # Not A Triangle
        self.assertEqual(classify_triangle(4, 5, 0), "Not A Triangle") # side of length 0
        self.assertEqual(classify_triangle(4, 1, -3), "Not A Triangle") # side with negative length
        self.assertEqual(classify_triangle(0, 1, -3), "Not A Triangle") # 0 and negative side


if __name__ == "__main__":
    run_classify_triangle(1, 2, 3)
    run_classify_triangle(1, 1, 1)
    run_classify_triangle(3, 4, 5)
    run_classify_triangle(1, 1, 4)
    run_classify_triangle(0, 0, 0)

    unittest.main(exit=False)
