drop table if exists comics;
create table comics (
  id integer primary key autoincrement,
  titles varchar(50) not null unique
);

drop table if exists wonder_woman_1;
create table wonder_woman_1 (
  id integer primary key autoincrement,
  issue_number integer not null,
  title varchar(100),
  arc varchar(50),
  price float
);

drop table if exists action_comics_1;
create table action_comics_1 (
  id integer primary key autoincrement,
  issue_number integer not null,
  title varchar(100),
  arc varchar(50),
  price float
);

drop table if exists superman_2;
create table superman_2 (
  id integer primary key autoincrement,
  issue_number integer not null,
  title varchar(100),
  arc varchar(50),
  price float
);
