from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

# @app.route('/burndown')
# def burndown():
#     return render_template('burndown.html')


# @app.route('/sprint')
# def sprint():
#     return render_template('sprint.html')

# @app.route('/productowner')
# @app.route('/po')
# def po():
#     return render_template('po.html')

for element in os.listdir(os.getcwd() + "/src/templates"):
    pagename = str(element).split(".")[0]
    if pagename == "intro":continue
    exec(f'''
print(element, pagename)
@app.route("/"+pagename)
def {pagename}():
    print("{pagename}", element)
    return render_template("element")''')
if __name__ == '__main__':
    app.run(debug=True)
