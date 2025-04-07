CREATE SCHEMA IF NOT EXISTS editora;
set search_path to editora;

drop table if exists editora.livros;
drop table if exists editora.autores;
drop table if exists editora.editoras;
drop table if exists editora.generos;
drop table if exists editora.clientes;
drop table if exists editora.status;
drop table if exists editora.paises;


CREATE TABLE paises(
  id_pais serial primary key,
  nome_pais varchar(200) not null unique
);

CREATE TABLE status(
  id_status serial primary key,
  nome_status varchar(100) not null unique
);

CREATE TABLE autores(
  id_autor serial primary key,
  nome_autor varchar(500) not null,
  data_nascimento_autor date not null,
  genero_autor char(1),
  pais_autor int references paises(id_pais)
);

CREATE TABLE editoras(
  id_editora serial primary key,
  nome_editora varchar(500) not null
);

CREATE TABLE generos(
  id_genero serial primary key,
  nome_genero varchar(500) not null unique
);

CREATE TABLE clientes(
  id_cliente serial primary key,
  nome_cliente varchar(500),
  email_cliente varchar(500),
  senha_cliente varchar(500),
  genero_cliente char(1),
  pais_cliente int references paises(id_pais),
  data_nascimento_cliente date not null,
  adm boolean
);

CREATE TABLE livros(
  id_livro serial primary key,
  nome_livro varchar(500) not null unique,
  id_autor_livro int references autores(id_autor),
  id_editora_livro int references editoras(id_editora),
  data_de_lancamento_livro date,
  id_genero_livro int references generos(id_genero),
  id_status_livro int references status(id_status),
  ano_lido_livro int,
  nota_livro float,
  resenha_livro varchar(1000),
  id_cliente_livro int references clientes(id_cliente)
);


