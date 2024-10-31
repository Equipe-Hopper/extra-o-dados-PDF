from botcity.maestro import *


class MaestroAlerts:
    def __init__(self, maestro, execution):
        self.maestro = maestro
        self.execution = execution

    def alert_info(self, titulo: str, mensagem: str):

        self.maestro.alert(
            task_id=self.execution,
            title=titulo,
            message=mensagem,
            alert_type=AlertType.INFO
        )
        print(f"ESSE É O TASK ID: {self.execution}")

    def alert_success(self, titulo: str, mensagem: str):

        self.maestro.alert(
            task_id=self.execution,
            title=titulo,
            message=mensagem,
            alert_type=AlertType.INFO
        )

    def alert_error(self, titulo: str, mensagem: str):

        self.maestro.alert(
            task_id=self.execution,
            title=titulo,
            message=mensagem,
            alert_type=AlertType.ERROR
        )

    def post_artifact(self, nome_artefato, caminho_arq):

        self.maestro.post_artifact(
            task_id=self.execution,
            artifact_name=nome_artefato,
            filepath=caminho_arq
        )

    def finish_task(self, finshed_status, finish_message):

        self.maestro.finish_task(
            task_id=self.execution,
            status=finshed_status,
            message=finish_message
        )
