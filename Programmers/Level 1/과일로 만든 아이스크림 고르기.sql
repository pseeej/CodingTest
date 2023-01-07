-- 코드를 입력하세요
SELECT FLAVOR
FROM ( SELECT FIRST_HALF.FLAVOR, FIRST_HALF.TOTAL_ORDER, ICECREAM_INFO.INGREDIENT_TYPE
        FROM FIRST_HALF, ICECREAM_INFO
        WHERE FIRST_HALF.FLAVOR = ICECREAM_INFO.FLAVOR) TAB
WHERE INGREDIENT_TYPE = "fruit_based" AND TOTAL_ORDER >= 3000

