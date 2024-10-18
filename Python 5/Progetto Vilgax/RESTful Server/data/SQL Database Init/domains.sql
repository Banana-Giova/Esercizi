create type Voto as 
	enum('1', '2', '3', '4', '5');

create type Paprika as 
  enum('con', 'senza');

create domain PosInteger as integer check (value >= 0);

create domain StringaM as varchar(100);

-------------------------------------

create table Recensioni (
  cf StringaM not null,
  descrizione StringaM not null,
  voto Voto not null,
  primary key (cf)  
);

create table Vittime (
  id StringaM not null,
  nome StringaM not null,
  cognome StringaM not null,
  paprika Paprika not null,
  primary key (id)  
);

create table Preghiere (
  proprietario StringaM not null,
  titolo StringaM not null,
  contenuto StringaM not null,
  data PosInteger not null,
  primary key (titolo),
  foreign key (proprietario) references Vittime(id)
);