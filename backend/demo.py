import io
import numpy as np
from PIL import Image
from tensorflow.keras.preprocessing.image import img_to_array
import rag  # Import your RAG module
from sky_test_v1 import validate_image  # Import your validation function
from model_v3 import air_pridiction  # Import your prediction function

# Load the image locally
image_path = "./pic.jpg"

try:
    # Open the image file in binary mode
    with open(image_path, "rb") as image_file:
        image_content = image_file.read()

    # Convert to a BytesIO object and then to a PIL Image
    pil_image = Image.open(io.BytesIO(image_content))
    pil_image = pil_image.convert("RGB")

    # Resize the image to 224x224 for the model
    pil_image = pil_image.resize((224, 224))

    # Convert to a numerical array
    img_array = img_to_array(pil_image) / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    print(f"Image processed successfully, shape: {img_array.shape}")

    # Validate the image using sky_test_v1
    if not validate_image(img_array):
        print("Invalid image input (not the sky).")
    else:
        # Run prediction using model_v3
        cnn_result = air_pridiction(img_array)
        print(f"CNN Prediction Result: {cnn_result}")

        # Call the RAG function to generate a response
        text_input = "How is air condition in india"  # Replace with your desired text input
        response_text = "CNN air pollution analysis: "
        response_text += cnn_result
        response_text += rag.initialize(text_input, cnn_result)
        print("Generated Response:")
        print(response_text)

except Exception as e:
    print(f"Error during processing: {e}")



# text_input = "How is air condition in india"  # Replace with your desired text input
# cnn_result = "PM2.5: 326/ PM10: 261"
# response_text = rag.initialize(text_input, cnn_result)
