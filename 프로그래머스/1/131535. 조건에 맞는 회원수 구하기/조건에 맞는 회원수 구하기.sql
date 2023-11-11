-- 코드를 입력하세요
-- USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇 명인지 출력하는 SQL문을 작성해주세요.
--  year(joined) = 2021
--  WHERE TO_CHAR(JOINED, 'YYYY') = 2021 -> oracle
--  WHERE date_format(JOINED, '%Y') = 2021 -> mysql
-- between 20 and 29
-- where year(joined) = 2021 and age between 20 and 29
SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE date_format(JOINED, '%Y') = 2021
AND
20 <= AGE and AGE <=29 ;