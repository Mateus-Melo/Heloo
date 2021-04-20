import psycopg2 as pg

creates = ["cidades", "situacoes", "medicos", "pacientes", "consultas"]

conn = pg.connect("dbname = Heloo user=postgres host=localhost password=1234")
cur = conn.cursor()
for i in creates:
    cur.execute(open("ddl/" + i + ".sql","r").read())
    conn.commit()
conn.close()