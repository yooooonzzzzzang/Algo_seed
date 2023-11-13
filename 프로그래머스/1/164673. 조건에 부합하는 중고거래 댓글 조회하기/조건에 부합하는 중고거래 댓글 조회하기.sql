-- 코드를 입력하세요
-- USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.

SELECT a.TITLE, a.BOARD_ID, b.REPLY_ID, b.WRITER_ID, b.CONTENTS, 
date_format(b.CREATED_DATE, '%Y-%m-%d') as CREATED_DATE
from USED_GOODS_BOARD as a, USED_GOODS_REPLY as b 
where a.CREATED_DATE like '2022-10%' and a.board_id = b.board_id 
order by b.CREATED_DATE, a.TITLE;