-- 코드를 입력하세요
-- FOOD_PRODUCT 테이블에서 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회하는 SQL문을 작성해주세요. 이때 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력시켜 주시고 결과는 식품 가격을 기준으로 내림차순 정렬해주세요.
# P0011	맛있는콩기름	CD_OL00001	식용유	4880 -> 맛올리브
# P0051	맛있는배추김치	CD_KC00001	김치	19000
# P0071	맛있는미역국	CD_SU00001	국	2400  -> 맛 김치ㅉ;게
# P0091	맛있는포카칩	CD_CK00001	과자	1500  -> 허니버터

# select max(PRICE) from FOOD_PRODUCT where CATEGORY in ('과자', '국', '김치', '식용유') group by category 


SELECT CATEGORY, PRICE as MAX_PRICE,PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE in (select max(PRICE) from FOOD_PRODUCT where CATEGORY in ('과자', '국', '김치', '식용유') group by category )
AND CATEGORY in ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
ORDER BY PRICE DESC