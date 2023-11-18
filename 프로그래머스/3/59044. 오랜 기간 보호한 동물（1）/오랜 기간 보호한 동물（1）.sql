-- 코드를 입력하세요
-- 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
-- a datetime : 보호시작일ㄹ
-- b datetime : 입양일

SELECT a.NAME, a.DATETIME
FROM ANIMAL_INS a 
LEFT JOIN ANIMAL_OUTS b 
ON a.ANIMAL_ID = b.ANIMAL_ID
WHERE b.ANIMAL_ID is null and a.NAME is not null
ORDER BY a.DATETIME LIMIT 3

