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

CREATE TABLE if not exists rebirth_dc_universe_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);

CREATE TABLE if not exists rebirth_superman_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);

CREATE TABLE if not exists rebirth_batman_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_wonder_woman_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_aquaman_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_green_arrow_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_the_flash_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_green_lanterns_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_titans_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_supergirl_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_teen_titans_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_justice_league_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_nightwing_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_batgirl_and_the_birds_of_prey_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists rebirth_batman_beyond_rebirth_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists dc_essential_graphic_novels_2017_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists annual_batgirl_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists annual_batman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists annual_wonder_woman_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists annual_supergirl_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists annual_the_flash_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists action_comics_special_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
CREATE TABLE if not exists superman_special_rebirth (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
