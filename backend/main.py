from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional

app = FastAPI()

@app.post("/api/upload")
async def upload_data(
    text: Optional[str] = Form(None),  # Make text optional
    image: Optional[UploadFile] = File(None)  # Make image optional
):
    response_text = "這是後端生成的回覆"
    
    if text:
        print(f"收到的問題: {text}")
    if image:
        image_content = await image.read()
        print(f"收到圖片: {image.filename}")

    return {"response": response_text}

