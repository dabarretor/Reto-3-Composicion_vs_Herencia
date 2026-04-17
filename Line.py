import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end
        self.length = self.compute_length()
        self.slope = self.compute_slope()

    def compute_length(self) -> float:
        length = math.sqrt(
            ((self.end.x - self.start.x) ** 2) + ((self.end.y - self.start.y) ** 2)
        )
        return length

    def compute_slope(self) -> float:
        dy = self.end.y - self.start.y
        dx = self.end.x - self.start.x
        radians = math.atan2(dy, dx)
        angle = math.degrees(radians)
        return angle

    def compute_horizontal_cross(self) -> bool:
        if (self.end.y * self.start.y) <= 0:
            return True
        else:
            return False

    def compute_vertical_cross(self) -> bool:
        if (self.end.x * self.start.x) <= 0:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, **kwargs):
        # The rectangle can be created using different combinations of parameters using the **kwargs syntax.
        # In case 1, the rectangle is created using the width, height, and bottom left corner.
        if "width" in kwargs and "height" in kwargs and "bottom_left_corner" in kwargs:
            self.width = kwargs["width"]
            self.height = kwargs["height"]
            bottom_left_corner = kwargs["bottom_left_corner"]

            center_x = bottom_left_corner.x + (
                self.width / 2
            )  # The center is sought at x.
            center_y = bottom_left_corner.y + (
                self.height / 2
            )  # The center is sought in y.

            self.center_point = Point(center_x, center_y)

        # In case 2, the rectangle is created using the width, height, and center point.
        elif "width" in kwargs and "height" in kwargs and "center_point" in kwargs:
            self.width = kwargs["width"]
            self.height = kwargs["height"]
            self.center_point = kwargs["center_point"]

        # In case 3, the rectangle is created using two opposite corners.
        elif "point1" in kwargs and "point2" in kwargs:
            self.point1 = kwargs["point1"]
            self.point2 = kwargs["point2"]
            width = abs(self.point2.x - self.point1.x)
            height = abs(self.point2.y - self.point1.y)
            center_x = (self.point1.x + self.point2.x) / 2
            center_y = (self.point1.y + self.point2.y) / 2

            self.width = width
            self.height = height
            self.center_point = Point(center_x, center_y)
        # In case 4, the rectangle is created using the four lines that form it.
        elif (
            "bottom_line" in kwargs
            and "top_line" in kwargs
            and "left_line" in kwargs
            and "right_line" in kwargs
        ):
            self.bottom_line = kwargs["bottom_line"]
            self.left_line = kwargs["left_line"]
            width = self.bottom_line.compute_length()
            height = self.left_line.compute_length()

            # We calculate the center point of the rectangle using the midpoint formula
            center_x = (self.bottom_line.start.x + self.bottom_line.end.x) / 2
            center_y = (self.left_line.start.y + self.left_line.end.y) / 2

            # The original __init__ is reused to create the rectangle
            self.width = width
            self.height = height
            self.center_point = Point(center_x, center_y)
        # Allows the rectangle to be created from its four boundary lines
        min_x = self.center_point.x - (self.width / 2) #
        max_x = self.center_point.x + (self.width / 2) #
        min_y = self.center_point.y - (self.height / 2) #
        max_y = self.center_point.y + (self.height / 2) #

        p_bottom_left = Point(min_x, min_y)
        p_bottom_right = Point(max_x, min_y)
        p_top_left = Point(min_x, max_y)
        p_top_right = Point(max_x, max_y)

        self.bottom_line = Line(p_bottom_left, p_bottom_right)
        self.top_line = Line(p_top_left, p_top_right)
        self.left_line = Line(p_bottom_left, p_top_left)
        self.right_line = Line(p_bottom_right, p_top_right)
        # The lines that form the rectangle are stored in a list for easy access and manipulation.
        self.lines = [self.bottom_line, self.top_line, self.left_line, self.right_line]

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width) + 2 * (self.height)

    def compute_interference_point(self, point: Point):
        """This fuction determinate if a point is inside the rectangle or not.
        For this, the maximum and minimum values of x and y
        that a point can have to be inside the rectangle are calculated.
        """
        Min_x = self.center_point.x - (
            self.width / 2
        )  # Represents the entire left edge.
        Max_x = self.center_point.x + (
            self.width / 2
        )  # Represents the entire right edge.
        Min_y = self.center_point.y - (
            self.height / 2
        )  # Represents the entire bottom edge.
        Max_y = self.center_point.y + (
            self.height / 2
        )  # Represents the entire top edge.

        """ If the given point has coordinates x and y that are within 
        the calculated maximum and minimum values, then the point is inside
        the rectangle and the function returns True. 
        Otherwise, it returns False.
        """

        if Max_x >= point.x >= Min_x and Max_y >= point.y >= Min_y:
            return True
        else:
            return False

    def compute_interference_line(self, line: Line):
        """Use the compute_interference_point function to determine
        if at least one point is inside the rectangle.
        If so, the line segment interferes with the rectangle,
        and the function returns True. Otherwise, it returns False."""

        is_start_inside = self.compute_interference_point(line.start)
        is_end_inside = self.compute_interference_point(line.end)
        if is_start_inside or is_end_inside:
            return True
        else:
            return False

if __name__ == "__main__":
    # of the line 138 to 132 is of the class Rectangle,
    # using two points as opposite corners (method_3).
    rectangle = Rectangle(point1=Point(0.5, -3.54), point2=Point(4.5, 0.46))
    area = rectangle.compute_area()
    perimeter = rectangle.compute_perimeter()
    interference = rectangle.compute_interference_point(Point(2, -1))
    interference_line = rectangle.compute_interference_line(
        Line(Point(0, 0), Point(5, 0))
    )

    print("RECTANGLE DATA:")
    print(
        f"Width: {rectangle.width} and Height: \
          {rectangle.height}"
    )  # Output: Width: 4.0 and Height: 4.0
    print(
        f"Center Point: ({rectangle.center_point.x},\
          {rectangle.center_point.y})"
    )  # Output: Center Point: (2.5, -1.54)
    print(f"Area: {area}")  # Output: Area: 16.0
    print(f"Perimeter: {perimeter}")  # Output: Perimeter: 16.0
    print(f"Interference: {interference}")  # Output: Interference: True
    print(f"Interference Line: {interference_line}")  # Output: Interference Line: False

    print("---  test of point 2: New method with four lines (method_4) ---")
    p1 = Point(0, 0)
    p2 = Point(4, 0)
    p3 = Point(0, 3)
    p4 = Point(4, 3)

    # A new rectangle is created using 4 lines
    rect_from_lines = Rectangle(
        bottom_line=Line(p1, p2),
        top_line=Line(p3, p4),
        left_line=Line(p1, p3),
        right_line=Line(p2, p4),
    )
    print(f"Area: {rect_from_lines.compute_area()}")  # Output: Area: 12.0
    print(
        f"Perimeter: {rect_from_lines.compute_perimeter()}"
    )  # Output: Perimeter: 14.0
    print(f"\n{'-' * 30}")

    # of the line 134 to 143 is of the class Line
    line = Line(Point(1, 2), Point(4, 6))
    length = line.compute_length()
    slope = line.compute_slope()
    horizontal_cross = line.compute_horizontal_cross()
    vertical_cross = line.compute_vertical_cross()

    print("\nLINES DATA: ")
    print(f"length: {line.compute_length()}")  # Output: length: 5.0
    print(f"slope: {line.compute_slope()}")  # Output: slope: 53.13
    # Output: horizontal cross: False
    print(f"horizontal cross: {line.compute_horizontal_cross()}")
    # Output: vertical cross: False
    print(f"vertical cross: {line.compute_vertical_cross()}")
