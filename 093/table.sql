create table posts (
    post_id bigint unsigned not null auto_increment,
    title varchar(128) not null,
    content text not null,
    primary key (post_id)
)engine=innodb
 default charset=utf8
 default collate=utf8_unicode_ci;

 create table comments (
     comment_id bigint unsigned not null auto_increment,
     post_id bigint unsigned not null,
     content text not null,
     primary key (comment_id),
     key post_id (post_id)
 )engine=innodb
  default charset=utf8
  default collate=utf8_unicode_ci;

insert into posts values (1, 'post 1', 'content 1');
insert into posts values (2, 'post 2', 'content 2');
insert into posts values (3, 'post 3', 'content 3');
insert into posts values (4, 'post 4', 'content 4');

insert into comments values (default, 1, 'post 1 comment 1');
insert into comments values (default, 1, 'post 1 comment 2');
insert into comments values (default, 1, 'post 1 comment 3');
insert into comments values (default, 1, 'post 1 comment 4');

insert into comments values (default, 2, 'post 2 comment 1');
insert into comments values (default, 2, 'post 2 comment 2');

insert into comments values (default, 3, 'post 3 comment 1');
insert into comments values (default, 3, 'post 3 comment 2');
insert into comments values (default, 3, 'post 3 comment 3');
