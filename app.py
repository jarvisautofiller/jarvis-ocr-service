# from easyocr import Reader
# reader = Reader(['en'])  # Add Indian languages
# result = reader.readtext('temp.jpeg', detail=0)
# print(result)
from flask import Flask, request, jsonify
from easyocr import Reader
import os
import tempfile

app = Flask(__name__)

# Load the EasyOCR reader once at startup
reader = Reader(['en'])  # English + Telugu

@app.route("/")
def index():
    return "EasyOCR API is running", 200

@app.route("/ocr", methods=["POST"])
def ocr():
    if 'image' not in request.files:
        return jsonify({"error": "No image file uploaded"}), 400

    image_file = request.files['image']

    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp:
            image_path = temp.name
            image_file.save(image_path)

        # Perform OCR
        result = reader.readtext(image_path, detail=0)

        # Clean up temp file
        os.remove(image_path)

        return jsonify({"text": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8080)
