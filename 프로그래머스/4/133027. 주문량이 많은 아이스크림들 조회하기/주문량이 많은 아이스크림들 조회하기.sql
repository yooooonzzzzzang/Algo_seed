-- 코드를 입력하세요
-- 7월 아이스크림 총 주문량과 상반기의 아이스크림 총 주문량을 더한 값이 큰 순서대로 상위 3개의 맛을 조회하는 SQL 문을 작성해주세요.

SELECT a.FLAVOR
FROM FIRST_HALF a
JOIN JULY b
ON a.FLAVOR = b.FLAVOR
group by flavor
ORDER BY sum(a.TOTAL_ORDER+ b.TOTAL_ORDER) desc limit 3