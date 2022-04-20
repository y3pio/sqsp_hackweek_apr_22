import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./fb_secret.json')
firebase_admin.initialize_app(cred)

db = firestore.client();

doc_ref = db.collection("rpiCount").document('personCount');


doc = doc_ref.get().to_dict();
newCount = doc['currentCount'] + 1

doc_ref.set({
	'currentCount': newCount
})
