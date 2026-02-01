-- 코드를 작성해주세요
select f.id, n.fish_name, f.length from fish_name_info n, fish_info f where f.fish_type=n.fish_type and (f.fish_type,f.length) in (select fish_type,max(length) from fish_info group by fish_type) order by f.id;

