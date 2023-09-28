from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/burndown')
def burndown():
    return render_template('burndown.html')


@app.route('/sprint')
def sprint():
    return render_template('sprint.html')


if __name__ == '__main__':
    app.run(debug=True)
