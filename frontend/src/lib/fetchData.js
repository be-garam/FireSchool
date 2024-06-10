const site_root = "http://127.0.0.1:1350/";

export async function fetchData(uri, method = 'GET', data = {}) {
    let url = new URL(site_root + uri);
    const headers = { 'Content-Type': 'application/json' };
    let options = {};

    if (method === 'GET' && Object.keys(data).length > 0) {
        url.search = new URLSearchParams(data).toString();
    }

    switch (method) {
        case 'GET':
            options = { method };
            break;
        case 'POST':
            options = {
                method,
                body: data
            };
            break;
        case 'PUT':
            options = {
                method,
                headers,
                body: JSON.stringify(data)
            };
            break;
        case 'DELETE':
            options = { method };
            break;
        default:
            throw new Error('Unsupported HTTP method');
    }
    
    console.log(options);

    const response = await fetch(url, options);
    console.log(response);
    return await response.json();
}
