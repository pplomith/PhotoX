drop database if exists photoX; 

create database photoX;

use photoX;


create table categoria (

	nome varchar(255), 
    cane varchar(255) default '0', 
    auto varchar(255) default '0', 
    quadro varchar(255) default '0', 
    soleggiato varchar(255) default '0',
    gatto varchar(255) default '0', 
    moto varchar(255) default '0', 
    scultura varchar(255) default '0', 
    coperto varchar(255) default '0', 
    primary key (nome)
); 

create table utente (

	username varchar(255), 
    passwordUtente varchar(255) not null, 
    categoria varchar(255), 
    primary key (username), 
    foreign key (categoria) references categoria (nome)
);