from typing import *
from dataclasses import dataclass

class DadosBrutoPrevisao(TypedDict):
    cidade: str
    temperatura_celcius: int
    umidade_relativa: int
    condicao_ceu: str
    vento_kmh: int
    
class ProvedorPrevisao(Protocol):
    def obter_dados(self, cidade: str) -> DadosBrutoPrevisao | None: ...

@dataclass(frozen=True)
class Previsao():
    cidade: str
    temperatura_celcius: int
    umidade_relativa: int
    condicao_ceu: str
    vento_kmh: int
    
@dataclass(frozen=True)
class Previsao_bruta():
    dados: DadosBrutoPrevisao
    
    def processar(self) -> Previsao | None:
        if not self.verificar():
            return None
        
        previsao = Previsao(
            cidade = self.dados['cidade'],
            temperatura_celcius = self.dados['temperatura_celcius'],
            umidade_relativa = self.dados['umidade_relativa'],
            condicao_ceu = self.dados['condicao_ceu'],
            vento_kmh = self.dados['vento_kmh']
        )
        
        return previsao
    
    def verificar(self) -> bool:
        if isinstance(self.dados['umidade_relativa'], int) and isinstance(self.dados['temperatura_celcius'], int):
            return True if (
                (0 <= self.dados['umidade_relativa'] <= 100) and
                (self.dados['condicao_ceu'] in ['ensolarado', 'nublado', 'chuvoso'])
            ) else False
        else:
            return False
        
# ------------------------------------------------------------

class ProvedorMeteoNatal():
    def obter_dados(self, cidade: str) -> DadosBrutoPrevisao | None:
        return {
            'cidade': 'Natal',
            'temperatura_celcius': 25,
            'umidade_relativa': 50,
            'condicao_ceu': 'ensolarado',
            'vento_kmh': 10
        }

# ------------------------------------------------------------

def processar_previsao_cidade(provedor: ProvedorPrevisao, cidade: str) -> Previsao | None:
    dados: DadosBrutoPrevisao | None = provedor.obter_dados(cidade)
    
    if dados is None:
        return None
    
    previsao_bruta = Previsao_bruta(dados=dados)
    previsao = previsao_bruta.processar()
    
    return previsao

# ------------------------------------------------------------

def verificar_dia_de_praia(previsao: Previsao) -> bool:
    return True if (
        previsao.condicao_ceu.lower() == 'ensolarado' and
        previsao.temperatura_celcius >= 25 # type: ignore
    ) else False