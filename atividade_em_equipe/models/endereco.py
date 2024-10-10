class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cidade: str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCidade: {self.cidade}"
        )     

        

        