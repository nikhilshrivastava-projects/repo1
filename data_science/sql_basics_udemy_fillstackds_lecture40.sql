-- 1 create database
create database testdb;

-- 2 use database
use testdb;

-- 3 create table
create table students(
roll_no int,
name varchar(20),
age int, 
phonenumber int);

-- 4 selecting table
select * from students;

-- 5 insert
insert into students
values(1,'Arya',21,349834934),
(2,'Brandon',19,349834934),
(3,'John',24,349834934),
(4,'Arya',21,349834934);

-- Delete
delete from students where roll_no = 1;

-- Constraints
-- not null
-- unique
-- primary key
-- foreign key
-- 
