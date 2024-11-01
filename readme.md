# Projeto de Automação com BotCity

Este projeto utiliza o framework da **BotCity** para automatizar a extração de números de telefone de um arquivo PDF e enviar essas informações por e-mail. A automação é composta por diferentes módulos que trabalham em conjunto para garantir um fluxo de trabalho eficiente.

## Funcionalidades

- **Extração de Números de Telefone**: O projeto utiliza a biblioteca `pdfplumber` para ler e extrair números de telefone de um PDF.
- **Envio de E-mail**: Através do `BotEmailPlugin`, o projeto envia o arquivo Excel gerado com os números extraídos para um endereço de e-mail específico.
- **Alertas e Notificações**: Utiliza o módulo `MaestroAlerts` para enviar notificações sobre o andamento da automação.

## Estrutura do Projeto
```bash
├── modules/
│ ├── email.py # Módulo para envio de e-mails
│ ├── pdf.py # Módulo para extração de informações de PDFs
│ └── maestro.py # Módulo para interagir com o BotCity Maestro
├── main.py # Script principal que executa a automação
└── resources/
├── Telefone.pdf # Arquivo PDF a ser processado
└── telefones_extraidos.xlsx # Resultado da extração
```


## Pré-requisitos

- Python 3.10
- BotCity SDK
- pdfplumber
- pandas
- openpyxl
- python-dotenv

## Configuração

1. **Instalação de Dependências**:

   Execute o seguinte comando para instalar as bibliotecas necessárias:

   ```
   pip install -r requirements.txt
   ```

   ```bash
   pip install botcity pdfplumber pandas openpyxl python-dotenv
   ```
