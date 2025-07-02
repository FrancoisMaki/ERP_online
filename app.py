from flask import Flask, render_template
from components.controller.country_controller import pais_bp  # Si ya usas Blueprints
from livereload import Server

app = Flask(__name__, static_folder='static')
app.register_blueprint(pais_bp)

# Página principal (login)
@app.route('/')
def index():
    return render_template('index.html')

# Página principal después del login
@app.route('/main')
def main():
    return render_template('main.html')

# Rutas de mantenimiento
@app.route('/countries')
def countries():
    return render_template('countries.html')

@app.route('/province')
def province():
    return render_template('province.html')

@app.route('/cities')
def cities():
    return render_template('cities.html')

@app.route('/companies')
def companies():
    return render_template('companies.html')

@app.route('/clients')
def clients():
    return render_template('clients.html')

@app.route('/supplier')
def supplier():
    return render_template('supplier.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/warehouses')
def warehouses():
    return render_template('warehouses.html')

# Rutas de almacén
@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/stock')
def stock():
    return render_template('stock.html')

# Rutas de ventas
@app.route('/new_sale')
def new_sale():
    return render_template('new_sale.html')

@app.route('/historial_sale')
def historial_sale():
    return render_template('historial_sale.html')

# Rutas de compras
@app.route('/payment_register')
def payment_register():
    return render_template('payment-register.html')

# Rutas de estadísticas
@app.route('/graphics')
def graphics():
    return render_template('graphics.html')

@app.route('/summary')
def summary():
    return render_template('summary.html')


if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.watch('templates/')
    server.watch('static/css/')
    server.watch('static/js/')
    server.serve(debug=True)    
