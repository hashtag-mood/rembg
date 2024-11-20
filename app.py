from flask import Flask, request, send_file
from flask_cors import CORS
from rembg import remove
from PIL import Image
import io
import os

app = Flask(__name__)
CORS(app)


@app.route('/rembg', methods=['GET', 'POST'])
def remove_background():
    if 'image' not in request.files:
        return 'No file part', 400

    image_file = request.files['image']
    img = Image.open(image_file)

    if img.mode == 'RGBA':
        img = img.convert('RGB')

    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    out_byte_arr = remove(img_byte_arr)

    out_img = Image.open(io.BytesIO(out_byte_arr))

    output = io.BytesIO()
    out_img.save(output, format='PNG')
    output.seek(0)

    return send_file(output, mimetype='image/png')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(debug=True, host='0.0.0.0', port=port)
