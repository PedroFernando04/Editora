INSERT INTO paises (nome_pais) VALUES
('Afeganistão'),
('África do Sul'),
('Albânia'),
('Alemanha'),
('Andorra'),
('Angola'),
('Antígua e Barbuda'),
('Arábia Saudita'),
('Argélia'),
('Argentina'),
('Armênia'),
('Austrália'),
('Áustria'),
('Azerbaijão'),
('Bahamas'),
('Bangladesh'),
('Barbados'),
('Bahrein'),
('Belarus'),
('Bélgica'),
('Belize'),
('Benin'),
('Butão'),
('Bolívia'),
('Bósnia e Herzegovina'),
('Botsuana'),
('Brasil'),
('Brunei'),
('Bulgária'),
('Burkina Faso'),
('Burundi'),
('Cabo Verde'),
('Camarões'),
('Camboja'),
('Canadá'),
('Catar'),
('Cazaquistão'),
('Chade'),
('Chile'),
('China'),
('Chipre'),
('Colômbia'),
('Comores'),
('Congo'),
('Coreia do Norte'),
('Coreia do Sul'),
('Costa do Marfim'),
('Costa Rica'),
('Croácia'),
('Cuba'),
('Dinamarca'),
('Djibouti'),
('Dominica'),
('Egito'),
('El Salvador'),
('Emirados Árabes Unidos'),
('Equador'),
('Eritreia'),
('Eslováquia'),
('Eslovênia'),
('Espanha'),
('Estados Unidos'),
('Estônia'),
('Etiópia'),
('Fiji'),
('Filipinas'),
('Finlândia'),
('França'),
('Gabão'),
('Gâmbia'),
('Gana'),
('Geórgia'),
('Granada'),
('Grécia'),
('Guatemala'),
('Guiana'),
('Guiné'),
('Guiné-Bissau'),
('Guiné Equatorial'),
('Haiti'),
('Honduras'),
('Hungria'),
('Iémen'),
('Ilhas Marshall'),
('Índia'),
('Indonésia'),
('Irã'),
('Iraque'),
('Irlanda'),
('Islândia'),
('Israel'),
('Itália'),
('Jamaica'),
('Japão'),
('Jordânia'),
('Kiribati'),
('Kosovo'),
('Kuwait'),
('Laos'),
('Lesoto'),
('Letônia'),
('Líbano'),
('Libéria'),
('Líbia'),
('Liechtenstein'),
('Lituânia'),
('Luxemburgo'),
('Macedônia do Norte'),
('Madagascar'),
('Malásia'),
('Malaui'),
('Maldivas'),
('Mali'),
('Malta'),
('Marrocos'),
('Maurícia'),
('Mauritânia'),
('México'),
('Mianmar'),
('Micronésia'),
('Moçambique'),
('Moldávia'),
('Mônaco'),
('Mongólia'),
('Montenegro'),
('Namíbia'),
('Nauru'),
('Nepal'),
('Nicarágua'),
('Níger'),
('Nigéria'),
('Noruega'),
('Nova Zelândia'),
('Omã'),
('Países Baixos'),
('Palau'),
('Panamá'),
('Papua Nova Guiné'),
('Paquistão'),
('Paraguai'),
('Peru'),
('Polônia'),
('Portugal'),
('Quênia'),
('Quirguistão'),
('Reino Unido'),
('República Centro-Africana'),
('República Democrática do Congo'),
('República Dominicana'),
('República Tcheca'),
('Romênia'),
('Ruanda'),
('Rússia'),
('Samoa'),
('San Marino'),
('Santa Lúcia'),
('São Cristóvão e Nevis'),
('São Tomé e Príncipe'),
('São Vicente e Granadinas'),
('Seicheles'),
('Senegal'),
('Serra Leoa'),
('Sérvia'),
('Singapura'),
('Síria'),
('Somália'),
('Sri Lanka'),
('Suazilândia'),
('Sudão'),
('Sudão do Sul'),
('Suécia'),
('Suíça'),
('Suriname'),
('Tailândia'),
('Taiwan'),
('Tajiquistão'),
('Tanzânia'),
('Timor-Leste'),
('Togo'),
('Tonga'),
('Trindade e Tobago'),
('Tunísia'),
('Turcomenistão'),
('Turquia'),
('Tuvalu'),
('Ucrânia'),
('Uganda'),
('Uruguai'),
('Uzbequistão'),
('Vanuatu'),
('Vaticano'),
('Venezuela'),
('Vietnã'),
('Zâmbia'),
('Zimbábue');

INSERT INTO status(nome_status)
VALUES
  ('Lido'),
  ('Lendo'),
  ('Lista de desejos');

INSERT INTO autores(nome_autor, data_nascimento, genero_autor, pais_autor)
VALUES
  ('Affonso Solano', '19811113', 'M', 27),
  ('Agatha Christie', '18900915', 'F', 146),
  ('C.S Lewis', '18981129', 'M', 146),
  ('Josh Malerman', '19750724', 'M', 62),
  ('F. Scott Fitzgerald', '18960924', 'M', 62),
  ('Michael Crichton', '19421023', 'M', 62),
  ('Eduardo Spohr', '19760605', 'M', 27),
  ('Michael Dante DiMartino', '19740718', 'M', 62);

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
  ('Pedro Fernando', 'pedrofernandofb@gmail.com', 'dicria', 'M', 27);

INSERT INTO livros(nome_livro, id_autor_livro, id_editora_livro, data_de_lancamento, id_genero_livro, status_livro, ano_lido, nota, resenha, id_cliente_livro)
VALUES
    ('O Espadachim de Carvão', 1, 1, '20130101', 1, 1, 2024, 9, null, 2),
    ('Caixa de Pássaros', 4, 3, '20150121', 2, 1, 2024, 9, null, 2),
    ('O Curioso Caso de Benjamin Button', 5, 6, '19220527', 3, 1, 2024, 6, null, 2),
    ('O Espadachim de Carvão e a voz do Guardião Cego', 1, 1, '20211020', 1, 1, 2024, 9, null, 2),
    ('Jurassick Park', 6, 4, '19901120', 4, 2, 2024, null, null, 2),
    ('Morte no Nilo', 2, 2, '19371101', 6, 1, 2024, 10, null, 2),
    ('O Santo Guerreiro: Roma Invicta', 7, 7, '20201207', 5, 3, 2024, null, null, 2),
    ('O Leão, a Feiticeira e o Guarda-Roupa', 3, 2, '19501016', 7, 1, 2024, 7, null, 2),
    ('Espadachim de Carvão e as pontes de Puzur', 1, 1, '20150910', 1, 1, 2024, 9, null, 2),
    ('A ascensão de Kyoshi: O passado da poderosa Avatar do Reino da Terra', 8, 8, '20190716', 1, 2, 2024, null, null, 2);
  
  
