drop table if exists comics;
create table comics (
  id integer primary key autoincrement,
  titles varchar(50) not null unique
);

CREATE TABLE if not exists action_comics_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);

CREATE TABLE if not exists batgirl_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists batman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists green_lanterns_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists supergirl_rebirth(
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists superman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists the_flash_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists wonder_woman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists detective_comics_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists nightwing_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists teen_titans_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists trinity_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists deathstroke_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists super_sons_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists doomsday_clock_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists superwoman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists titans_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
