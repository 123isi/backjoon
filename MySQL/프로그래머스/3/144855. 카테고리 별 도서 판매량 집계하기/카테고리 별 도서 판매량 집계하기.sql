-- 코드를 입력하세요
SELECT category, sum(s.sales) from book b, book_sales s where b.book_id=s.book_id and (year(sales_date)=2022 and month(sales_date)=1) group by category order by category