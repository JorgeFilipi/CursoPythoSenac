from flask import Blueprint, render_template, request, url_for, redirect
from services.task_service import TaskService

task_blueprint = Blueprint('task', __name__)
task_service = TaskService()

@task_blueprint.route("/")
def index():
    tarefas = task_service.listar_tarefas()
    return render_template("index.html", tarefas=tarefas)

@task_blueprint.route("/adicionar", methods=["POST"])
def adicionar():
    conteudo = request.form.get("tarefa")

    try:
        task_service.adicionar_tarefa(conteudo)
    except ValueError as e:
        return str(e), 400

    return redirect(url_for("task.index"))

@task_blueprint.route("/completa/<int:tarefa_id>")
def completar(tarefa_id):
    try:
        task_service.completar_tarefa(tarefa_id)
    except IndexError as e:
        return str(e), 400
    return redirect(url_for("task.index"))

@task_blueprint.route("/remover/<int:tarefa_id>")
def remover(tarefa_id):
    try:
        task_service.remover_tarefa(tarefa_id)
    except IndexError as e:
        return str(e), 400
    return redirect(url_for("task.index"))