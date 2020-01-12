create table my_table (
    id bigint unsigned not null auto_increment,
    status tinyint unsigned not null default 2,
    events int unsigned not null default 0,
    latitude decimal(10, 8) null,
    longitude decimal(11, 8) null,
    name varchar(50) not null,
    description varchar(128) not null default 'N/A',
    bio text null,
    birthday date null,
    event_time time null,
    created_at datetime not null,
    primary key (id),
    key status (status),
    key birthday_time (birthday, event_time)
)engine=innodb
 default charset=utf8
 default collate=utf8_unicode_ci;
