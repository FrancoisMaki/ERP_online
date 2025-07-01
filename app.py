from flask import Flask, send_from_directory
from components.controller.country_controller import pais_bp

app = Flask(__name__, static_folder='public')

app.register_blueprint(pais_bp)

# Ruta para servir el HTML
@app.route('/')
def index():
    return send_from_directory('public/html', 'countries.html')

# Opcional: si quieres servir js directamente, no es necesario si static_folder está bien
@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('public/js', filename)

if __name__ == '__main__':
    app.run(debug=True)
