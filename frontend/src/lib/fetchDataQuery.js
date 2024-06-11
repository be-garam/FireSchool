const site_root = "http://127.0.0.1:1350/";

export async function fetchDataQuery(uri, method = 'GET', data = {}) {
    let url = new URL(site_root + uri);
    const headers = { 'Content-Type': 'application/json' };
    let options = { method, headers };

    if (method === 'GET' && Object.keys(data).length > 0) {
        url.search = new URLSearchParams(data).toString();
    }

    if (method === 'POST') {
        // POST 요청 시에도 쿼리 파라미터로 데이터를 전송
        url.search = new URLSearchParams(data).toString();
    }

    const response = await fetch(url, options);
    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || response.statusText);
    }
    return await response.json();
}
