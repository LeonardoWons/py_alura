from fila_base import FilaBase
from constantes import FILA_PRIORITARIA


class FilaPrioritaria(FilaBase):

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'{FILA_PRIORITARIA}{self.codigo}'
        
    def chama_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return f'Cliente atual: {cliente_atual}, dirija-se ao caixa {caixa}'

    def estatistica(self, dia, agencia, retorna_estatistica) -> dict:
        estatistica = retorna_estatistica(dia, agencia)
        
        return estatistica.roda_estatistica(self.clientes_atendidos)
