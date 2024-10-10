import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from atividade_em_equipe.models.medico import Medico
from atividade_em_equipe.models.endereco import Endereco
from atividade_em_equipe.models.engenheiro import Engenheiro

os.system("cls || clear")

medico1 = Medico("Marta", "71988008800", "Marta@gmail.com", Endereco("Praça do sol", "123", "E", "Salvador"),1000, "2.000")
engnheiro1 = Engenheiro("Maria", "71988776655", "maria@gmail.com", Endereco("Praça da revolução", "122", "L", "Salvador"), 5000, "1,000")

print(engnheiro1)
print(medico1)