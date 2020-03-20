from flask import Flask,render_template #llamamos flask y lo inicializamos render template hace render de html
app = Flask(__name__)

@app.route('/')#esta es la pagina principal
def home():#funcion home returna un texto en este momento
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/FAQ")
def FAQ():
    return render_template('FAQ.html')

if __name__ == '__main__':#Validar que sea en index del servicio
    app.run(debug=True)