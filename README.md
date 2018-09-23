This website has two parts. The first part is accessible by the domain name and is used to showcase who I am and some of the projects I am working on.  
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
- SQLite3

## Setup
This would only happen when running on localhost
- initialize the database (only do this once)
~~~ shell
$ python3 init_db.py
~~~

- start the site (localhost)
~~~ shell
$ python3 __init__.py
~~~

## Storage

### Setup
When `init_db.py` is run
- The following tables are created.

  ~~~ sql
  CREATE TABLE Comics (
    comic_id integer primary key autoincrement,
    vol_id integer not null,
    issue_num integer not null,         -- issue number
    title varchar(100),
    arc varchar(50),                    -- story line
    price float,                        -- how much I paid/
    FOREIGN KEY (vol_id) REFERENCES Volumes(vol_id)
  );

  CREATE TABLE Publishers (
    pub_id integer primary key autoincrement,
    pub_name varchar(50) not null unique
  );

  -- could make this into a "information about the volume" kind of thing
  CREATE TABLE Volumes (
    vol_id integer primary key autoincrement,
    pub_id integer not null,
    vol_name varchar(50) not null,
    vol_number varchar(10) not null,
    month_start varchar(3),   -- according to cover date
    year_start integer,
    month_end varchar(7),     -- ongoing
    year_end integer,         -- "" means ongoing
    link varchar(100),        -- link to comicbookdb.com's volume page
    UNIQUE (vol_name, vol_number),
    FOREIGN KEY (pub_id) REFERENCES Publishers(pub_id)
  );

  ~~~

### Adding Entries

#### Publishers
This option adds a publisher into the _Publishers_ table.

#### Volumes
To add a volume into the _Volumes_ table, it's Publisher must already be in the _Publishers_ table as that field is filled by a dropdown of existing publishers.

#### Comics
To add a comic into the _Comics_ table, it's volume must already be in the _Volumes_ table as that field is filled by a dropdown of existing volumes.

### Deleting Comics
Deletes the comic from _Comics_ table based on the id.

# Page Tabs
### Display All
The page displays all the comics in the database.

### Tables
Displays all the volumes in the _Volumes_ table routing to a table of the comics in that volume once clicked.

### Add
Dropdown that allows for comics, volumes, and publishers to be added to the database.

### Search Bar
Was implemented before database schema redesign. Will eventually be added back in.

### Account
Dropdown allowing the user to access account details

#### Export Data
Still testing. Working on being able to send csv's of database info to local computer.
