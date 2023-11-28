-- 코드를 입력하세요
-- PATIENT, DOCTOR 그리고 APPOINTMENT 테이블에서 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성해주세요. 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성해주세요. 결과는 진료예약일시를 기준으로 오름차순 정렬해주세요.

SELECT c.APNT_NO, a.PT_NAME, a.PT_NO, b.MCDP_CD, b.DR_NAME, c.APNT_YMD
FROM PATIENT a, DOCTOR b, APPOINTMENT c
WHERE a.PT_NO = c.PT_NO and b.DR_ID = c.MDDR_ID 
    and DATE_FORMAT(APNT_YMD, '%Y-%m-%d') = '2022-04-13'  and APNT_CNCL_YN ='N' 
ORDER BY c.APNT_YMD
