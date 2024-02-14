use futbol;
CREATE TABLE results(
   id_result   INT AUTO_INCREMENT PRIMARY KEY
  ,id_shootout int not null
  ,id_scorers int not null
  ,dates      DATE  NOT NULL
  ,home_team  VARCHAR(32) NOT NULL
  ,away_team  VARCHAR(32) NOT NULL
  ,home_score INTEGER  NOT NULL
  ,away_score INTEGER  NOT NULL
  ,tournament VARCHAR(45) NOT NULL
  ,city       VARCHAR(28) NOT NULL
  ,country    VARCHAR(32) NOT NULL
  ,neutral    VARCHAR(5) NOT NULL
  ,constraint FK_scorers foreign key (id_scorers) references scorers (id_scorers),
   constraint FK_shootout foreign key (id_shootout) references shootout (id_shootout)
);

CREATE TABLE shootout(
 id_shootout INT AUTO_INCREMENT PRIMARY KEY
 ,dates     DATE NOT NULL 
  ,home_team VARCHAR(24) NOT NULL
  ,away_team VARCHAR(23) NOT NULL
  ,winner    VARCHAR(24) NOT NULL
);

CREATE TABLE scorers(
   id_scorers INT AUTO_INCREMENT PRIMARY KEY
  ,dates      DATE  NOT NULL
  ,home_team VARCHAR(32) NOT NULL
  ,away_team VARCHAR(32) NOT NULL
  ,team      VARCHAR(32) NOT NULL
  ,scorer    VARCHAR(38) NOT NULL
  ,minutes    VARCHAR(3) NOT NULL
  ,own_goal  VARCHAR(5) NOT NULL
  ,penalty   VARCHAR(5) NOT NULL
);
