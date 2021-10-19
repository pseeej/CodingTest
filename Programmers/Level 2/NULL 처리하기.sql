-- 코드를 입력하세요
-- case when ~ then ~ else ~ end as ~

SELECT ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL THEN 'No name'
        ELSE NAME
        END AS NAME,
    SEX_UPON_INTAKE
    FROM ANIMAL_INS
        
