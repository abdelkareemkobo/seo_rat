"""A Simple API for configure the DB connection with Mongodb"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['MongoDBConnection']

# %% ../nbs/00_core.ipynb 3
class MongoDBConnection:
    """Class to handle MongoDB connections for SEORAT"""

    def __init__(self, connection_string: str = "mongodb://127.0.0.1:27017/"):
        self.connection_string = connection_string
        self.client: Optional[MongoClient] = None

    def connect(self, db_name: str = "seorat") -> Optional[Database]:
        """Connect to MongoDB and return database instance"""
        try:
            self.client = MongoClient(self.connection_string)
            return self.client[db_name]
        except Exception as e:
            print(f"Error connecting to MongoDB: {e}")
            return None

    def close(self):
        """Close the MongoDB connection"""
        if self.client:
            self.client.close()

