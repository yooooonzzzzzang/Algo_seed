-- 코드를 입력하세요
-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요.
-- ,전체주소, 전화번호
SELECT b.USER_ID, b.NICKNAME ,
CONCAT(b.city," ",b.STREET_ADDRESS1," ",b.STREET_ADDRESS2) as 전체주소, 
CONCAT(substr(b.TLNO,1,3),"-",substr(b.TLNO,4,4),"-",substr(b.TLNO,8,4)) as전화번호
FROM USED_GOODS_BOARD a
JOIN USED_GOODS_USER b
ON a.WRITER_ID = b.USER_ID
GROUP BY b.USER_ID
HAVING count(a.BOARD_ID) >= 3
ORDER BY b.USER_ID DESC