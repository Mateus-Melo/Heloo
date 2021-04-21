import pandas as pd
import psycopg2 as pg
from sqlalchemy import create_engine

def remove_duplicatas(df):
    return df.drop_duplicates()

def trata_telefones(telefones):
    return telefones.str.replace("[ ,(,),-]","", regex=True)

conn = pg.connect("dbname = Heloo user=postgres host=localhost password=1234")
situacoes = pd.read_sql_query('select * from consultas_situacoes',con=conn)
cidades = pd.read_sql_query('select * from cidades',con=conn)
medicos = pd.read_sql_query('select * from medicos',con=conn)
pacientes = pd.read_sql_query('select * from pacientes',con=conn)
consultas = pd.read_sql_query('select * from consultas',con=conn)
conn.close()

engine = create_engine('postgresql://postgres:1234@localhost:5432/DW_Heloo')

# Cidades

populacao_cidades = pd.read_excel("etl/Lista-de-Municípios-com-IBGE-Brasil.xlsx")[["Município", "População"]]
cidades = remove_duplicatas(cidades)
cidades = pd.merge(cidades, populacao_cidades,"left", left_on = "nome", right_on = "Município")
cidades["População"] = cidades["População"].astype("int")
cidades.to_sql("dim_cidades", engine, if_exists = "replace")

# Pacientes

telefones = pacientes["telefone"]
pacientes["telefone"] = trata_telefones(telefones)
pacientes = remove_duplicatas(pacientes)
pacientes.to_sql("dim_pacientes", engine, if_exists = "replace")

# Médicos

telefones = medicos["telefone"]
medicos["telefone"] = trata_telefones(telefones)
medicos = remove_duplicatas(medicos)
medicos.to_sql("dim_medicos", engine, if_exists = "replace")

# Consultas Situações

situacoes = remove_duplicatas(situacoes)
situacoes.to_sql("dim_situacoes", engine, if_exists = "replace")

# Consultas

consultas = remove_duplicatas(consultas)
consultas.to_sql("fato_consultas", engine, if_exists = "replace")






