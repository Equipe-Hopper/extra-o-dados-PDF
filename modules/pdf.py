import pdfplumber
import pandas as pd
import re
import openpyxl

class Pdf:

    def __init__(self,pdf_path):
        self.pdf_path = pdf_path
        pass

    
    def extract_phone_numbers(self):
        all_text = ""
        #extrai o texto do pdf
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    all_text += page_text

        text = all_text.strip()

        # Regex para encontrar números de telefone # remover alguns caracteres especiais
        phone_pattern = re.compile(r'\(\d{2}\)\s*\d{5}-\d{4}|\(\d{2}\)\s*\d{4}-\d{4}')
        phones = phone_pattern.findall(text)

        if not phones:
            print("Nenhum número de telefone encontrado.")
            return None

        # Remover duplicatas  #Converte a lista phones em um conjunto (set). 
        unique_phones = list(set(phones)) #Como conjuntos em Python não permitem elementos duplicados, todos os itens duplicados são automaticamente removidos.

        # Criar DataFrame
        df = pd.DataFrame(unique_phones, columns=['Telefone'])

        # Salvar DataFrame em Excel
        output_file = 'resources/telefones_extraidos.xlsx'
        df.to_excel(output_file, index=False)
        print(f'Números de telefone extraídos e salvos em: {output_file}')

        return output_file