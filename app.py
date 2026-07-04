from flask import Flask, render_template, request, jsonify
import io
import base64
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

app = Flask(__name__)

def apply_effects(img, op):
    if op == 'grayscale': 
        img = img.convert('L').convert('RGB')
    elif op == 'blur': 
        img = img.filter(ImageFilter.GaussianBlur(5))
    elif op == 'brightness': 
        img = ImageEnhance.Brightness(img).enhance(1.5)
    elif op == 'threshold': 
        img = img.convert('L').point(lambda p: 255 if p > 128 else 0).convert('RGB')
    elif op == 'invert':
        img = ImageOps.invert(img)
    elif op == 'sepia':
        # Formula konversi matriks warna Sepia standar
        sepia_data = [
            0.393, 0.769, 0.189, 0,
            0.349, 0.686, 0.168, 0,
            0.272, 0.534, 0.131, 0
        ]
        img = img.convert('RGB', sepia_data)
    elif op == 'contrast':
        img = ImageEnhance.Contrast(img).enhance(2.0)
    elif op == 'edge': 
        img = img.filter(ImageFilter.FIND_EDGES)
    elif op == 'sharpen':
        img = img.filter(ImageFilter.SHARPEN)
    return img

def img_to_base64(img):
    output = io.BytesIO()
    img.save(output, format="PNG")
    b64_string = base64.b64encode(output.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{b64_string}"

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/webcam_page')
def webcam_page(): 
    return render_template('webcam.html')

@app.route('/upload_image', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    img = Image.open(request.files['file'].stream).convert('RGB')
    img = apply_effects(img, request.form.get('operation'))
    return jsonify({'url': img_to_base64(img)})

@app.route('/save_webcam', methods=['POST'])
def save_webcam():
    data_data = request.json['imageData']
    img_bytes = base64.b64decode(data_data.split(',')[1] if ',' in data_data else data_data)
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img = apply_effects(img, request.json.get('operation', 'none'))
    return jsonify({'url': img_to_base64(img)})

if __name__ == '__main__':
    app.run(debug=True)