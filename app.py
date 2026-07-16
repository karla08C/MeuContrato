from src.excel import carregar_funcionarios


def main():
    try:
        funcionarios = carregar_funcionarios("data/funcionarios.xlsx")

        print("=" * 50)
        print("FUNCIONÁRIOS CADASTRADOS")
        print("=" * 50)
        print(funcionarios)

    except FileNotFoundError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()