-- 코드를 입력하세요
SELECT b.WRITER_ID as USER_ID, u.NICKNAME as NICKNAME, SUM(b.PRICE) as TOTAL_SALES
from USED_GOODS_BOARD as b join USED_GOODS_USER as u on b.WRITER_ID = u.USER_ID
where b.STATUS = "DONE"
group by b.WRITER_ID having SUM(b.PRICE) >= 700000
order by SUM(b.PRICE) asc
