from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def not_found(e):
    return "<p>¡Lo siento! No hay respuesta. Inténtalo otra vez</p>"

@app.route('/', methods=['GET'])
def index():
    users = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

    return render_template("table.html", users = users)

if __name__ == "__main__":
    app.run( debug = True )