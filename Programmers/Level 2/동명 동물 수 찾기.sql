-- 코드를 입력하세요
SELECT NAME,
    COUNT(NAME) AS 'COUNT'
    FROM ANIMAL_INS
    GROUP BY NAME
-- group by에서의 조건문은 having 사용하기!
    HAVING COUNT(NAME)>1
    ORDER BY NAME
