from flask import Blueprint, render_template, request, redirect, url_for
from services.bike_service import BikeService

bike_bp = Blueprint('bike_bp', __name__)
bike_service = BikeService()

@bike_bp.route('/')
def index():
    bikes = bike_service.get_all_bikes()
    return render_template('index.html', bikes=bikes)

@bike_bp.route('/add', methods=['POST'])
def add_bike():
    model = request.form['model']
    category = request.form['category']
    price = float(request.form['price'])
    bike_service.add_bike(model, category, price)
    return redirect(url_for('bike_bp.index'))

@bike_bp.route('/sell/<model>', methods=['POST'])
def sell_bike(model):
    bike_service.sell_bike(model)
    return redirect(url_for('bike_bp.index'))

@bike_bp.route('/delete/<model>', methods=['POST'])
def delete_bike(model):
    bike_service.delete_bike(model)
    return redirect(url_for('bike_bp.index'))
