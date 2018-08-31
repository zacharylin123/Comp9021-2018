# Defines two classes, Point() and Triangle().
# An object for the second class is created by passing named arguments,
# point_1, point_2 and point_3, to its constructor.
# Such an object can be modified by changing one point, two or three points
# thanks to the method change_point_or_points().
# At any stage, the object maintains correct values
# for perimeter and area.
#
# Written by *** and Eric Martin for COMP9021


from math import sqrt


class PointError(Exception):
    def __init__(self, message):
        self.message = message


class Point():
    def __init__(self, x = None, y = None):
        if x is None and y is None:
            self.x = 0
            self.y = 0
        elif x is None or y is None:
            raise PointError('Need two coordinates, point not created.')
        else:
            self.x = x
            self.y = y
            
    # Possibly define other methods


class TriangleError(Exception):
    def __init__(self, message):
        self.message = message



class TriangleError(Exception):
    def __init__(self, message):
        self.message = message


class Triangle:
    def __init__(self, *, point_1, point_2, point_3):
##        self.L1 = sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)
##        self.L2 = sqrt((point_3.x - point_2.x) ** 2 + (point_3.y - point_2.y) ** 2)
##        self.L3 = sqrt((point_3.x - point_1.x) ** 2 + (point_3.y - point_1.y) ** 2)
##        if self.L1 + self.L2 <= self.L3 or self.L3 + self.L2 <= self.L1 or self.L1 + self.L3 <= self.L2:
##            raise TriangleError('Incorrect input, triangle not created.')
        self.point_1 = point_1
        self.point_2 = point_2
        self.point_3 = point_3
        self.area = self._compute_area()
        self.perimeter = self._compute_perimeter()
        self.create_or_not()
    def create_or_not(self):
        L1 = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
        L2 = sqrt((self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        L3 = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
        if L1 + L2 <= L3 or L3 + L2 <= L1 or L1 + L3 <= L2:
            raise TriangleError('Incorrect input, triangle not created.')

    def _compute_area(self):
        L1 = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
        L2 = sqrt((self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        L3 = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
        self.area = sqrt((L1 + L2 + L3) * (-L1 + L2 + L3) * (L1 - L2 + L3) * (L1 + L2 - L3) / 16) 
        return self.area
    def _compute_perimeter(self):
        L1 = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
        L2 = sqrt((self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        L3 = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
        self.perimeter = L1 + L2 + L3
        return self.perimeter
    def change_point_or_points(self, *, point_1 = None, point_2 = None, point_3 = None):
        if point_1 is not None:
            if point_1 == self.point_1:
                print('Incorrect input, triangle not modified.')
            else:
                self.point_1 = point_1
        if point_2 is not None:
            if point_2 == self.point_2:
                print('Incorrect input, triangle not modified.')
            else:
                self.point_2 = point_2
        if point_3 is not None:
            if point_3 == self.point_3:
                print('Incorrect input, triangle not modified.')
            else:
                self.point_3 = point_3
        L1 = sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2)
        L2 = sqrt((self.point_3.x - self.point_2.x) ** 2 + (self.point_3.y - self.point_2.y) ** 2)
        L3 = sqrt((self.point_3.x - self.point_1.x) ** 2 + (self.point_3.y - self.point_1.y) ** 2)
        
        if L1 + L2 <= L3 or L3 + L2 <= L1 or L1 + L3 <= L2:
            
            print('Incorrect input, triangle not modified.')
        self._compute_perimeter()
        self._compute_area()
             

