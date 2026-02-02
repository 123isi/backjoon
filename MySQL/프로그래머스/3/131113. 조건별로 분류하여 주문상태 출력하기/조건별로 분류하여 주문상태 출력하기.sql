-- 코드를 입력하세요
SELECT order_id, product_id, ifnull(left(out_date,10), null) AS out_date, if(out_date is null,'출고미정',if(out_date<='2022-05-01','출고완료','출고대기')) as 출고여부 from FOOD_ORDER order by order_id;