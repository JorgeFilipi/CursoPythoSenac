from flask import Flask, render_template, url_for, redirect, request

app=Flask(__name__)

tarefas = []

@app.route("/")
def index():
    return render_template("index.html", tarefas=tarefas)

@app.route("/adicionar", methods=["POST"])
def adicionar():
    nova_tarefa = request.form.get("tarefa")
    if nova_tarefa:
        tarefa = {"conteudo": nova_tarefa, "completa": False}
        tarefas.append(tarefa)
    return redirect(url_for("index"))

@app.route("/completar/<int:tarefa_id>")
def completar(tarefa_id):
    tarefas[tarefa_id]["completa"] = True
    return redirect(url_for("index"))

@app.route("/remover/<int:tarefa_id>")
def remover(tarefa_id):
    tarefas.pop(tarefa_id)
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
