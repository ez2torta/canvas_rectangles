# vamos a resolver el problema de rectángulos chicos
# dentro de rectángulos grandes

# para esto necesitamos utilizar un par de cálculos y poder estimar
# si caben o no caben los rectángulos según un criterio
from pydantic import BaseModel


class RectanglePosition(BaseModel):
    x: int
    y: int


class Rectangle(BaseModel):
    width: int
    height: int
    position: RectanglePosition = RectanglePosition(x=0, y=0)

    def overlap_with_other_rectangle(self, other):
        set_1 = set(self.to_point_tuple_list())
        answer = set_1.intersection(other.to_point_tuple_list())
        return answer

    def to_point_tuple_list(self):
        tuples = set()
        for i in range(self.position.x, self.position.x + self.width, 1):
            for j in range(self.position.y, self.position.y + self.height, 1):
                # print(f"i = {i} j = {j} \n")
                tuples.add((i, j))
        return tuples


class RectangleProblem(BaseModel):
    big_rectangle: Rectangle
    small_rectangle: Rectangle
    solution: list[Rectangle] = []

    def get_number_of_rectangles_for_normal(self):
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        number_of_rectangles_using_width = int(b_width / s_width)
        number_of_rectangles_using_height = int(b_height / s_height)
        return (number_of_rectangles_using_width, number_of_rectangles_using_height)

    def get_number_of_rectangles_for_rotated(self):
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        number_of_rectangles_using_width = int(b_width / s_height)
        number_of_rectangles_using_height = int(b_height / s_width)
        return (number_of_rectangles_using_width, number_of_rectangles_using_height)

    def get_rectangles_for_normal(self):
        # width, height = self.get_number_of_rectangles_for_normal()
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        rectangles = []
        for i in range(0, b_width, s_width):
            for j in range(0, b_height, s_height):
                rectangles.append(
                    Rectangle(
                        width=s_width,
                        height=s_height,
                        position=RectanglePosition(x=i, y=j),
                    )
                )
        return rectangles

    def get_rectangles_for_rotated(self):
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        rectangles = []
        for i in range(0, b_width, s_height):
            for j in range(0, b_height, s_width):
                # print(f"i = {i} j = {j} \n")
                rectangles.append(
                    Rectangle(
                        width=s_height,
                        height=s_width,
                        position=RectanglePosition(x=i, y=j),
                    )
                )
        return rectangles

    def get_rectangles_for_rotated_offset(self):
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        rectangles = []
        for i in range(b_width, 0, s_height):
            for j in range(b_height, 0, s_width):
                # print(f"i = {i} j = {j} \n")
                rectangles.append(
                    Rectangle(
                        width=s_height,
                        height=s_width,
                        position=RectanglePosition(x=i, y=j),
                    )
                )
        return rectangles

    def solve(self):
        final_rectangles = []
        normal_rectangles = self.get_rectangles_for_normal()
        rotated_rectangles = self.get_rectangles_for_rotated_offset()
        # breakpoint()
        for rect in normal_rectangles:
            # print(rect)
            big_overlap = self.big_rectangle.overlap_with_other_rectangle(rect)
            small_tuple_list = rect.to_point_tuple_list()
            if len(small_tuple_list) == len(big_overlap):
                final_rectangles.append(rect)
        final_tuple_list = set()
        for rect in normal_rectangles:
            final_tuple_list = final_tuple_list.union(rect.to_point_tuple_list())
        # breakpoint()
        for rect in rotated_rectangles:
            tuple_list = rect.to_point_tuple_list()
            # breakpoint()
            difference = tuple_list.difference(final_tuple_list)
            print(difference)
            if difference:
                final_rectangles.append(rect)
        return final_rectangles
