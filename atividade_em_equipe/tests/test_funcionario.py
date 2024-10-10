import pytest
from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.funcionario import Funcionario

@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000)
    return funcionario

def test_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 3000

def test_mudar_salario_valido(funcionario_valido):
    funcionario_valido.salario = 6000
    assert funcionario_valido.salario == 6000

def test_nome_valido(funcionario_valido):
    assert funcionario_valido.nome == "Ruan"

def test_mudar_nome_valido(funcionario_valido):
    funcionario_valido.nome = "Cauly"
    assert funcionario_valido.nome == "Cauly"

def test_numero_valido(funcionario_valido):
    assert funcionario_valido.telefone == "3333-4444"

def test_mudar_numero_valido(funcionario_valido):
    funcionario_valido.telefone = "4444-3333"
    assert funcionario_valido.telefone == "4444-3333"

def test_email_valido(funcionario_valido):
    assert funcionario_valido.email == "Ruan32232@gmail.com"

def test_mudar_email_valido(funcionario_valido):
    funcionario_valido.email = "Cauly8@gmail.com"
    assert funcionario_valido.email == "Cauly8@gmail.com"

def test_salario_negativo():
    with pytest.raises(ValueError, match="O salário não pode ser negativo!"):
        Funcionario("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), -3000)

def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="O salário deve se manter como número!"):
        Funcionario("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), "3000")

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="O nome deve se manter como um texto!"):
        Funcionario(55, "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000)

def test_nome_vazio():
    with pytest.raises(TypeError, match="O nome não pode estar vazio!"):
        Funcionario("", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="O telefone deve se manter como tipo texto!"):
        Funcionario("Ruan", 33334444, "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000)

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="O email deve se manter como texto!"):
        Funcionario("Ruan", "3333-4444", 55, Endereco("Rua K", "5", "N/A", "Salvador"), 3000)