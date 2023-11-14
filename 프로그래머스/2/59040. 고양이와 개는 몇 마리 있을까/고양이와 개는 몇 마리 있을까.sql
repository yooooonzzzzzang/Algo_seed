-- 코드를 입력하세요
-- 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 
-- 이때 고양이를 개보다 먼저 조회해주세요.
SELECT ANIMAL_TYPE, count(*) as count
FROM ANIMAL_INS 
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE = 'Cat' or ANIMAL_TYPE = 'Dog'
ORDER BY ANIMAL_TYPE
