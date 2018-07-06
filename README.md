This website has two parts. The first part is accessible by the domain name (which is currently not connected to the IP for reasons I don't understand / have not been able to fix) and is used to showcase who I am and some of the projects I have developed.  
The second part of this website is a comic book database that I have developed myself.

# nathanwelch.me (part 1)



# comicBase (part 2)



Append '/comicBase' to the end of the domain to access this  
Eventually there will be a "playground" setting so other users can look at it.

## Info
comicBase is a comic book database I have developed to cut down on the number of same issues I am buying while in store. Also because it I thought it would be fun to make. It is running on an Amazon lightsail instance running Ubuntu 16.04.  
I am using these to run comicBase:
- Apache
- Flask
- sqlite3

## Setup
This would only happen when running on localhost
- initialize the database (only do this once)
~~~ shell
$ python3 init_db.py
~~~

- start the site
~~~ shell
$ python3 __init__.py
~~~

## Storage

### Setup
When `init_db.py` is run
- The following table is created (comes from "sql/tables.py"):

  ~~~ sql
  CREATE TABLE comics (
    id integer primary key autoincrement,
    titles varchar(50) not null unique
  );
  ~~~
- Any entries in the "sql/entries.py" file are added

### Inserting Comics
When comics are added using the "Add" page on the navbar, first the issue_name and the volume are pushed together to make a table name. This table is then created using this format:

~~~ sql
CREATE TABLE if not exists issue_name_volume (
    id integer primary key autoincrement,
    issue_number integer not null,
    title varchar(100),
    arc varchar(50),
    price float
);
~~~

As is shown, if there is no table of that name it will be created. This also is unique to each issue_name, volume pair as each comic in that volume will create the same title name.  

This "issue_name_volume" title is then added into the previously mentioned "comics" table.

### Deleting Comics
When a comic is deleted, it first deletes the comic from it's assigned table. Then it checks to make sure the table it was deleted from is not empty. If it's not empty then it continues on. If it is empty, it drops the table then deletes the entry from the "comics" table.


# Page Tabs
### Display All
The page displays all the comics in the database. It starts off the top of the "comics" table printing the info from each table grabbed and moves onto the next one till it reaches the bottom if the "comics" table.

### Add
This page pulls up an input form that then adds the info into the database.

Form checking will be added.


### Search Bar
First version of this had form checking. Now it is just an input box.
Searches through all info and finds like terms in any of the table entries.



# end
