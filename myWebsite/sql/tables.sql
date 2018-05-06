drop table if exists comics;
create table comics (
  id integer primary key autoincrement,
  titles varchar(50) not null unique
);
