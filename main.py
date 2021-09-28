from gtts import gTTS
from tempfile import TemporaryFile
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse
from starlette.requests import Request


def convert_text_speach():
    tts = gTTS('我不明白你的問題，請再重複一次', lang='zh-tw')
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.seek(0)
    return f


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# @app.get("/")
# async def main():
#     return  StreamingResponse(convert_text_speach(), media_type="audio/mpeg")


@app.get("/", response_class=HTMLResponse)
def http(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload-text")
async def main(upload_text: Request):
    text = await upload_text.json()
    return text
    # return  StreamingResponse(convert_text_speach(), media_type="audio/mpeg")
