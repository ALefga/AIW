from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    return render_template("index.html")

@app.route("/")
def hola():
    return "Hola, Bienvenido"
@app.route()
def baloncesto():
    return "Hola, esta es laweb de baloncesto!"
@app.route("/pruebaPost", methods=["POST", "GET"])
def pruebaPost():
    if (request.method == "POST"):
        return "esto es un POST"
    elif (request.method == "GET"):
        return "esto es un get"
    return "hola, esta es la web de baloncesto!"

app.run()