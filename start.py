from pathlib import Path
from random import choice

import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from starlette.requests import Request
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/forever")
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {'request': request})


@app.get("/pics/{pic_name}")
async def get_pic(pic_name: str):
    return FileResponse(f"./pictures/{pic_name}")


@app.get("/", response_class=HTMLResponse)
async def read_items():
    file_loc = Path(__file__).parent
    pics = (file_loc / "pictures").iterdir()
    choose_one = choice(list(pics))
    choose_name = choose_one.name
    return f"""
    <html>
        <head>
        <meta charset="utf-8"> 
            <title>Honey, you're wearing this today</title>
        </head>
        <body>
            <p>老婆今天穿这套怎么样:</p>
            <img src="./pics/{choose_name}" alt="today wear">
            <p>老婆真漂亮，爱你哟</p>
        </body>
    </html>
    """


# @app.post("/upload_collections", tags=['Upload files to directory'])
# async def upload_files(files: str):
#     file_list = []
#     for single_file in files:
#         with open(single_file.filename, "wb") as buffer:
#             shutil.copy(single_file.filename, 'uploaded_files/')
#             os.remove(single_file.filename)
#         file_list.append(single_file.filename)
#     return "The following files has been uploaded:" + str(file_list)


if __name__ == '__main__':
    uvicorn.run(app='start:app', host="0.0.0.0",
                port=8000, reload=True, debug=True)
