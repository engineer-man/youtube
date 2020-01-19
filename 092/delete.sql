-- delete all
delete from people;

-- delete only engineer man
delete from people where name = 'Engineer Man';

-- delete only people 30 and over
delete from people where age >= 30;

-- delete only people 30 and over in russia
delete from people where age >= 30 and country = 'Russia';

-- pro tip
start transaction;
delete from people;
rollback;
