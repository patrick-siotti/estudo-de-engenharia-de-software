from .core import ProvedorMeteoNatal, processar_previsao_cidade, verificar_dia_de_praia

def main() -> None:
    provedor = ProvedorMeteoNatal()
    previsao = processar_previsao_cidade(provedor, 'Natal')
    if previsao is None:
        print('Não foi possível obter a previsão para a cidade de Natal')
        return
    
    print(f'A previsão para a cidade de {previsao.cidade} é de {previsao.temperatura_celcius}°C, {previsao.umidade_relativa}% de umidade e {previsao.condicao_ceu} com vento de {previsao.vento_kmh} km/h')
    if verificar_dia_de_praia(previsao):
        print('É um dia de praia!')
    else:
        print('Não é um dia de praia!')

if __name__ == '__main__':
    main()