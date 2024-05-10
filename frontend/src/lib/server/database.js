// In a real app, this data would live in a database,
// rather than in memory. But for now, we cheat.
const id = 0;
const db = new Map();
// db.set(id, {"speaker": "bot", "message": "Let's surf the school 🌊"})
// db.set(id + 1, {"speaker": "user","message": "🏄"})

export function getMessages(userid) {
	if (!db.get(userid)) {
		db.set(userid, [{
			id: crypto.randomUUID(),
            speaker: "bot",
            message: "Let's surf the school 🌊"
		},
        {
			id: crypto.randomUUID(),
            speaker: "user",
            message: "🏄"
		}]);
	}

	return db.get(userid);
}

export function createChat(userid, chat) {
	const messages = db.get(userid);

	messages.push({
		id: crypto.randomUUID(),
		speaker: "user",
        message: chat
	});
}
