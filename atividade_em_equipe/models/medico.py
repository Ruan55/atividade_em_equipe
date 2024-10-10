from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.funcionario import Funcionario

class Medico(Funcionario):

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crm: str) -> None:
       super().__init__(nome, telefone, email, endereco, salario)
       self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,valor):
        self._verificar_crm_tipo_invalido(valor)

        self.crm = valor
        return self.crm
    
    def _verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O crm deve se manter como tipo texto!")

    def __str__(self) -> str:
     return(
             f"\n{super().__str__()}"
             f"\nCrm: {self.crm}"
             )    