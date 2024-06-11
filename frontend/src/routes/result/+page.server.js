import * as db from '$lib/server/database.js';
import { fetchDataQuery } from '$lib/fetchDataQuery.js';

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
        db.getAnswer(
			'/v1/chat/completions', 
			'POST', 
			data.get('chat'),
			cookies.get('userid'));
	}
};