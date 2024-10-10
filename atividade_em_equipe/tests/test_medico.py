import pytest
from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.medico import Medico

@pytest.fixture
def medico_valido():
    medico = Medico("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000, "444")
    return medico

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "444"

def test_mudar_crm_valido(medico_valido):
    medico_valido.crm = "555"
    assert medico_valido.crm == "555"

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match="O crm deve se manter como tipo texto!"):
        Medico("Ruan", "3333-4444", "Ruan32232@gmail.com", Endereco("Rua K", "5", "N/A", "Salvador"), 3000, 444)