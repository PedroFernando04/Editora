INSERT INTO autores(nome_autor, data_nascimento, genero_autor)
VALUES
  ('Affonso Solano', '19811113', 'M'),
  ('Agatha Christie', '18900915', 'F'),
  ('C.S Lewis', '18981129', 'M'),
  ('Josh Malerman', '19750724', 'M'),
  ('F. Scott Fitzgerald', '18960924', 'M'),
  ('Michael Crichton', '19421023', 'M'),
  ('Eduardo Spohr', '19760605', 'M'),
  ('Michael Dante DiMartino', '19740718', 'M');

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

INSERT INTO livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento, id_genero_livro, status_livro, ano_lido)
VALUES
    ('O Espadachim de Carvão', 1, 1, '20130101', 1, 'Lido', 2024),
    ('Caixa de Pássaros', 4, 3, '20150121', 2, 'Lido', 2024)),
    ('O Curioso Caso de Benjamin Button', 5, 6, '19220527', 3, 'Lido', 2024)),
    ('O Espadachim de Carvão e a voz do Guardião Cego', 1, 1, '20211020', 1, 'Lido', 2024)),
    ('Jurassick Park', 6, 4, '19901120', 4, 'Lido', 2024)),
    ('Morte no Nilo', 2, 2, '19371101', 6, 'Lido', 2024)),
    ('O Santo Guerreiro: Roma Invicta', 7, 7, '20201207', 5, 'Lido', 2024))
    ('O Leão, a Feiticeira e o Guarda-Roupa', 3, 2, '19501016', 7, 'Lido', 2024)),
    ('Espadachim de Carvão e as pontes de Puzur', 1, 1, '20150910', 1, 'Lido', 2024)),
    ('A ascensão de Kyoshi: O passado da poderosa Avatar do Reino da Terra', 8, 8, '20190716', 1, 'Lido', 2024));
  
  
