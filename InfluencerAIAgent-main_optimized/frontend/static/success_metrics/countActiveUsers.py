def count_active_users():
# Replace with your actual MongoDB connection string and database name
database_name = 'mydatabase'  # Replace with your database name
client = MongoClient(mongo_connection_string)
db = client[database_name]
active_user_count = users_collection.count_documents({'status': 'active'})
return active_user_count
active_user_count = count_active_users()