from gtts import gTTS
from tempfile import TemporaryFile
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
def convert_text_speach():
    tts = gTTS('我不明白你的問題，請再重複一次', lang='zh-tw')
    f = TemporaryFile()
    tts.write_to_fp(f)
    f.seek(0)
    return f



some_file_path = "large-video-file.mp4"
app = FastAPI()


@app.get("/")
async def main():
    return  StreamingResponse(convert_text_speach(), media_type="audio/mpeg")