# start uvicorn
source ./canvas_rect/bin/activate
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload