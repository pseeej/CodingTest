-- 코드를 입력하세요
SELECT LEFT(PRODUCT_CODE, 2) CATEGORY, COUNT(*)
FROM PRODUCT
GROUP BY LEFT(PRODUCT_CODE, 2)
ORDER BY CATEGORY
