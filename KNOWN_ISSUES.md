## Error creating table 'keep-alive': {'code': 'PGRST202', 'details': 'Searched for the function public.execute_sql with parameter sql or with a single unnamed json/jsonb parameter, but no matches were found in the schema cache.', 'hint': None, 'message': 'Could not find the function public.execute_sql(sql) in the schema cache'}

run the following code:
```sql
CREATE OR REPLACE FUNCTION public.execute_sql(sql text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  EXECUTE sql;
END;
$$;
```

## Error creating table 'keep-alive': {'code': '42601', 'details': None, 'hint': None, 'message': 'syntax error at or near "-"'}

- add "" to the table name

## Error creating table 'keep-alive': {'code': '42501', 'details': None, 'hint': None, 'message': 'permission denied for schema public'}

- make sure of `SECURITY DEFINER`

## /rest/v1/rpc/truncate_table "HTTP/2 404 Not Found"
## 2025-03-16 18:05:26 - WARNING - Some database actions failed.
run from an owner or administrator account:
```sql
CREATE OR REPLACE FUNCTION public.truncate_table(table_name text)
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
  EXECUTE 'TRUNCATE TABLE ' || quote_ident(table_name) || ' RESTART IDENTITY';
END;
$$;
```

if you run from the developer, you'll get `Unable to run query: Connection string is missing`