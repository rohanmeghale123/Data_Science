create database jan_hybride;
use jan_hybride;

create table employee(id int primary key,name varchar(20),dept_id int);

create table department(dept_id int primary key,name varchar(20),mb_no int);

alter table employee
add foreign key(dept_id) references department(dept_id);

insert into department(dept_id,name,mb_no) values( 1,"mca",123445);

select * from department;

insert into employee(id,name,dept_id) values(11,"Rohan",1);

select * from department;

table department;
table employee;

create table emp(id int primary key,name varchar(20),salary decimal(7,2) default 15000,
age int check(age>18),joinin_date date not null,email varchar(25) unique,
mob_no int, gender char(2),ciry varchar(25));

show tables;
show create table emp;
