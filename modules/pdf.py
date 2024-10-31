from PyPDF2 import PdfReader  
import pdfplumber
import pandas as pd
import re

class Pdf:
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