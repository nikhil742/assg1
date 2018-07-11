'''
#1)
#CREATE DATABASE AND TABLES--->>>
mysql> create database pyf;
Query OK, 1 row affected (0.01 sec)
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
| pyf                |
| sh                 |
| test               |
+--------------------+
6 rows in set (0.10 sec)
mysql> use pyf;
Database changed
mysql> create table BOOK(
    -> BOOK_ID int(5),
    -> Title_ID varchar(55),
    -> location varchar(5),
    -> Author varchar(11));
Query OK, 0 rows affected (0.17 sec)
mysql> show tables;
+---------------+
| Tables_in_pyf |
+---------------+
| book          |
+---------------+
1 row in set (0.00 sec)
mysql> create table TITLE(
    -> title_ID int(5),
    -> publisher_ID int(5),
    -> publisher_year int(10),
    -> publisher_name varchar(10));
Query OK, 0 rows affected (0.18 sec)
mysql> create table PUBLISHERS(
    -> publisher_ID int(5),
    -> name varchar(10),
    -> publisher_Address varchar(15),
    -> Zip_CODE_ID int(10));
Query OK, 0 rows affected (0.18 sec)
mysql> create table ZIP_CODES(
    -> ZIP_ID int(5),
    -> city varchar(25),
    -> State varchar(25),
    -> ZIP_CODE int(10));
Query OK, 0 rows affected (0.17 sec)
mysql> create table AUTHORS_TITLES(
    -> AUTHORS_TITLES_ID int(5),
    -> AUTHORS_ID int(5),
    -> TITLES_ID int(5));
Query OK, 0 rows affected (0.15 sec)
mysql> create table AUTHORS(
    -> AUTHORS_ID int(5),
    -> first_name varchar(15),
    -> Middle_name varchar(15),
    -> Last_name varchar(15));
Query OK, 0 rows affected (0.14 sec)
mysql> show tables;
+----------------+
| Tables_in_pyf  |
+----------------+
| authors        |
| authors_titles |
| book           |
| publishers     |
| title          |
| zip_codes      |
+----------------+
6 rows in set (0.00 sec)
mysql> describe BOOK;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| BOOK_ID  | int(5)      | YES  |     | NULL    |       |
| Title_ID | varchar(55) | YES  |     | NULL    |       |
| location | varchar(5)  | YES  |     | NULL    |       |
| Author   | varchar(11) | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.12 sec)
mysql> describe Title;
+----------------+-------------+------+-----+---------+-------+
| Field          | Type        | Null | Key | Default | Extra |
+----------------+-------------+------+-----+---------+-------+
| title_ID       | int(5)      | YES  |     | NULL    |       |
| publisher_ID   | int(5)      | YES  |     | NULL    |       |
| publisher_year | int(10)     | YES  |     | NULL    |       |
| publisher_name | varchar(10) | YES  |     | NULL    |       |
+----------------+-------------+------+-----+---------+-------+
4 rows in set (0.02 sec)
mysql> describe PUBLISHERS;
+-------------------+-------------+------+-----+---------+-------+
| Field             | Type        | Null | Key | Default | Extra |
+-------------------+-------------+------+-----+---------+-------+
| publisher_ID      | int(5)      | YES  |     | NULL    |       |
| name              | varchar(10) | YES  |     | NULL    |       |
| publisher_Address | varchar(15) | YES  |     | NULL    |       |
| Zip_CODE_ID       | int(10)     | YES  |     | NULL    |       |
+-------------------+-------------+------+-----+---------+-------+
4 rows in set (0.02 sec)
mysql> describe ZIP_CODES;
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| ZIP_ID   | int(5)      | YES  |     | NULL    |       |
| city     | varchar(25) | YES  |     | NULL    |       |
| State    | varchar(25) | YES  |     | NULL    |       |
| ZIP_CODE | int(10)     | YES  |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
4 rows in set (0.03 sec)
mysql> describe AUTHORS;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| AUTHORS_ID  | int(5)      | YES  |     | NULL    |       |
| first_name  | varchar(15) | YES  |     | NULL    |       |
| Middle_name | varchar(15) | YES  |     | NULL    |       |
| Last_name   | varchar(15) | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
4 rows in set (0.09 sec)
mysql> describe AUTHORS_TITLES;
+-------------------+--------+------+-----+---------+-------+
| Field             | Type   | Null | Key | Default | Extra |
+-------------------+--------+------+-----+---------+-------+
| AUTHORS_TITLES_ID | int(5) | YES  |     | NULL    |       |
| AUTHORS_ID        | int(5) | YES  |     | NULL    |       |
| TITLES_ID         | int(5) | YES  |     | NULL    |       |
+-------------------+--------+------+-----+---------+-------+
3 rows in set (0.54 sec)
#2)
INSERT VALUES IN TABLES-->>>>>
mysql> insert into Book (BOOK_ID,Title_ID, location,Author) values(2,5,'abc','sharma')
    -> ;
Query OK, 1 row affected (0.44 sec)
mysql>  insert into Book (BOOK_ID,Title_ID, location,Author) values(1,3,'cba','sharm')
    -> ;
Query OK, 1 row affected (0.28 sec)
mysql> select * from BOOK;
+---------+----------+----------+--------+
| BOOK_ID | Title_ID | location | Author |
+---------+----------+----------+--------+
|       2 | 5        | abc      | sharma |
|       1 | 3        | cba      | sharm  |
+---------+----------+----------+--------+
2 rows in set (0.00 sec)
mysql>  insert into TITLE(title_ID,publisher_ID,publisher_year,publisher_name) values(1,2,1996,'sh');
Query OK, 1 row affected (0.08 sec)
mysql> insert into TITLE(title_ID,publisher_ID,publisher_year,publisher_name) values(2,5,1998,'shar');
Query OK, 1 row affected (0.08 sec)
mysql> select * from TITLE;
+----------+--------------+----------------+----------------+
| title_ID | publisher_ID | publisher_year | publisher_name |
+----------+--------------+----------------+----------------+
|        1 |            2 |           1996 | sh             |
|        2 |            5 |           1998 | shar           |
+----------+--------------+----------------+----------------+
2 rows in set (0.00 sec)
mysql> insert into PUBLISHERs(publisher_ID,name,publisher_Address,ZIP_CODE_ID) values(1,'shubham','#asdfghjkl',55),(2,'sharma','#qwertyuio',44);
Query OK, 2 rows affected (0.07 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> select * from PUBLISHERS;
+--------------+---------+-------------------+-------------+
| publisher_ID | name    | publisher_Address | Zip_CODE_ID |
+--------------+---------+-------------------+-------------+
|            1 | shubham | #asdfghjkl        |          55 |
|            2 | sharma  | #qwertyuio        |          44 |
+--------------+---------+-------------------+-------------+
2 rows in set (0.00 sec)
mysql> insert into ZIP_CODES(ZIP_ID,city,state,ZIP_CODE) values(1,'jagadhri','haryana',5678),(2,'Dheradun','UK',1234);
Query OK, 2 rows affected (0.08 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> select * from ZIP_CODES;
+--------+----------+---------+----------+
| ZIP_ID | city     | State   | ZIP_CODE |
+--------+----------+---------+----------+
|      1 | jagadhri | haryana |     5678 |
|      2 | Dheradun | UK      |     1234 |
+--------+----------+---------+----------+
2 rows in set (0.00 sec)
mysql> insert into AUTHORS_TITLES(AUTHORS_TITLES_ID,AUTHORS_ID,TITLES_ID) values(1,22,55),(2,66,99);
Query OK, 2 rows affected (0.08 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> select * from AUTHORS_TITLES;
+-------------------+------------+-----------+
| AUTHORS_TITLES_ID | AUTHORS_ID | TITLES_ID |
+-------------------+------------+-----------+
|                 1 |         22 |        55 |
|                 2 |         66 |        99 |
+-------------------+------------+-----------+
2 rows in set (0.00 sec)
mysql> insert into AUTHORS(AUTHORS_ID,first_name,Middle_name,Last_name) values(1,'raj','kumar','sharma'),(2,'ravi','kumar','sharma');
Query OK, 2 rows affected (0.07 sec)
Records: 2  Duplicates: 0  Warnings: 0
mysql> select * from AUTHORS;
+------------+------------+-------------+-----------+
| AUTHORS_ID | first_name | Middle_name | Last_name |
+------------+------------+-------------+-----------+
|          1 | raj        | kumar       | sharma    |
|          2 | ravi       | kumar       | sharma    |
+------------+------------+-------------+-----------+
2 rows in set (0.00 sec)
#3)
UPDATES VALUES--->>>>>
mysql> update BOOK SET Author='sharmas' WHERE BOOK_ID=1;
Query OK, 1 row affected (0.08 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> update BOOK SET Author='sharma' WHERE BOOK_ID=2;
Query OK, 1 row affected (0.07 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> select * from BOOK;
+---------+----------+----------+---------+
| BOOK_ID | Title_ID | location | Author  |
+---------+----------+----------+---------+
|       2 | 5        | abc      | sharma  |
|       1 | 3        | cba      | sharmas |
+---------+----------+----------+---------+
2 rows in set (0.00 sec)
mysql> update BOOK SET BOOK_ID=1 WHERE TITLE_ID=5;
Query OK, 1 row affected (0.09 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> update BOOK SET BOOK_ID=2 WHERE TITLE_ID=3;
Query OK, 1 row affected (0.08 sec)
Rows matched: 1  Changed: 1  Warnings: 0
mysql> select * from BOOK;
+---------+----------+----------+---------+
| BOOK_ID | Title_ID | location | Author  |
+---------+----------+----------+---------+
|       1 | 5        | abc      | sharma  |
|       2 | 3        | cba      | sharmas |
+---------+----------+----------+---------+
2 rows in set (0.00 sec)
'''
