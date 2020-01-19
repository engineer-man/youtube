-- update specific record
update people set age = 35 where name = 'Engineer Man';

-- update specific record multiple columns
update people set age = 35, country = 'Canada' where name = 'Engineer Man';

-- pro tip
start transaction;
update people set age = 35;
rollback;
commit;
