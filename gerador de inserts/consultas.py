import pandas as pd
import numpy as np

df = pd.read_csv("gerador de inserts/Datas.csv")
datas = list(df.sample(n=200000, replace=True)['Data'])
consultas_não_agendadas = df.loc[0:111, ["Data"]]
pacientes = np.random.randint(1, 100001, 200000)
medicos = np.random.randint(1, 217, 200000)
cidades = np.random.choice([1,2,3,4,5,6,7,8,9], 200000, [0.15,0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.12, 0.13])
situacoes = np.random.choice([2,3], 200000, True, [0.75, 0.25])

arquivo = open("inserts/consultas.sql", "a")

for i in range(200000):
    if not(datas[i] in consultas_não_agendadas.values):
        situacoes[i] = 1 
    arquivo.write("INSERT INTO CONSULTAS(PACIENTE_ID, MEDICO_ID, DATA_AGENDAMENTO, SITUACAO_ID, CIDADE_ID)\n")
    insert = "VALUES(" + str(pacientes[i]) + ", " + str(medicos[i]) + ", '" + datas[i] + "', " + str(situacoes[i]) + ", " + str(cidades[i]) + ");\n"
    arquivo.write(insert) 

arquivo.close()
    
