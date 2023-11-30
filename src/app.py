from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    grupo="IEVN"
    lista=["IEVN 1001,IEVN 1002,IEVN 1002"]
    return render_template('index.html',grupo=grupo,lista=lista)

@app.route('/hola')
def hola():
    return "Saludo UTL"

@app.route('/user/<string:nombre>')
def user(nombre):
    return 'Saludos {0}'.format(nombre)

@app.route('/numero/<int:n1>')
def nummero(n1):
    return 'el numero es: {}'.format(n1)

@app.route('/user/<int:id>/<string:nom>')
def user1(id,nom):
    return 'ID: {} Nombre {}'.format(id,nom)

@app.route('/suma/<float:n1>/<float:n2>')
def suma(n1,n2):
    return 'la sumaaaa eeeeees: {}'.format(n1+n2)

@app.route('/default')
@app.route('/default/<string:dd>')
def default(dd='fulanito'):
    return"<h1>El nombre es {} </h1>".format(dd)

@app.route('/alumnos')
def alumnos():
    return render_template(alumnos.html)

if __name__=="__main__":
    app.run(debug=True)

