class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cidade = self._verificar_cidade(cidade)

    def _verificar_logradouro(self,valor):
        self._verificar_logradouro_tipo_invalido(valor)

        self.logradouro = valor
        return self.logradouro

    def _verificar_numero(self,valor):
        self._verificar_numero_tipo_invalido(valor)

        self.numero = valor
        return self.numero
    
    def _verificar_complemento(self,valor):
        self._verificar_complemento_tipo_invalido(valor)

        self.complemento = valor
        return self.complemento
    
    def _verificar_cidade(self,valor):
        self._verificar_cidade_tipo_invalido(valor)

        self.cidade = valor
        return self.cidade
    
    def _verificar_logradouro_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O logradouro deve se manter como texto!")
        
    def _verificar_numero_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O número deve se manter como tipo texto!")
        
    def _verificar_complemento_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O complemento deve se manter como tipo texto!")
        
    def _verificar_cidade_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("A cidade deve se manter como texto!")

    def __str__(self) -> str:
        return(
            f"\nLogradouro: {self.logradouro}"
            f"\nNúmero: {self.numero}"
            f"\nComplemento: {self.complemento}"
            f"\nCidade: {self.cidade}"
        )     

        

        