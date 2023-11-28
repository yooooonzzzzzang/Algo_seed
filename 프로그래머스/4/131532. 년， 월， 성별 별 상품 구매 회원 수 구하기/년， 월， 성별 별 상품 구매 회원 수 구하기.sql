-- 코드를 입력하세요
-- USER_INFO 테이블과 ONLINE_SALE 테이블에서 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성해주세요. 결과는 년, 월, 성별을 기준으로 오름차순 정렬해주세요. 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
SELECT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, a.GENDER as GENDER, count(distinct a.USER_ID)
FROM USER_INFO a
JOIN ONLINE_SALE b
ON a.USER_ID = b.USER_ID
WHERE GENDER is not null
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER