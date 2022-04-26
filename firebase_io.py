import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys

# By default add 1 to count if no argument is given
additionalCount = 1

if len(sys.argv) > 1:
	# i.e python firebase_io.py 123
	additionalCount = int(sys.argv[1])

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./fb_secret.json')
firebase_admin.initialize_app(cred)

db = firestore.client();

doc_ref = db.collection("rpiCount").document('personCount');

doc = doc_ref.get().to_dict();
newCount = doc['currentCount'] + additionalCount

doc_ref.set({
	'currentCount': newCount
})
