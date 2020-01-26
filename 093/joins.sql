-- left join (return all rows from posts but only matching comments)
select * from posts
left join comments on posts.post_id = comments.post_id
where posts.post_id = 1
order by comments.comment_id desc;

-- inner join (return all rows from posts that have matching comments)
select * from posts
inner join comments on posts.post_id = comments.post_id;

-- right join (return all rows from comments but only matching posts)
select * from posts
right join comments on posts.post_id = comments.post_id;
