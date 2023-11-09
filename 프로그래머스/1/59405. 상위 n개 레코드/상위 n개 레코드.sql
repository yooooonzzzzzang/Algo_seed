-- 코드를 입력하세요
# SELECT NAME FROM ANIMAL_INS order by datetime limit 1;
SELECT NAME from ANIMAL_INS where DATETIME = (select min(DATETIME) from ANIMAL_INS)