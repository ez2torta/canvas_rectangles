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
