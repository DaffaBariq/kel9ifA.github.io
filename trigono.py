import math
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/ten')
def tentang():
    return render_template('ten.html')

@app.route('/kal')
def kalkulator():
    return render_template('kal.html')

@app.route('/materi')
def materi():
    return render_template('materi.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        x = float(request.form['angle'])
    except ValueError:
        return render_template('kal.html', result="Masukkan sudut dalam bentuk angka.")
    fungtri = request.form['function']
    rad = (math.pi / 180) * x
    sin = math.sin(rad)
    cos = math.cos(rad)
    tan = math.tan(rad)

    result = None

    if fungtri == 'sinus':
        result = f'sin {x}° = {round(sin, 3)}'
    elif fungtri == 'cosinus':
        result = f'cos {x}° = {round(cos, 3)}'
    elif fungtri == 'tangen':
        result = f'tan {x}° = {round(tan, 3)}'
    elif fungtri == 'semua':
        result = f'sin {x}° = {round(sin, 3)}\ncos {x}° = {round(cos, 3)}\ntan {x}° = {round(tan, 3)}'
    else:
        result = 'Kesalahan!!! Coba cek penulisan Anda'

    return render_template('kal.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
