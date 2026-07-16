from pathlib import Path
import pandas as pd


def carregar_funcionarios(caminho_arquivo: str) -> pd.DataFrame:
    """
    Lê a planilha de funcionários e retorna um DataFrame.
    """
    caminho = Path(caminho_arquivo)

    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    return pd.read_excel(caminho)