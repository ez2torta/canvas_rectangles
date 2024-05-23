from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from app.rectangles import Rectangle, RectangleProblem

app = FastAPI()

origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def root():
    return {"message": "Hello World"}


@app.get("/rectangle_problem/{big_width}/{big_height}/{small_width}/{small_height}")
def rectangle_problem(
    big_width: int, big_height: int, small_width: int, small_height: int
):
    small_rectangle = Rectangle(width=small_width, height=small_height)
    big_rectangle = Rectangle(width=big_width, height=big_height)
    problem = RectangleProblem(
        small_rectangle=small_rectangle, big_rectangle=big_rectangle
    )
    solution = problem.solve()
    return solution


@app.exception_handler(404)
async def custom_404_handler(request: Request, exc: HTTPException):
    return FileResponse("./static/index.html")


try:
    app.mount("/", StaticFiles(directory="static", html=True), name="static")
except:
    raise ValueError("No pude montar la carpeta static.. existe la carpeta static?")
