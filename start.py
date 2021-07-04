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


@app.get("/dress/{pic_name}")
async def get_pic(pic_name: str):
    return FileResponse(f"./pictures/dress/{pic_name}")


@app.get("/clothes/{pic_name}")
async def get_pic(pic_name: str):
    return FileResponse(f"./pictures/clothes/{pic_name}")


@app.get("/pants/{pic_name}")
async def get_pic(pic_name: str):
    return FileResponse(f"./pictures/pants/{pic_name}")


@app.get("/", response_class=HTMLResponse)
async def read_items():
    file_loc = Path(__file__).parent
    pics = (file_loc / "pictures" / "clothes").iterdir()
    choose_one = choice(list(pics))
    choose_name = choose_one.name
    serial_num = choose_name.split(".")[0]
    print(serial_num)
    if serial_num in [39, 40]:
        pants_num_list = range(53, 56)
        pants_num = choice(pants_num_list)
    elif serial_num == "29":
        pants_num = "54"
    elif serial_num in range(26, 29) or serial_num == "30":
        pants_num = "46"
    elif serial_num in ["12", "36", "37", "38"]:
        pants_num = choice(["41", "42", "43", "44", "48", "50"])
    elif serial_num == "20":
        pants_num = "21"
    elif serial_num == "23":
        pants_num = "44"
    elif serial_num in ["22", "24", "25"]:
        pants_num = "49"
    elif serial_num == "09":
        pants_num = "42"
    elif serial_num == "10":
        pants_num = "54"
    else:
        pants_num = choice(list((file_loc / "pictures" / "pants").iterdir()))
    return f"""
    <html>
        <head>
        <meta charset="utf-8"> 
            <title>Honey, you're wearing this today</title>
        </head>
        <body>
            <p>老婆今天穿这件衣服哦:</p>
            <img src="./clothes/{choose_name}" alt="today wear">
            <p>老婆今天穿这条裤子哦:</p>
            <img src="./pants/{pants_num}.jpg" alt="today wear">
            <p>老婆真漂亮，爱你哟</p>
        </body>
    </html>
    """


@app.get("/dress", response_class=HTMLResponse)
async def read_items():
    file_loc = Path(__file__).parent
    pics = (file_loc / "pictures"/"dress").iterdir()
    choose_one = choice(list(pics))
    choose_name = choose_one.name
    return f"""
    <html>
        <head>
        <meta charset="utf-8"> 
            <title>Honey, you're wearing this today</title>
        </head>
        <body>
            <p>老婆今天穿这条裙子哦:</p>
            <img src="./dress/{choose_name}" alt="today wear">
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
