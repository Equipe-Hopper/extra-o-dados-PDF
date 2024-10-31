from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv
import os

load_dotenv()

class Email:
    def __init__(self):
        pass
    def send_email_with_attachment(self,file_path)->None:
        email = BotEmailPlugin()

        # Configurar IMAP e SMTP com o servidor Gmail
        email.configure_imap("imap.gmail.com", 993)
        email.configure_smtp("smtp.gmail.com", 587)

        email.login(os.getenv("USER"), os.getenv("SENHA"))  # Substitua pelos seus dados

        # Definir os atributos da mensagem
        to = ["armando.goncalves@ifam.edu.br"]  
        subject = "Arquivo Excel Gerado"
        body = "<h1>Olá!</h1> Arquivo de envio automático."
        files = [file_path]

        # Enviar a mensagem de e-mail
        email.send_message(subject, body, to, attachments=files, use_html=True)

        # Fechar a conexão com os servidores IMAP e SMTP
        email.disconnect()