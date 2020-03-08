from flask import Flask, render_template
from algo import Parse
import sys

app = Flask(__name__)
#  calls algo file and lauches localhost which uses home.html ## just run this file to see result
@app.route('/')
def hello():
    verose = False
    if "-v" in str(sys.argv):
        verose = True
    p = Parse(verose)
    data= p.information
    return render_template('home.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)





