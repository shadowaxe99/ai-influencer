import pymongo
from bson import ObjectId

class BaseMongoInterface:
    def __init__(self, db_uri, db_name, collection_name):
        self.db_uri = db_uri
        self.db_name = db_name
        self.collection_name = collection_name
        self.client = pymongo.MongoClient(self.db_uri)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.collection_name]

class UserProfilesManager(BaseMongoInterface):
    PROFILE_COLLECTION = "profiles"

    def __init__(self, user_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_id = user_id
        self._check_connection()

    @property
    def _collection(self):
        return self.db[self.PROFILE_COLLECTION]

    def _check_connection(self):
        if not self.client.server_info():
            raise ConnectionError("Couldn't connect to the MongoDB server.")

    def manage_user_profile(self, operation="retrieve"):
        """Manage user profiles based on the specified operation."""
        valid_operations = ("create", "retrieve", "update", "delete")
        if operation not in valid_operations:
            raise ValueError(f"Operation '{operation}' invalid. Supported ones are: {valid_operations}.")
        
        if operation == "create":
            pass
        elif operation == "retrieve":
            return self.get_profile()
        elif operation == "update":
            pass
        elif operation == "delete":
            pass

    def get_profile(self):
        """Retrieve a single profile."""
        result = self._collection.find_one({'_id': self.user_id})
        if not result:
            raise ProfileNotFoundError(f"No profile found for user ID: {str(self.user_id)}")
        return result

    def update_profile(self, updated_data):
        """Update a user profile."""
        query = {'_id': self.user_id}
        new_values = {'$set': updated_data}
        self._collection.update_one(query, new_values)

    def delete_profile(self):
        """Delete a user profile."""
        result = self._collection.delete_one({'_id': self.user_id})
        if result.deleted_count != 1:
            raise ProfileDeletionError(f"Failed to delete profile for user ID: {str(self.user_id)}")

class ProfileNotFoundError(Exception):
    pass

class ProfileDeletionError(Exception):
    pass
