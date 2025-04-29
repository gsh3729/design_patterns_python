'''
provides a surrogate or placeholder for another object to control access to it. 
to add functionality (like access control, lazy initialization, logging, etc.) to an object without changing its code
'''

class Database:
    def __init__(self, db_url):
        print("Connecting to DB...")
        self.db_url = db_url
        self.connected = True

    def query(self, sql):
        print(f"Executing SQL on {self.db_url}: {sql}")
        return f"Results for '{sql}'"


# PROXY
class DatabaseProxy:
    def __init__(self, db_url):
        self.db_url = db_url
        self._real_db = None

    def _initialize(self):
        if self._real_db is None:
            self._real_db = Database(self.db_url)

    def query(self, sql):
        print("[Proxy] Intercepting query...")
        self._initialize()
        return self._real_db.query(sql)


# Client code
def run_service(db):
    print("Service started")
    result = db.query("SELECT * FROM users")
    print("Query Result:", result)


# Usage
proxy_db = DatabaseProxy("postgresql://localhost/db")
run_service(proxy_db)

'''
Service started
[Proxy] Intercepting query...
Connecting to DB...
Executing SQL on postgresql://localhost/db: SELECT * FROM users
Query Result: Results for 'SELECT * FROM users'
'''