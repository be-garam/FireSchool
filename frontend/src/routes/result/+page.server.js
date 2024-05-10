import * as db from '$lib/server/database.js';

export function load({ cookies }) {
	let id = cookies.get('userid');

	if (!id) {
		id = crypto.randomUUID();
		cookies.set('userid', id, { path: '/' });
	}

	return {
		messages: db.getMessages(id)
	};
}

export const actions = {
	default: async ({ cookies, request }) => {
		const data = await request.formData();
		db.createChat(cookies.get('userid'), data.get('chat'));
	}
};
