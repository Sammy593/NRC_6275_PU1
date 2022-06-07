#importar la libreria flask
from flask import Flask, redirect, request, render_template, url_for
app = Flask(__name__, template_folder='templates')

@app.route('/')
#contenedor para llamar a index.html
def index():
    return render_template('/index.html')

#ejecutar
if __name__ == '__main__':
    app.run(debug=True)