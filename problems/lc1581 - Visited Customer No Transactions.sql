-- Write your PostgreSQL query statement below
with all_visits as (
  select v.visit_id, customer_id, transaction_id, amount
  from Visits v
  left join Transactions t
  on v.visit_id = t.visit_id
  where amount is null
)

select customer_id, count(customer_id) as count_no_trans
from all_visits
group by customer_id
