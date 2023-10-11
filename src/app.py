from flask import Flask, render_template, request
import werkzeug.exceptions
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    try:
        criterios = [int(request.form[f'criterio{i}']) for i in range(1, 8)]
        criterios[0] *= 2
        criterios[-1] *= 2
        return render_template('avaliador.html', media=sum(criterios))
    except werkzeug.exceptions.BadRequestKeyError:
        return render_template('avaliador.html', media="Existem campos em branco.")

for element in os.listdir(os.getcwd() + "/src/templates"):
    name = str(element).split(".")[0]
    if name == "intro":continue
    exec(f'''
@app.route("/{name}")
def {name}():
    return render_template("/{element}")
    ''')

if __name__ == '__main__':
    app.run(debug=True)
