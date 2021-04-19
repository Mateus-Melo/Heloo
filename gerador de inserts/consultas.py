import pandas as pd
import numpy as np

df = pd.read_csv("gerador de inserts\Datas.csv")
datas = list(df.sample(n=100000, replace=True)['Data'])
pacientes = np.random.randint(1, 100001, 100000)
medicos = np.random.randint(1, 217, 100000)
cidades = np.random.randint(1, 10, 100000)
situacoes = np.random.randint(1, 4, 100000)

arquivo = open("inserts/consultas.sql", "a")

for i in range(100000):
    arquivo.write("INSERT INTO CONSULTAS(PACIENTE_ID, MEDICO_ID, DATA_AGENDAMENTO, SITUACAO_ID, CIDADE_ID)\n")
    insert = "VALUES(" + str(pacientes[i]) + ", " + str(medicos[i]) + ", '" + datas[i] + "', " + str(situacoes[i]) + ", " + str(cidades[i]) + ");\n"
    arquivo.write(insert) 

arquivo.close()
    
