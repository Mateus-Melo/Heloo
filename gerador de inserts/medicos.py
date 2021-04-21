# encoding: utf-8
nomes = ["'João", "'José", "'Maria", "'Francisco", "'Luiz", "'Luiza"]
sobrenomes1 = [" Silveira", " Cavalcante", " Carvalho", " Lima", " Rocha"," Freitas"]
sobrenomes2 = [" Guimarães'", " Rosa'", " Melo'", " Gomes'", " Lopes'", " Souza'"]

crm1 = ["10","20","30","40","50","60"]
crm2 = ["1","2","3","4","5","6"]
crm3 = ["1","2","3","4","5","6"]
ufs = ["PB'","PE'","BA'","AL'","SE'","CE'","MA'","RN'","PI'"]
especialidades = ["'Cargiologista'","'Reumatologista'", "'Pediatra'", "'Ortopedista'","'Neurologista'","'Dermatologista'"]

telefones = ["'83999999999'","'(81)99999 9999'","'(84)99999-9999'"]

arquivo = open("inserts/medicos.sql","a", encoding='utf-8')

for i in range(6):
    for j in range(6):
        for k in range(6):
            arquivo.write("INSERT INTO MEDICOS(crm, nome, especialidade, telefone)\n")

            insert = "VALUES('CRM" + crm1[i] + crm2[j] + crm3[k] + "/"  + ufs[i*j*k%9] + ","
            
            insert+= nomes[i] + sobrenomes1[j] + sobrenomes2[k] + ","
            insert+= especialidades[i] + ","
            insert+= telefones[i*j*k%3] + ");\n"
            arquivo.write(insert)
arquivo.close()


