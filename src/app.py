from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/intro')
def intro():
    return render_template('intro.html')

for element in os.listdir(os.getcwd() + "/templates"): # Get elements in template directory
    pagename = str(element).split(".")[0]
    if pagename == "intro":continue
    # Add element to Flask environment
    exec(f'''
print(element, pagename)
@app.route("/"+pagename)
def {pagename}():
    print("{pagename}", element)
    return render_template("{element}")''')

if __name__ == '__main__':
    app.run(debug=True)
