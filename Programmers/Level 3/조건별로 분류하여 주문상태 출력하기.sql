-- 코드를 입력하세요
SELECT ORDER_ID, PRODUCT_ID, left(OUT_DATE, 10) OUT_DATE, IF(OUT_DATE <= '2022-05-01', '출고완료', if(out_date is null, '출고미정', '출고대기')) '출고여부'
FROM FOOD_ORDER
order by order_id
