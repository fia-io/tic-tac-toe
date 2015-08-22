DROP TABLE IF EXISTS games;

CREATE TABLE games (
  id int not null AUTO_INCREMENT,
  player1 varchar(9),
  player2 varchar(9),
  state char(9),
  PRIMARY KEY (id)
);

INSERT INTO games (player1, player2, state)
VALUES ('mb', 'Thorson', 'XXXXXXXOX');
