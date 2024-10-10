from abc import ABC,abstractmethod
from models.endereco import Endereco

class Funcionario(ABC):

    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, salario: float) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.salario = salario

    @abstractmethod
    def salarioFinal(self) -> float:
        pass

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nEndereço: {self.endereco}"
            f"\nSalário: {self.salario}"
            f"\nSalario final: {self.salarioFinal()}"
            )     
        
