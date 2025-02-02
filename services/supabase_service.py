# services/supabase_service.py

from supabase import create_client, Client

class SupabaseClient:
    def __init__(self, url, key, table_name):
        if not url or not key:
            raise ValueError("Supabase URL and Key must be provided.")
        self.client: Client = create_client(url, key)
        self.table_name = table_name

    def check_and_create_table(self):
        """
        Checks if the table exists by attempting a simple select query.
        If the table does not exist, it attempts to create it using an RPC function.
        Note: This requires that an RPC function (e.g. 'execute_sql') is set up in your Supabase database.
        """
        try:
            # Attempt to fetch one record from the table.
            response = self.client.table(self.table_name).select("*").limit(1).execute()
            # If no exception occurs, we assume the table exists.
            print(f"Table '{self.table_name}' exists.")
            return True
        except Exception as e:
            print(f"Table '{self.table_name}' does not exist (or could not be queried). Error: {e}")
            print(f"Attempting to create table '{self.table_name}'...")
            # Define a SQL statement to create the table.
            create_sql = f"""
            CREATE TABLE "{self.table_name}" (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
            """
            try:
                # Call an RPC function to execute the SQL.
                # Ensure that your Supabase instance has an RPC (e.g., "execute_sql") that accepts a parameter "sql"
                response = self.client.rpc("execute_sql", {"sql": create_sql}).execute()
                print(f"Table '{self.table_name}' created successfully.")
                return True
            except Exception as create_error:
                print(f"Error creating table '{self.table_name}': {create_error}")
                return False

    def insert_random_name(self, random_name):
        data = {'name': random_name}
        try:
            response = self.client.table(self.table_name).insert(data).execute()
            print(f"Inserted data into '{self.table_name}': {response.data}")
            return True
        except Exception as e:
            print(f"Error inserting data into '{self.table_name}': {e}")
            return False

    def get_table_count(self):
        try:
            response = self.client.table(self.table_name).select('*', count='exact').execute()
            if response.count is not None:
                return response.count
            else:
                print(f"Could not retrieve count from '{self.table_name}'.")
                return None
        except Exception as e:
            print(f"Error counting data in '{self.table_name}': {e}")
            return None

    def truncate_table(self):
        try:
            # Using an RPC call to truncate the table. Ensure your Supabase DB has this RPC set up.
            self.client.rpc("truncate_table", {"table_name": self.table_name}).execute()
            print(f"Truncated '{self.table_name}'.")
            return True
        except Exception as e:
            print(f"Error truncating '{self.table_name}': {e}")
            return False

    def delete_random_entry(self):
        try:
            # Fetch all IDs from the table
            response = self.client.table(self.table_name).select('id').execute()
            if response.data:
                ids = [item['id'] for item in response.data]
                if not ids:
                    print(f"No entries to delete in '{self.table_name}'.")
                    return True  # No deletion needed, but not an error

                # Randomly select one ID to delete
                import random
                random_id = random.choice(ids)

                # Delete the entry with the selected ID
                self.client.table(self.table_name).delete().eq('id', random_id).execute()
                print(f"Deleted entry with id {random_id} from '{self.table_name}'.")
                return True
            else:
                print(f"No data retrieved from '{self.table_name}'.")
                return False
        except Exception as e:
            print(f"Error deleting data from '{self.table_name}': {e}")
            return False
