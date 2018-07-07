drop table if exists comics;
create table comics (
  id integer primary key autoincrement,
  titles varchar(50) not null unique
);

CREATE TABLE if not exists Action_Comics_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);

CREATE TABLE if not exists Batgirl_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Batman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Green_Lanterns_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Supergirl_Rebirth(
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Superman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists The_Flash_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Wonder_Woman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Detective_Comics_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Nightwing_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Teen_Titans_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Trinity_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Deathstroke_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Super_Sons_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Doomsday_Clock_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Superwoman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Titans_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Annual_Batman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Annual_Supergirl_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Annual_Wonder_Woman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Annual_Batgirl_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Annual_The_Flash_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Special_Superman_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists Special_Action_Comics_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists DC_Universe_Rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
