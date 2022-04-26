window.onload = function() {
	const targetElement = document.querySelector("#output");

	const firebase = window.firebase;
	const firebaseConfig = {}; // Copy over config from Firebase Web SDK section.
	firebase.initializeApp(firebaseConfig);

	const db = firebase.firestore();
	var docRef = db.collection("rpiCount").doc("personCount");

	docRef.get().then(doc => {
		targetElement.innerHTML = `${doc.data().currentCount}`
	}).catch(err => {
		console.log("docRef get Error:", err);
	})

	db.collection("rpiCount").doc("personCount")
    .onSnapshot((doc) => {
    	targetElement.innerHTML = `${doc.data().currentCount}`
    });
}