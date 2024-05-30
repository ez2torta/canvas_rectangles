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

    def overlap_with_other(self, other):
        if (self.position.x + self.width <= other.position.x) or (
            self.position.y + self.height <= other.position.y
        ):
            return False

        if (other.position.x + other.width <= self.position.x) or (
            other.position.y + other.height <= self.position.y
        ):
            return False

        return True


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

    def get_rectangles_for_normal_with_offset(self, offset_x, offset_y):
        normal_rectangles = self.get_rectangles_for_normal()
        offset_rectangles = [
            Rectangle(
                width=r.width,
                height=r.height,
                position=RectanglePosition(
                    x=r.position.x + offset_x, y=r.position.y + offset_y
                ),
            )
            for r in normal_rectangles
        ]
        return offset_rectangles

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

    def get_rectangles_for_rotated_with_offset(
        self, offset_x: int = 0, offset_y: int = 0
    ):
        rotated_rectangles = self.get_rectangles_for_rotated()
        offset_rectangles = [
            Rectangle(
                width=r.width,
                height=r.height,
                position=RectanglePosition(
                    x=r.position.x + offset_x, y=r.position.y + offset_y
                ),
            )
            for r in rotated_rectangles
        ]
        return offset_rectangles

    def solve(self):
        normal_rectangles = self.get_rectangles_for_normal()
        rotated_rectangles = self.get_rectangles_for_rotated()
        for rect in normal_rectangles:
            overlaps = [r.overlap_with_other(rect) for r in self.solution]
            if len(overlaps) == 0:
                self.solution.append(rect)
        for rect in rotated_rectangles:
            overlaps = [r.overlap_with_other(rect) for r in normal_rectangles]
            if len(overlaps) == 0 and rect.overlap_with_other(self.big_rectangle):
                self.solution.append(rect)
        return self.solution
