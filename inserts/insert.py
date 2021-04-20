import psycopg2 as pg

inserts = ["cidades", "situacoes", "medicos", "pacientes", "consultas"]

conn = pg.connect("dbname = Heloo user=postgres host=localhost password=1234")
cur = conn.cursor()
for i in inserts:
    cur.execute(open("inserts/" + i + ".sql","r").read())
    conn.commit()
conn.close()