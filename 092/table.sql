create table people (
    person_id bigint unsigned not null auto_increment,
    name varchar(64) not null,
    age int not null,
    country varchar(32) not null,
    joined date not null,
    primary key (person_id)
)engine=innodb
 default charset=utf8
 default collate=utf8_unicode_ci;
