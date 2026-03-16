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
        length = math.sqrt(((self.end.x-self.start.x)**2)+((self.end.y-self.start.y)**2))
        return length
            
    def compute_slope(self) -> float:
        dy = self.end.y - self.start.y
        dx = self.end.x - self.start.x
        radians = math.atan2(dy, dx)
        angle = math.degrees(radians)
        return angle
    
    def compute_horizontal_cross(self) -> bool:
        if (self.end.y*self.start.y) <= 0:
            return True
        else:
            return False
    
    def compute_vertical_cross(self) -> bool:
        if (self.end.x*self.start.x) <= 0:
            return True
        else:
            return False
