CREATE TABLE consultas (
id BIGSERIAL NOT NULL PRIMARY KEY,
paciente_id BIGINT NOT NULL REFERENCES pacientes(id),
medico_id BIGINT NOT NULL REFERENCES medicos(id),
data_agendamento TIMESTAMP,
situacao_id BIGINT NOT NULL REFERENCES consultas_situacoes(id),
cidade_id BIGINT NOT NULL REFERENCES cidades(id)
)