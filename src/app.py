from flask import Flask, render_template, request
import werkzeug.exceptions
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/processar', methods=['POST'])
def processar_formulario():
    try:
        criterios = [request.form[f'criterio{i+1}'] for i in range(7)]
        criterios = list(map(int, criterios))
        criterios[-3:] = [c * 2 for c in criterios[-3:]]
        media_final = round(sum(criterios) / len(criterios),1)
        return render_template('avaliador.html', media=media_final)
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
