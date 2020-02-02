create table posts (
    post_id bigint unsigned not null auto_increment,
    title varchar(128) not null,
    content text not null,
    likes int unsigned not null default 0,
    primary key (post_id)
)engine=innodb
 default charset=utf8
 default collate=utf8_unicode_ci;

create table likes (
    like_id bigint unsigned not null auto_increment,
    post_id bigint unsigned not null,
    user_id bigint unsigned not null,
    primary key (like_id),
    key post_id (post_id),
    key user_id (user_id)
)engine=innodb
 default charset=utf8
 default collate=utf8_unicode_ci;
