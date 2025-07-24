from os import system

commands: list[str] = [
    'cls',
    'poetry run python -m projeto_previsao'
]

if __name__ == "__main__":
    for command in commands:
        system(command)