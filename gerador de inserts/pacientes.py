telefones = ["'83999999999'","'(81)99999 9999'","'(84)99999-9999'"]

arquivo = open("inserts/pacientes.sql","a")

for i in range(100000):
    arquivo.write("INSERT INTO pacientes(nome,telefone)\n")
    insert = "VALUES('Paciente " + str(i) + "'," + telefones[i%3] + ");\n"
    arquivo.write(insert)
arquivo.close()