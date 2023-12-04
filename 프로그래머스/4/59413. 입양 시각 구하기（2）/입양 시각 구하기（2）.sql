-- 코드를 입력하세요
-- 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 0시부터 23시까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
# SELECT DATE_FORMAT(DATETIME,'%H') as HOUR, count(*)
# FROM ANIMAL_OUTS
# GROUP BY HOUR
# ORDER BY HOUR
with recursive cte as (
    select 0 as hour
    union all
    select hour+1 
    from cte
    where hour < 23
)

select cte.hour, IFNULL(a.cnt,0)
from cte
left join (
    SELECT DATE_FORMAT(DATETIME,'%H') as time, 
    count(*) as cnt
    FROM ANIMAL_OUTS
    GROUP BY time
    ORDER BY time
) a
ON cte.hour = a.time