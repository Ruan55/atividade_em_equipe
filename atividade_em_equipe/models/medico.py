from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.funcionario import Funcionario

class Medico(Funcionario):
    BONIFICACAO = 2.0

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float, crm: str) -> None:
       super().__init__(nome, telefone, email, endereco, salario)
       self.crm = crm

    def salarioFinal(self) -> float:
        resultado = self.salario * self.BONIFICACAO
        return resultado   

    def __str__(self) -> str:
     return(
             f"\n{super().__str__()}"
             f"\nCrm: {self.crm}"
             )    