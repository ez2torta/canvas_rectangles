from app.rectangles import RectanglePosition, Rectangle, RectangleProblem


def test_basic_rectangle_usage():
    rectangle = Rectangle(width=16, height=9)
    assert rectangle


def test_fixed_solution_for_rectangle_problem():
    big_rectangle = Rectangle(width=5, height=3)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    problem_solution = problem.solve()

    fixed_solution = [
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=2)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=3)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=4)),
        Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=0)),
        Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=2)),
    ]
    assert problem_solution == fixed_solution
