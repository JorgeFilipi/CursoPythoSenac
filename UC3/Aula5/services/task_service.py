from  models.task_model import Task

class TaskService:

    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, conteudo):
        if not conteudo:
            raise  ValueError("A terefa não pode ser vazia")

        nova_tarefa = Task(conteudo, False)
        self.tarefas.append(nova_tarefa)

    def listar_tarefas(self):
        return self.tarefas

    def completar_tarefa(self, tarefa_id):
        self.tarefas[tarefa_id].completa = True

    def remover_tarefas(self, tarefa_id):
        self.tarefas.pop(tarefa_id)