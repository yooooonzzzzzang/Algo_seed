-- 코드를 입력하세요
-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문을 작성해주세요. 결과는 카테고리명을 기준으로 오름차순 정렬해주세요.


SELECT a.CATEGORY, SUM(b.SALES) as TOTAL_SALES
FROM BOOK a
JOIN BOOK_SALES b
ON a.BOOK_ID = b.BOOK_ID and DATE_FORMAT(b.SALES_DATE, '%Y-%m') = '2022-01'
GROUP BY a.CATEGORY
ORDER BY a.CATEGORY