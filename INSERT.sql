INSERT INTO autores(nome_autor, data_nascimento, genero_autor, pais)
VALUES
  ('Affonso Solano', '19811113', 'M', 'Brasil'),
  ('Agatha Christie', '18900915', 'F', 'Inglaterra'),
  ('C.S Lewis', '18981129', 'M', 'Inglaterra'),
  ('Josh Malerman', '19750724', 'M', 'Estados Unidos'),
  ('F. Scott Fitzgerald', '18960924', 'M', 'Estados Unidos'),
  ('Michael Crichton', '19421023', 'M', 'Estados Unidos'),
  ('Eduardo Spohr', '19760605', 'M', 'Brasil'),
  ('Michael Dante DiMartino', '19740718', 'M', 'Estados Unidos');

INSERT INTO generos(nome_genero)
VALUES
  ('Ação e Aventura'),
  ('Suspense'),
  ('Conto'),
  ('Ficção Científica'),
  ('Ficção Histórica'),
  ('Mistério'),
  ('Fantasia'),
  ('Comédia');

INSERT INTO editoras(nome_editora)
VALUES
    ('LeYa'),
    ('HarperCollins'),
    ('Intrínseca'),
    ('Editora Aleph'),
    ('Talentos da Literatura Brasileira'),
    ('Crowell-Collier Publishing Company'),
    ('Verus'),
    ('Planeta');

INSERT INTO clientes(nome_cliente, email_cliente, senha_cliente, genero_cliente, pais_cliente)
VALUES
  ('Admin', 'admin', 'admin', null, null),
  ('Pedro Fernando', 'pedrofernandofb@gmail.com', 'dicria', 'M', 'Brasil')

INSERT INTO livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento, id_genero_livro, status_livro, ano_lido, nota, resenha, id_cliente_livro)
VALUES
    ('O Espadachim de Carvão', 1, 1, '20130101', 1, 'Lido', 2024, 9, null, 2),
    ('Caixa de Pássaros', 4, 3, '20150121', 2, 'Lido', 2024, 9, null, 2),
    ('O Curioso Caso de Benjamin Button', 5, 6, '19220527', 3, 'Lido', 2024, 6, null, 2),
    ('O Espadachim de Carvão e a voz do Guardião Cego', 1, 1, '20211020', 1, 'Lido', 2024, 9, null, 2),
    ('Jurassick Park', 6, 4, '19901120', 4, 'Em leitura', 2024, null, null, 2),
    ('Morte no Nilo', 2, 2, '19371101', 6, 'Lido', 2024, 10, null, 2),
    ('O Santo Guerreiro: Roma Invicta', 7, 7, '20201207', 5, 'Na fila', 2024, null, null, 2),
    ('O Leão, a Feiticeira e o Guarda-Roupa', 3, 2, '19501016', 7, 'Lido', 2024, 7, null, 2),
    ('Espadachim de Carvão e as pontes de Puzur', 1, 1, '20150910', 1, 'Lido', 2024, 9, null, 2),
    ('A ascensão de Kyoshi: O passado da poderosa Avatar do Reino da Terra', 8, 8, '20190716', 1, 'Em leitura', 2024, null, null, 2);
  
  
