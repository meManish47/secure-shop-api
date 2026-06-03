# AST requirement: Inheritance
class DatabaseConnection:
    def connect(self):
        pass
        
class PostgresConnection(DatabaseConnection):
    def connect(self):
        print("Connecting to postgres...")

def get_db():
    return PostgresConnection()\n