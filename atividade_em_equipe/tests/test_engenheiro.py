import pytest
from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.engenheiro import Engenheiro

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000, "333")
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "333"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "555"
    assert engenheiro_valido.crea == "555"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="O crea deve se manter como tipo texto!"):
        Engenheiro("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000, 333)