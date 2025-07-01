from flask import Flask, render_template
from components.controller.country_controller import pais_bp

app = Flask(__name__, static_folder='static')

app.register_blueprint(pais_bp)

# Ruta principal que carga el HTML desde /templates
@app.route('/')
def index():
    return render_template('countries.html')  # Busca en templates/countries.html

if __name__ == '__main__':
    app.run(debug=True)
