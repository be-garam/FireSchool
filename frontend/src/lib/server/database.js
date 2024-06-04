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
        // {
		// 	id: crypto.randomUUID(),
        //     speaker: "user",
        //     message: "🏄"
		// }
	]);
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

// export function getAnswer(userid, chat) {
// 	const messages = db.get(userid);

// 	messages.push({
// 		id: crypto.randomUUID(),
// 		speaker: "bot",
//         message: "answer example"
// 	});
// }

export async function getAnswer(uri, method = 'POST', chat, userid) {
	const messages = db.get(userid);
    const model_root = "http://10.125.208.189:9241";
    let url = new URL(model_root + uri);
    const headers = { 'Content-Type': 'application/json' };
    let data = JSON.stringify({
        messages: [
          {
            role: "school expert",
            content: chat
          }
        ],
        model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
    });
    let options = {};

    if (method === 'POST' && Object.keys(data).length > 0) {
        url.search = new URLSearchParams(data).toString();
    }

    switch (method) {
        case 'GET':
            options = { method };
            break;
        case 'POST':
            options = {
                method,
                headers,
                body: data
            };
        case 'PUT':
            options = { method };
            break;
        case 'DELETE':
            options = { method };
            break;
        default:
            throw new Error('Unsupported HTTP method');
    }
    
	const response = await fetch(url, options);
	const answer = await response.json();
    console.log(answer);
	answer['id'] = crypto.randomUUID();
	answer['speaker'] = "bot";
	answer['message'] = "answer example";
    console.log(answer);
	return answer;
}

