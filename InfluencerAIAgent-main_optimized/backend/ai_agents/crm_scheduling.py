import datetime
from pymongo import MongoClient
client = MongoClient(os.getenv('MONGODB_URI', 'mongodb://localhost:27017/'))
db = client[os.getenv('MONGODB_DB', 'influencer_platform')]
collection = db[os.getenv('MONGODB_COLLECTION', 'contactDatabase')]
contactDatabase = []
appointmentSchedule = []
def manageContacts():
global contactDatabase
try:
contacts = collection.find()
contactDatabase = list(contacts)
except Exception as e:
def scheduleAppointments():
global appointmentSchedule
updated_contacts = []
now = datetime.datetime.now()
for contact in contactDatabase:
contact['next_appointment'] = now + datetime.timedelta(days=7)
updated_contacts.append(contact)
appointmentSchedule.extend(updated_contacts)
# Update the contacts in the original database
for contact in updated_contacts:
manageContacts()
scheduleAppointments()