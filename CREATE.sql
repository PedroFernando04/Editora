CREATE TABLE autores(
  id_autor serial primary key,
  nome_autor varchar(500) not null,
  data_nascimento date not null,
  genero_autor char(1)
);

CREATE TABLE editoras(
  id_editora serial primary key,
  nome_editora varchar(500) not null
);

CREATE TABLE generos(
  id_genero serial primary key,
  nome_genero varchar(500) not null unique
);

CREATE TABLE livros(
  id_livro serial primary key,
  nome_livro varchar(500) not null unique,
  id_autor_livro int references autores(id_autor),
  id_editora_livro int references editoras(id_editora),
  data_de_lancamento date,
  id_genero_livro int references generos(id_genero)
  status_livro varchar(20) 
);
