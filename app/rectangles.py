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


class RectangleProblem(BaseModel):
    big_rectangle: Rectangle
    small_rectangle: Rectangle

    def get_number_of_rectangles_for_normal(self):
        b_width = self.big_rectangle.width
        s_width = self.small_rectangle.width
        number_of_rectangles_using_width = b_width / s_width
        b_height = self.big_rectangle.height
        s_height = self.small_rectangle.height
        number_of_rectangles_using_height = b_height / s_height
        return {
            "number_using_width": number_of_rectangles_using_width,
            "number_using_height": number_of_rectangles_using_height,
        }

    def get_number_of_rectangles_for_rotated(self):
        b_width = self.big_rectangle.width
        s_width = self.small_rectangle.height
        number_of_rectangles_using_width = b_width / s_width
        b_height = self.big_rectangle.height
        s_height = self.small_rectangle.width
        number_of_rectangles_using_height = b_height / s_height
        return {
            "number_using_width": number_of_rectangles_using_width,
            "number_using_height": number_of_rectangles_using_height,
        }

    def solve(self):
        solution = [
            Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
            Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
            Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=2)),
            Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=3)),
            Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=4)),
            Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=0)),
            Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=2)),
        ]
        return solution
