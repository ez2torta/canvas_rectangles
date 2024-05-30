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

    def get_rectangles_for_normal(self) -> list[Rectangle]:
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

    def get_rectangles_for_normal_with_offset(
        self, offset_x, offset_y
    ) -> list[Rectangle]:
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

    def get_rectangles_for_rotated(self) -> list[Rectangle]:
        b_width = self.big_rectangle.width
        b_height = self.big_rectangle.height
        s_width = self.small_rectangle.width
        s_height = self.small_rectangle.height
        rectangles = []
        for i in range(0, b_width, s_height):
            for j in range(0, b_height, s_width):
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
    ) -> list[Rectangle]:
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

    def add_to_solution(self, rect: Rectangle):
        overlaps_with_solution = any(r.overlap_with_other(rect) for r in self.solution)
        overlaps_with_big_rectangle = rect.overlap_with_other(self.big_rectangle)
        exceeds_big_rectangle = (
            rect.position.x + rect.width > self.big_rectangle.width
        ) or (rect.position.y + rect.height > self.big_rectangle.height)
        if (
            not overlaps_with_solution
            and overlaps_with_big_rectangle
            and not exceeds_big_rectangle
        ):
            self.solution.append(rect)

    def solve(self):
        for i in [0, 1]:
            for j in [0, 1]:
                offset_rectangles = self.get_rectangles_for_normal_with_offset(
                    offset_x=i, offset_y=j
                )
                for rect in offset_rectangles:
                    self.add_to_solution(rect)
        for i in [0, 1]:
            for j in [0, 1]:
                offset_rectangles = self.get_rectangles_for_rotated_with_offset(
                    offset_x=i, offset_y=j
                )
                for rect in offset_rectangles:
                    self.add_to_solution(rect)

        return self.solution
