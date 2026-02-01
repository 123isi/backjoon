-- 코드를 입력하세요
SELECT book_id, author_name, left(published_date, 10) from book b, author a where b.author_id=a.author_id and category='경제' order by published_date