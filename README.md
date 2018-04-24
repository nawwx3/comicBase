This website has two parts. The first part is accessible by the domain name (which is currently not connected to the IP for reasons I don't understand / have not been able to fix) and is used to showcase who I am and some of the projects I have developed.  
The second part of this website is a comic book database that I have developed myself.

# nathanwelch.me (part 1)



# comicBase (part 2)



append '/comicBase' to the end of the domain to access this  
eventually there will be a "playground" setting so other users can look at it.

## Info
comicBase is a comic book database I have developed to cut down on the number of same issues I am buying while in store. Also because it I thought it would be fun to make. It is running on an Amazon lightsail instance running Ubuntu 16.04.  
I am using these to run comicBase:
- Apache
- Flask
- sqlite3

## Setup
- initialize the database (only do this once)
~~~ shell
$ python3 init_db.py
~~~

- start the site
~~~ shell
$ python3 __init__.py
~~~

## Storage
This explains how the database is setup.  
When `init_db.py` is run it makes this table:

~~~ sql
CREATE TABLE comics (
  id integer primary key autoincrement,
  titles varchar(50) not null unique
);
~~~

Then when comics are added using the "Add Comics" page on the navbar, first the issue_name and the volume are pushed together to make a table name. This table is then created using this format:

~~~ sql
CREATE TABLE if not exists table_title (
    id integer primary key autoincrement,
    issue_number varchar(5) not null,
    title varchar(100),
    arc varchar(50),
    price float
);
~~~

As is show, if there is no table of that name it will be created. This also is unique to each comic_title, volume pair as each comic in that volume will create the same title name.  

This "table_title" is then added into the previously mentioned "comics" table.
