-- insert trigger
delimiter $$
create trigger likes_insert
after insert on likes
for each row
begin
    update posts set likes = likes + 1 where post_id = new.post_id;
end$$
delimiter ;

-- see all triggers
show triggers;

-- delete trigger
delimiter $$
create trigger likes_delete
after delete on likes
for each row
begin
    update posts set likes = likes - 1 where post_id = old.post_id;
end$$
delimiter ;

-- remove trigger
drop trigger likes_insert;
drop trigger likes_delete;
