from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def hola():
    if (request.method == "POST"):
        weight = request.form.get("Peso")
        height = request.form.get("Altura")
        
        # Validar que los datos sean numéricos y positivos
        if weight.isnumeric() and height.isnumeric() and float(weight) > 0 and float(height) > 0:
            print(weight + height)
        else:
            # Si los datos no son válidos, mostrar un mensaje de error
            return render_template("error.html", message="Los datos ingresados no son válidos")
    return render_template("index1.html")
app.run()

"""menor de 18.5 bajo peso
18.5 y 24.9 normal
25 y 29.9 sobrepeso
mayor de 30 obesidad
"""
