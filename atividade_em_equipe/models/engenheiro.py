from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.funcionario import Funcionario

class Engenheiro(Funcionario):

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crea: str) -> None:
       super().__init__(nome, telefone, email, endereco, salario)
       self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)

        self.crea = valor
        return self.crea

    def _verificar_crea_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crea deve se manter como tipo texto!")   

    def __str__(self) -> str:
        return(
             f"\n{super().__str__()}"
             f"\nCrea: {self.crea}"
             )    