drop table if exists comics;
create table comics (
  id integer primary key autoincrement,
  issue_name varchar(30) not null,
  issue_number integer not null,
  title varchar(50),
  price float,
  volume varchar(20),
  arc varchar(30) not null
);
