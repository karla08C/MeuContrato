# 📄 MeuContrato — Automação de Geração de Contratos

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> Solução em Python desenvolvida para automatizar a leitura de bases de dados em Excel e a geração padronizada de contratos de trabalho em formato DOCX e PDF.

---

## 🎯 Contexto e Problema Resolvido

Em rotinas de Departamento Pessoal, Recursos Humanos e Administrativo, o preenchimento manual de múltiplos contratos de trabalho a partir de planilhas gera gargalos operacionais e alto risco de erros de digitação.

O **MeuContrato** automatiza esse fluxo de ponta a ponta: lê a base estruturada de colaboradores (`.xlsx`), valida a existência dos arquivos, processa os registros via `Pandas` e prepara os documentos finais com agilidade e confiabilidade.

---

## ✨ Funcionalidades

- 📊 **Ingestão de Dados em Lote:** Leitura e validação de planilhas Excel (`data/funcionarios.xlsx`) utilizando `pandas` e `openpyxl`.
- 📝 **Geração Automatizada de Documentos:** Preenchimento dinâmico de minutas contratuais via `python-docx`.
- 📑 **Exportação para PDF:** Conversão direta de documentos gerados com `docx2pdf`.
- 📂 **Arquitetura Modular:** Separação clara entre dados de entrada, modelos (templates), código-fonte e documentos gerados.

---

## 🗂️ Estrutura do Projeto

```text
MeuContrato/
├── data/               # Planilhas de entrada (ex: funcionarios.xlsx)
├── templates/          # Modelos de contrato (.docx) com variáveis
├── output/             # Contratos finais gerados (DOCX / PDF)
├── logs/               # Registros de execução e auditoria
├── src/                # Módulos internos de processamento
│   └── excel.py        # Funções de leitura e validação de planilhas
├── app.py              # Ponto de entrada principal da aplicação
├── requirements.txt    # Dependências do projeto (UTF-8)
└── README.md           # Documentação do projeto
```

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Manipulação de Dados:** Pandas, NumPy, OpenPyXL
- **Automação de Documentos:** python-docx, docx2pdf, lxml
- **Utilitários:** tqdm (barra de progresso), colorama

---

## 🚀 Como Executar Localmente

### 1. Clone o repositório
```bash
git clone https://github.com/karla08C/MeuContrato.git
cd MeuContrato
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv

# No Windows (PowerShell):
.\.venv\Scripts\Activate.ps1

# No Linux/macOS:
source .venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute a aplicação
Certifique-se de que a planilha `data/funcionarios.xlsx` esteja na pasta `data/` e execute:
```bash
python app.py
```

---

## 👩‍💻 Autora

Desenvolvido por **Karla Castro** — conectando gestão de processos administrativos e engenharia de software.
- [LinkedIn](https://www.linkedin.com/in/karlaj-castro/)
- [GitHub](https://github.com/karla08C)