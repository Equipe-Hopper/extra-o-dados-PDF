from PyPDF2 import PdfReader  
import pdfplumber
import pandas as pd
import os
import re
from openpyxl import load_workbook
from openpyxl.styles import Alignment
from botcity.plugins.email import BotEmailPlugin
from dotenv import load_dotenv

load_dotenv()

def extract_phone_numbers(pdf_path):
    all_text = ""
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                all_text += page_text

    text = all_text.strip()

    # Regex para encontrar números de telefone
    phone_pattern = re.compile(r'\(\d{2}\)\s*\d{5}-\d{4}|\(\d{2}\)\s*\d{4}-\d{4}')
    phones = phone_pattern.findall(text)

    if not phones:
        print("Nenhum número de telefone encontrado.")
        return None

    # Remover duplicatas
    unique_phones = list(set(phones))

    # Criar DataFrame
    df = pd.DataFrame(unique_phones, columns=['Telefone'])

    # Salvar DataFrame em Excel
    output_file = 'telefones_extraidos.xlsx'
    df.to_excel(output_file, index=False)
    print(f'Números de telefone extraídos e salvos em: {output_file}')

    return output_file

def send_email_with_attachment(file_path):
    email = BotEmailPlugin()

    # Configurar IMAP e SMTP com o servidor Gmail
    email.configure_imap("imap.gmail.com", 993)
    email.configure_smtp("smtp.gmail.com", 587)

    email.login(os.getenv("USER"), os.getenv("SENHA"))  # Substitua pelos seus dados

    # Definir os atributos da mensagem
    to = ["francisco.alberto@ifam.edu.br"]  
    subject = "Arquivo Excel Gerado"
    body = "<h1>Olá!</h1> Arquivo de envio automático."
    files = [file_path]

    # Enviar a mensagem de e-mail
    email.send_message(subject, body, to, attachments=files, use_html=True)

    # Fechar a conexão com os servidores IMAP e SMTP
    email.disconnect()

# Executar a extração e envio de e-mail
output_file = extract_phone_numbers('Telefone.pdf')
if output_file is not None:
    send_email_with_attachment(output_file)
