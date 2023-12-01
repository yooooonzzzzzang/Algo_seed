-- 코드를 입력하세요
-- MEMBER_PROFILE와 REST_REVIEW 테이블에서 리뷰를 가장 많이 작성한 회원의 리뷰들을 조회하는 SQL문을 작성해주세요. 회원 이름, 리뷰 텍스트, 리뷰 작성일이 출력되도록 작성해주시고, 결과는 리뷰 작성일을 기준으로 오름차순, 리뷰 작성일이 같다면 리뷰 텍스트를 기준으로 오름차순 정렬해주세요.
# SELECT a.MEMBER_NAME,b.REVIEW_TEXT,b.REVIEW_DATE
# FROM MEMBER_PROFILE a
# JOIN REST_REVIEW b
# ON a.MEMBER_ID = b.MEMBER_ID
# WHERE b.MEMBER_ID = (select max(count(MEMBER_ID)) from REST_REVIEW )
# ORDER BY b.REVIEW_DATE, b.REVIEW_TEXT
# select max(count(MEMBER_ID)) from REST_REVIEW 
# ksjs1115@gmail.com	3
# soso94@naver.com	3
# minjea985@naver.com
with temp as (
 SELECT MEMBER_ID, COUNT(MEMBER_ID) AS COUNT
    FROM REST_REVIEW
    GROUP BY MEMBER_ID
    ORDER BY COUNT DESC
    LIMIT 1
    )
    
SELECT a.MEMBER_NAME,b.REVIEW_TEXT,
DATE_FORMAT(b.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
FROM REST_REVIEW b
JOIN MEMBER_PROFILE a
ON a.MEMBER_ID = b.MEMBER_ID
JOIN temp
ON b.MEMBER_ID = temp.MEMBER_ID
ORDER BY REVIEW_DATE, b.REVIEW_TEXT