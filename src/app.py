from flask import Flask, render_template, request
from jinja2.exceptions import TemplateNotFound
from werkzeug.exceptions import BadRequestKeyError

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
        pontuacao = sum(criterios) / 4.5
        if pontuacao <= 3:
            return render_template('avaliador.html', media="Muito ruim")
        elif 3 < pontuacao <= 6:
            return render_template('avaliador.html', media="Ruim")
        elif 6 < pontuacao <= 7:
            return render_template('avaliador.html', media="Aceitável")
        elif 7 < pontuacao <= 9:
            return render_template('avaliador.html', media="Bom")
        elif pontuacao > 9:
            return render_template('avaliador.html', media="Excelente")
        
    except BadRequestKeyError:
        return render_template('avaliador.html', media="Existem campos em branco")

@app.route("/<filename>")
def templates(filename):
    try:
        return render_template(f"{filename}.html")
    except TemplateNotFound:
        return "Página não encontrada", 404

if __name__ == '__main__':
    app.run(debug=True)
