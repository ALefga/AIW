from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/IMC", methods=["POST","GET"])
def calcular_imc_flask():
    imc=0
    clasificacion=""
    try:
        if request.method == "POST":
            peso = float(request.form.get("Peso"))
            altura = float(request.form.get("Altura"))
            imc = peso / (altura ** 2)

            if imc < 18.5:
                clasificacion = "Bajo peso"
            elif imc >= 18.5 and imc <= 24.9:
                clasificacion = "Normal"
            elif imc >= 25 and imc <= 29.9:
                clasificacion = "Sobrepeso"
            else:
                clasificacion = "Obesidad"
    except ValueError:
        msg= "ingrese solo numeros"
        return render_template("index1.html",msg=msg )
    return render_template("index1.html", imc=imc, clasificacion=clasificacion)
if __name__ == "__main__":
    app.run()
"""
menor de 18.5 bajo peso
18.5 y 24.9 normal
25 y 29.9 sobrepeso
mayor de 30 obesidad
"""
