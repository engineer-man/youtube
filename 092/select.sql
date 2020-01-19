-- select all
select * from people;

-- select all but specific columns
select name, age from people;

-- select only engineer man
select * from people where name = 'Engineer Man';

-- select only people 30 and over
select * from people where age >= 30;

-- select only people 30 and over in russia
select * from people where age >= 30 and country = 'Russia';

-- select all and order by age
select * from people order by age desc;

-- select top 3 oldest
select * from people order by age desc limit 3;
