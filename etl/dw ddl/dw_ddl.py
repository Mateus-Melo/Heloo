import psycopg2 as pg

creates = ["dim_cidades", "dim_situacoes", "dim_medicos", "dim_pacientes", "fato_consultas"]

conn = pg.connect("dbname = DW_Heloo user=postgres host=localhost password=1234")
cur = conn.cursor()
for i in creates:
    cur.execute(open("etl/dw ddl/" + i + ".sql","r").read())
    conn.commit()
conn.close()