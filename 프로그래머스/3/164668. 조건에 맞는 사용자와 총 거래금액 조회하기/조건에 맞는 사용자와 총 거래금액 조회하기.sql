-- 코드를 입력하세요
-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
SELECT b.USER_ID, b.NICKNAME, sum(a.PRICE) as TOTAL_SALES
FROM USED_GOODS_BOARD a 
JOIN USED_GOODS_USER b
ON a.WRITER_ID = b.USER_ID
WHERE a.STATUS = 'DONE'
GROUP BY b.USER_ID
HAVING TOTAL_SALES >= 700000 
ORDER BY TOTAL_SALES;