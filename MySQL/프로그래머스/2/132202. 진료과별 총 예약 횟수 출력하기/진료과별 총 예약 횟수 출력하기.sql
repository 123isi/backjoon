-- 코드를 입력하세요
SELECT mcdp_cd,count(*) from appointment where month(apnt_ymd)=5 group by mcdp_cd order by count(*), mcdp_cd;