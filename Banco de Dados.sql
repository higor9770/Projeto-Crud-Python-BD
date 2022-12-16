CREATE DATABASE crud_python;

USE crud_python;

CREATE TABLE IF NOT EXISTS funcionarios (
	nome VARCHAR (80) NOT NULL,
    CPF VARCHAR (14) NOT NULL PRIMARY KEY,
    telefone VARCHAR (14) NOT NULL UNIQUE, -- Exemplo: (81) 995481296
    salario DECIMAL (7,2) NOT NULL,
    endereco VARCHAR (45) NOT NULL
);
drop table tec_administrativo;
CREATE TABLE IF NOT EXISTS tec_administrativo (
	id_tec_administrativo TINYINT AUTO_INCREMENT PRIMARY KEY,
    setor VARCHAR (30) NOT NULL
);

CREATE TABLE IF NOT EXISTS professor (
	id_professor TINYINT AUTO_INCREMENT PRIMARY KEY,
    titulacao VARCHAR (60) NOT NULL,
    area_formacao VARCHAR (60) NOT NULL
);

drop table aluno;
CREATE TABLE IF NOT EXISTS aluno (
	nome VARCHAR (80) NOT NULL, 
    matricula varchar(6), -- o auto incremento de matricula deu erro para executar 
    CPF VARCHAR (14) NOT NULL PRIMARY KEY
);

drop table curso;
CREATE TABLE IF NOT EXISTS curso (
	id_curso TINYINT AUTO_INCREMENT PRIMARY KEY,
    nomeCurso VARCHAR (60) NOT NULL,
    duracao INT (04) NOT NULL
);

drop table disciplina;
CREATE TABLE IF NOT EXISTS disciplina (
	id_disciplina TINYINT AUTO_INCREMENT PRIMARY KEY,
    nomeDisciplina VARCHAR (60) NOT NULL, 
    carga_horaria int (04) NOT NULL
);

select * from aluno;
select * from curso;
select * from disciplina;
select * from funcionarios;
select * from professor;
select * from tec_administrativo;