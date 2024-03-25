-- 코드를 작성해주세요
SELECT distinct ID,EMAIL,FIRST_NAME,LAST_NAME
FROM DEVELOPERS a
JOIN SKILLCODES b
On b.code & a.SKILL_CODE = b.code
where b.category = 'Front End' 
ORDER BY ID;