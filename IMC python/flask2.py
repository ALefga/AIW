from flask import Flask, request, render_template

app = Flask(__name__)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc >= 18.5 and imc <= 24.9:
        return "Normal"
    elif imc >= 25 and imc <= 29.9:
        return "Sobrepeso"
    else:
        return "Obesidad"

@app.route("/IMC", methods=["POST","GET"])
def calcular_imc_flask():
    if request.method == "POST":
        peso = float(request.form.get("Peso"))
        altura = float(request.form.get("Altura"))

        imc = calcular_imc(peso, altura)
        clasificacion = clasificar_imc(imc)

        return render_template("index1.html", imc=imc, clasificacion=clasificacion)
    else:
        return render_template("index1.html")

if __name__ == "__main__":
    app.run()

"""
menor de 18.5 bajo peso
18.5 y 24.9 normal
25 y 29.9 sobrepeso
mayor de 30 obesidad
"""
