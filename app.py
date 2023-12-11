# app.py
from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

@app.route('/index')
def home():
    print("app.py")
    # return redirect(url_for('add_device.index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
