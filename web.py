from flask import Flask, render_template, request
import math
import calculate

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/paralel', methods=['POST'])
def switch_to_par():
    if request.method == 'POST':
        return render_template("paralel.html")

@app.route('/piramid', methods=['POST'])
def switch_to_pir():
    if request.method == 'POST':
        return render_template("piramid.html")

@app.route('/cilin', methods=['POST'])
def switch_to_cil():
    if request.method == 'POST':
        return render_template("cilin.html")

@app.route('/start_page', methods=['POST'])
def switch_to_start():
    if request.method == 'POST':
        return render_template("index.html")

@app.route('/calculate_par', methods=['POST'])
def calculate_par():
    if request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        w = int(request.form.get('w'))
        result = calculate.par(a, b, c, w)
    return render_template("paralel.html", result_value=result)

@app.route('/calculate_pir', methods=['POST'])
def calculate_pir():
    if request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        c = float(request.form.get('c'))
        w = float(request.form.get('w'))
        result = calculate.pir(a, b, c, w)
    return render_template("piramid.html", result_value=result)

@app.route('/calculate_cil', methods=['POST'])
def calculate_cil():
    if request.method == 'POST':
        a = float(request.form.get('a'))
        b = float(request.form.get('b'))
        w = float(request.form.get('w'))
        result = calculate.cil(a, b, w)
    return render_template("cilin.html", result_value=result)

if __name__ == '__main__':
    app.run()