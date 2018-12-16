create table users (
    user_id int unsigned not null auto_increment,
    name varchar(128) not null,
    primary key (user_id)
)engine=innodb default charset utf8 collate utf8_unicode_ci;

create table lists (
    list_id int unsigned not null auto_increment,
    user_id int unsigned not null,
    name varchar(128) not null,
    created_at datetime not null,
    primary key (list_id)
)engine=innodb default charset utf8 collate utf8_unicode_ci;

create table list_items (
    list_item_id int unsigned not null auto_increment,
    list_id int unsigned not null,
    is_done tinyint unsigned not null,
    content text not null,
    created_at datetime not null,
    primary key (list_item_id)
)engine=innodb default charset utf8 collate utf8_unicode_ci;
