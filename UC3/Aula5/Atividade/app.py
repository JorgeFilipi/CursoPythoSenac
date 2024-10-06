from flask import Flask, render_template, url_for, redirect, request

app=Flask(__name__)

bikes = []

@app.route("/")
def index():
    return render_template("index.html", bikes=bikes)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nova_bike = request.form.get("bike")
    if nova_bike:
        nova_bike = {"marca": nova_bike, "status": False}
        bikes.append(nova_bike)
    return redirect(url_for("index"))

@app.route("/completar/<int:bike_id>")
def completar(bike_id):
    bikes[bike_id]["status"] = True
    return redirect(url_for("index"))

@app.route("/remover/<int:bike_id>")
def remover(bike_id):
    bikes.pop(bike_id)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
