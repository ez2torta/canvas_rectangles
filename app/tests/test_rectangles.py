from app.rectangles import RectanglePosition, Rectangle, RectangleProblem


def test_basic_rectangle_usage():
    rectangle = Rectangle(width=16, height=9)
    assert rectangle



def test_basic_rectangle_overlap():
    rec_1 = Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=0))
    rec_2 = Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=0))
    assert rec_1.overlap_with_other(rec_2)

    rec_1 = Rectangle(width=3, height=2, position=RectanglePosition(x=0, y=1))
    rec_2 = Rectangle(width=1, height=2, position=RectanglePosition(x=1, y=0))
    assert rec_1.overlap_with_other(rec_2)

    rec_1 = Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0))
    rec_2 = Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=2))
    assert not rec_1.overlap_with_other(rec_2)

    rec_1 = Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0))
    rec_2 = Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=0))
    assert not rec_1.overlap_with_other(rec_2)


def test_get_number_using_normal():
    big_rectangle = Rectangle(width=4, height=2)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    problem_solution = problem.get_number_of_rectangles_for_normal()
    fixed_solution = (2.0, 2.0)
    assert problem_solution == fixed_solution


def test_get_number_using_rotated():
    big_rectangle = Rectangle(width=4, height=2)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    problem_solution = problem.get_number_of_rectangles_for_rotated()
    fixed_solution = (4.0, 1.0)

    assert problem_solution == fixed_solution


def test_get_rectangles_for_normal():
    big_rectangle = Rectangle(width=4, height=2)
    small_rectangle = Rectangle(width=2, height=1)

    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    rectangles = problem.get_rectangles_for_normal()
    assert rectangles == [
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=1)),
    ]


def test_get_rectangles_for_rotated():
    big_rectangle = Rectangle(width=4, height=2)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    rectangles = problem.get_rectangles_for_rotated()
    assert rectangles == [
        Rectangle(width=1, height=2, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=1, height=2, position=RectanglePosition(x=1, y=0)),
        Rectangle(width=1, height=2, position=RectanglePosition(x=2, y=0)),
        Rectangle(width=1, height=2, position=RectanglePosition(x=3, y=0)),
    ]


def test_basic_solution_for_basic_rectangle():
    big_rectangle = Rectangle(width=4, height=2)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    problem_solution = problem.solve()
    test_solution = [
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=1)),
    ]
    fixed_solution = [
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=1, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=1, y=1)),
    ]
    assert problem_solution == fixed_solution


def test_fixed_solution_for_rectangle_problem():
    big_rectangle = Rectangle(width=5, height=3)
    small_rectangle = Rectangle(width=2, height=1)
    problem = RectangleProblem(
        big_rectangle=big_rectangle,
        small_rectangle=small_rectangle,
    )
    problem_solution = problem.solve()
    test_solution = [
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=0, y=2)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=0)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=1)),
        Rectangle(width=2, height=1, position=RectanglePosition(x=2, y=2)),
    ]

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
