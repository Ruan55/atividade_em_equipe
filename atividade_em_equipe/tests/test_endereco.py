import pytest
from atividade_em_equipe.models.endereco import Endereco

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua K", "5", "N/A", "Salvador")
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua K"

def test_mudar_logradouro_valido(endereco_valido):
    endereco_valido.logradouro = "Rua P"
    assert endereco_valido.logradouro == "Rua P"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "5"

def test_mudar_numero_valido(endereco_valido):
    endereco_valido.numero = "6"
    assert endereco_valido.numero == "6"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "N/A"

def test_mudar_complemento_valido(endereco_valido):
    endereco_valido.complemento = "Apt.55"
    assert endereco_valido.complemento == "Apt.55"

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "Salvador"

def test_mudar_cidade_valido(endereco_valido):
    endereco_valido.cidade = "São Paulo"
    assert endereco_valido.cidade == "São Paulo"

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match="O logradouro deve se manter como texto!"):
        Endereco(55 , "5", "N/A", "Salvador")

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O número deve se manter como tipo texto!"):
        Endereco("Rua K", 5, "N/A", "Salvador")

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="O complemento deve se manter como tipo texto!"):
        Endereco("Rua K", "5", 44, "Salvador")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="A cidade deve se manter como texto!"):
        Endereco("Rua K", "5", "N/A", 66)