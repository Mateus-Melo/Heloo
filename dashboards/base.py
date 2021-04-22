import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://postgres:1234@localhost:5432/DW_Heloo')

consultas = pd.read_sql_table("fato_consultas", engine)
cidades = pd.read_sql_table("dim_cidades", engine)
pacientes = pd.read_sql_table("dim_pacientes", engine)
medicos = pd.read_sql_table("dim_medicos", engine)
situacoes = pd.read_sql_table("dim_situacoes", engine)

cidades = cidades.rename(columns = {"nome" : "cidade", "id" : "cidade_id"})
pacientes = pacientes.rename(columns = {"nome" : "paciente", "telefone" : "telefone paciente", "id" : "paciente_id"})
medicos = medicos.rename(columns = {"nome" : "médico", "telefone" : "telefone médico", "id" : "medico_id"})
situacoes = situacoes.rename(columns = {"nome" : "situação", "id" : "situacao_id"})

base = pd.merge(consultas, cidades)
base = pd.merge(base, medicos)
base = pd.merge(base, pacientes)
base = pd.merge(base, situacoes)

base.to_csv("dashboards/base-consultas.csv", sep = ";", index=False)
