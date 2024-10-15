from repositories.task_repository import TaskRepository

class TaskService:
    def adicionar_tarefa(self, conteudo, prioridade="Média"):
        if not conteudo:
            raise ValueError("A tarefa não pode ser vazia")
        TaskRepository.add_task(conteudo, prioridade)

    def lista_tarefas(self):
        return TaskRepository.get_all_task()

    def completar_tarefa(self, tarefa_id):
        TaskRepository.complete_task(tarefa_id)  # Corrigido 'completa_task' para 'complete_task'

    def remover_tarefa(self, tarefa_id):
        TaskRepository.delete_task(tarefa_id)
