create table authors (
    author_id int unsigned not null auto_increment,
    name varchar(255) not null,
    created_at datetime not null,
    primary key (author_id)
)engine=innodb default charset=utf8 collate=utf8_unicode_ci;

insert into authors values (default, 'William Shakespeare', now());
insert into authors values (default, 'Emily Dickinson', now());
insert into authors values (default, 'H. P. Lovecraft', now());
insert into authors values (default, 'Arthur Conan Doyle', now());
insert into authors values (default, 'Leo Tolstoy', now());
insert into authors values (default, 'Edgar Allan Poe', now());
insert into authors values (default, 'Robert Ervin Howard', now());
insert into authors values (default, 'Rabindranath Tagore', now());
insert into authors values (default, 'Rudyard Kipling', now());

create table books (
    book_id int unsigned not null auto_increment,
    author_id int unsigned not null,
    name varchar(255) not null,
    created_at datetime not null,
    primary key (book_id)
)engine=innodb default charset=utf8 collate=utf8_unicode_ci;

insert into books values (default, 1, 'Alls Well That Ends Well', now());
insert into books values (default, 1, 'As You Like It', now());
insert into books values (default, 1, 'The Comedy of Errors', now());
insert into books values (default, 2, 'I dwell in Possibility', now());
insert into books values (default, 2, 'Much Madness is divinest Sense', now());
insert into books values (default, 2, 'Another book', now());
insert into books values (default, 3, 'At the Mountains of Madness', now());
insert into books values (default, 3, 'The Case of Charles Dexter Ward', now());
insert into books values (default, 3, 'The Dream-Quest of Unknown Kadath', now());
insert into books values (default, 4, 'A Study in Scarlet', now());
insert into books values (default, 4, 'The Sign of the Four', now());
insert into books values (default, 4, 'The Adventures of Sherlock Holmes', now());
insert into books values (default, 5, 'Two Hussars', now());
insert into books values (default, 5, 'A Morning of a Landed Proprietor', now());
insert into books values (default, 5, 'Albert', now());
insert into books values (default, 6, 'Tales of the Grotesque and Arabesque', now());
insert into books values (default, 6, 'The Prose Romances of Edgar A. Poe', now());
insert into books values (default, 6, 'Tales', now());
insert into books values (default, 7, 'What the Nation Owes the South', now());
insert into books values (default, 7, 'The Ideal Girl', now());
insert into books values (default, 7, 'Dula Due To Be Champion', now());
insert into books values (default, 8, 'Creative Unity', now());
insert into books values (default, 8, 'Nationalism', now());
insert into books values (default, 8, 'Thought Relics', now());
insert into books values (default, 9, 'Schoolboy Lyrics', now());
insert into books values (default, 9, 'Echoes, by Two Writers', now());
insert into books values (default, 9, 'Departmental Ditties and other verses', now());
