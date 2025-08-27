from flask import Flask, render_template, request, send_file, jsonify
from rembg import remove
from PIL import Image
import io, os, logging

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'Nenhum arquivo enviado', 400
    file = request.files['file']
    if file.filename == '':
        return 'Arquivo inválido', 400
    try:
        input_image = Image.open(file.stream).convert('RGBA')
    except Exception as e:
        app.logger.exception('Erro ao abrir a imagem')
        return 'Não foi possível abrir a imagem', 400

    try:
        # rembg aceita bytes-like objects or PIL Image
        output = remove(input_image)
    except Exception as e:
        app.logger.exception('Erro na remoção de fundo')
        return 'Erro ao processar a imagem no servidor', 500

    # Garantir PNG com canal alfa
    img_io = io.BytesIO()
    output.save(img_io, format='PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='semfundo.png')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
