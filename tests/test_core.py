import pytest
from projeto_previsao.core import ( # type: ignore
    Previsao, 
    ProvedorPrevisao,
    verificar_dia_de_praia,
    processar_previsao_cidade,
)

@pytest.fixture
def previsao_dia_de_praia_positivo() -> Previsao:
    return Previsao(
        cidade = 'Natal',
        temperatura_celcius = 25,
        umidade_relativa = 50,
        condicao_ceu = 'ensolarado',
        vento_kmh = 10
    )

@pytest.fixture
def previsao_dia_de_praia_negativo() -> Previsao:
    return Previsao(
        cidade = 'Natal',
        temperatura_celcius = 15,
        umidade_relativa = 80,
        condicao_ceu = 'nublado',
        vento_kmh = 5
    )
    
@pytest.fixture
def provedor_de_previsao_cidade_existente_mock(mocker):
    dados_falsos = {
        'cidade': 'Natal', 'temperatura_celcius': 30, 'umidade_relativa': 60,
        'condicao_ceu': 'ensolarado', 'vento_kmh': 15
    }
    
    mock = mocker.Mock(spec=ProvedorPrevisao)
    mock.obter_dados.return_value = dados_falsos
    return mock

@pytest.fixture
def provedor_de_previsao_cidade_inexistente_mock(mocker):
    mock = mocker.Mock(spec=ProvedorPrevisao)
    mock.obter_dados.return_value = None
    return mock

def test_processar_previsao_cidade_existente(provedor_de_previsao_cidade_existente_mock: ProvedorPrevisao):
    previsao = processar_previsao_cidade(provedor_de_previsao_cidade_existente_mock, 'Natal')
    assert previsao.cidade == 'Natal'
    assert previsao.temperatura_celcius == 30
    assert previsao.umidade_relativa == 60
    assert previsao.condicao_ceu == 'ensolarado'
    assert previsao.vento_kmh == 15

def test_processar_previsao_cidade_inexistente(provedor_de_previsao_cidade_inexistente_mock: ProvedorPrevisao):
    previsao = processar_previsao_cidade(provedor_de_previsao_cidade_inexistente_mock, 'Sao Paulo')
    assert previsao is None

def test_verificar_dia_de_praia_positivo(previsao_dia_de_praia_positivo: Previsao):
    assert verificar_dia_de_praia(previsao_dia_de_praia_positivo) is True

def test_verificar_dia_de_praia_negativo(previsao_dia_de_praia_negativo: Previsao):
    assert verificar_dia_de_praia(previsao_dia_de_praia_negativo) is False