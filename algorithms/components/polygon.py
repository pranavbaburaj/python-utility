import uuid


class Polygon:
    def __init__(self):
        self.polygon_object = self.create_new_polygon_object()

    def create_new_polygon_object(self):
        return f"Object:{str(uuid.uuid4())}"

    def sides(self, number_of_sides=0, interior_angles=0, exterior_angles=0):
        if interior_angles is not 0:
            """
            @Sum of interior angles:(n - 2) * 180
            @n = (interior_angle / 180 ) + 2
            """
            number_of_sides = (interior_angles / 180) + 2

            if str(number_of_sides).split(".")[-1] == "0":
                return number_of_sides
            else:
                raise Exception(f"Polygon with the sum of interior angles {interior_angles} does not exists")
        elif exterior_angles is not 0:
            if exterior_angles <= 360:
                return 360 / exterior_angles
            else:
                raise Exception(f"Exterior angle cannot exceed 360")
        elif number_of_sides is not 0:
            return number_of_sides
        else:
            raise Exception(f"Cannot find sides without interior or exterior angles")

    def sum_interior_angle(self, sides):
        return (sides - 2) * 180

    def each_interior_angle(self, pattern, interior_angle=0):
        if isinstance(pattern, list):
            value = 0
            for x in range(len(pattern)):
                value += pattern[x]

            if interior_angle > 0:
                return interior_angle / pattern
            else:
                raise Exception(f"Interior angle cannot be 0")
        else:
            raise TypeError(f"Unexpected type {type(pattern)} for patter")

    def sum_exterior_angle(self, sides=0, interior_angle=0):
        if interior_angle is not 0:
            if interior_angle < 180:
                return 180 - interior_angle
            else:
                raise Exception(f"Cannot exceed 180")
        elif sides is not 0:
            return 360 / sides
        else:
            raise Exception(f"Cannot find exterior angles without sides or interior angles")

    def __repr__(self):
        return self.polygon_object
