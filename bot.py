from modules.email_utils import Email
from modules.pdf import Pdf
from botcity.web import WebBot
from botcity.maestro import *
from modules.maestro import MaestroAlerts

BotMaestroSDK.RAISE_NOT_CONNECTED = False

class Bot(WebBot):

    def action(self=None,execution=None):
        maestro = BotMaestroSDK.from_sys_args()
        execution = maestro.get_execution()

        
        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        maestro_actions= MaestroAlerts(maestro,execution.task_id)

        try:

            # maestro_actions.alert_info(titulo="Iniciando automação",mensagem="A automaçao foi iniciada...")

            # Executar a extração e envio de e-mail
            email = Email()
            pdf = Pdf('resources\Telefone.pdf')
            output_file = pdf.extract_phone_numbers()
          
            # maestro_actions.alert_info(titulo="Extraindo Informaçoes",mensagem="A automaçao esta extraindo informaçoes...")

            if output_file is not None:

              
                # maestro_actions.post_artifact(nome_artefato="Telefones Extraidos",caminho_arq="resources/telefones_extraidos.xlsx")
                
                email.send_email_with_attachment(output_file)

                   
            finshed_status = AutomationTaskFinishStatus.SUCCESS

            finish_message = "Tarefa finalizada com sucesso"
          
            # maestro_actions.alert_success(titulo="Tarefa finalizada com sucesso",mensagem="Tarefa finalizada com sucesso..")

        except Exception as ex:
            print("Error: ", ex)
            self.save_screenshot("resources/erro.png")

            finshed_status = AutomationTaskFinishStatus.FAILED
            finish_message = "Tarefa finalizada com erro"

            # maestro_actions.alert_error(titulo="Tarefa finalizada com ERRO",mensagem="Tarefa finalizada com ERRO...")

        
        finally:
            self.wait(3000)
            # maestro_actions.finish_task(finshed_status=finshed_status,finish_message=finish_message)

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == "__main__":
    Bot.main()
