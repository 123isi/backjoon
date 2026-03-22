-- 코드를 작성해주세요
select id,if(size_of_colony<=100,"LOW",if(size_of_colony<=1000,"MEDIUM","HIGH")) as size from ecoli_data