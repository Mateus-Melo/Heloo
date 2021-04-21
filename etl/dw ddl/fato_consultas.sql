CREATE TABLE fato_consultas (
id BIGSERIAL NOT NULL PRIMARY KEY,
paciente_id BIGINT NOT NULL REFERENCES dim_pacientes(id),
medico_id BIGINT NOT NULL REFERENCES dim_medicos(id),
data_agendamento TIMESTAMP,
situacao_id BIGINT NOT NULL REFERENCES dim_consultas_situacoes(id),
cidade_id BIGINT NOT NULL REFERENCES dim_cidades(id)
)