from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

for element in os.listdir("src/templates"):
    print(element)
    name = str(element).split(".")[0]
    if name == "intro":continue
    exec(f'''
@app.route("/{name}")
def {name}():
    return render_template("/{element}")
    ''')

if __name__ == '__main__':
    app.run(debug=True)
