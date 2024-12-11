from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io
import rag
from sky_test_v1 import validate_image
from model_v3 import air_pridiction

app = FastAPI()

@app.post("/api/upload")
async def upload_data(
    text: Optional[str] = Form(None),  # Make text optional
    image: Optional[UploadFile] = File(None)  # Make image optional
):
    response_text = "這是後端生成的回覆"

    if text:
        print(f"收到的問題: {text}")
        # Call the RAG function with text
        if image:
            # 讀取圖片內容
            image_content = await image.read()
            # 轉換為 PIL Image 格式
            pil_image = Image.open(io.BytesIO(image_content))
            pil_image = pil_image.convert("RGB")
            # 調整圖片大小以符合模型的輸入要求 (假設模型需要 224x224)
            pil_image = pil_image.resize((224, 224))
            # 轉換為數值矩陣
            img_array = img_to_array(pil_image) / 255.0  # 標準化
            img_array = np.expand_dims(img_array, axis=0)  # 添加批次維度
            print(f"圖片處理完成，形狀: {img_array.shape}")

            # 呼叫 sky_test_v1.py 檢查是否合法
            if not validate_image(img_array):
                return {"response": "Invalid image input (not the sky)."}
                # return JSONResponse(content={"error": "Invalid image input"}, status_code=400)
            else:
                # Run prediction using model_v3
                cnn_result = air_pridiction(img_array)
                print(f"CNN Prediction Result: {cnn_result}")

                # Call the RAG function to generate a response
                response_text = "CNN air pollution analysis: "
                response_text += cnn_result
                response_text += rag.initialize(text, cnn_result)
        else:
            response_text = rag.initialize(text)
    else:
        response_text = "Error: empty input."


    return {"response": response_text}
