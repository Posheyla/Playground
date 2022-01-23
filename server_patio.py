from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def paginaInicio():
    return render_template("index.html")

@app.route('/play/<int:numero>')
def paginaSecundaria(numero):
    return render_template("index.html",numero=numero)

@app.route('/play/<int:numero>/<color>')
def paginaTercera(numero,color):
    return render_template("index.html",numero=numero,color=color)

if __name__=="__main__":
    app.run(debug=True)
