import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import sys

cred = credentials.Certificate('./fb_secret.json')
firebase_admin.initialize_app(cred)


def update_firebase(additionalCount):
	# Fetch the service account key JSON file contents
	
	db = firestore.client();

	doc_ref = db.collection("rpiCount").document('personCount');

	doc = doc_ref.get().to_dict();
	newCount = doc['currentCount'] + additionalCount

	doc_ref.set({
		'currentCount': newCount
	})

if __name__ == '__main__':
	# By default add 1 to count if no argument is given
	paramCount = 1
	if len(sys.argv) > 1:
		# i.e python firebase_io.py 123
		paramCount = int(sys.argv[1])
	update_firebase(paramCount)