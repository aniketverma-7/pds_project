# add_device.py
from flask import Flask, render_template, request, redirect, url_for

add_device_app = Flask(__name__)

# Dummy data, replace with actual database interactions
service_locations = ["Home", "Office"]
device_types = ["Refrigerator", "AC", "Dryer"]
device_models = {"Refrigerator": ["Bosch 800", "Samsung XYZ"], "AC": ["GE 4500", "LG 3000"], "Dryer": ["Model A", "Model B"]}

@add_device_app.route('/')
def index():
    print("add_device.py")
    return render_template('index.html', locations=service_locations)

@add_device_app.route('/add_device', methods=['GET', 'POST'])
def add_device():
    if request.method == 'POST':
        location = request.form.get('location')
        device_type = request.form.get('device_type')
        model = request.form.get('model')
        # Add device to the database (not implemented in this example)
        return redirect(url_for('index'))
    return render_template('add_device.html', locations=service_locations, device_types=device_types, device_models=device_models)

if __name__ == '__main__':
    add_device_app.run(debug=True)
