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
    let url = 'http://10.125.208.189:9241/v1/chat/completions';
    const headers = { 
        'Content-Type': 'application/json',
        'accept': 'application/json'
    };
    let data = JSON.stringify({
        messages: [
          {
            role: "school admissions specialist",
            content: chat
          }
        ],
        model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
    });
    // console.log(data);
    let options = {};
    let chatData = {};

    const messages = db.get(userid);

    // if (method === 'POST' && Object.keys(data).length > 0) {
    //     url.search = new URLSearchParams(data).toString();
    // }


    switch (method) {
        case 'GET':
            // console.log("GET");
            options = { method };
            break;
        case 'POST':
            // console.log("POST");
            options = {
                method,
                headers,
                body: JSON.stringify({
                    messages: [
                    {
                        role: "school admissions specialist",
                        content: "hi"
                    }
                    ],
                    model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
                })
            };
            break;
        case 'PUT':
            // console.log("PUT");
            options = { method };
            break;
        case 'DELETE':
            // console.log("DELETE");
            options = { method };
            break;
        default:
            throw new Error('Unsupported HTTP method');
    }
    
    console.log(options);

	const response = await fetch(url, options);
	const answer = await response.json();
    chatData['id'] = crypto.randomUUID();
	chatData['speaker'] = "bot";
	chatData['message'] = answer.choices[0].message.content;
    console.log(JSON.stringify(chatData));
    messages.push(chatData);
    return chatData;
}// }
