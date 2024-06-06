<script>
    async function getAnswer() {
        let url = "http://10.125.208.189:9241/v1/chat/completions"
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                messages: [
                {
                    role: "school admissions specialist",
                    content: chat
                }
                ],
                model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
            })
        });
        const data = await res.json();s
        console.log(data);
    }
</script>

<pre>
    {data}
</pre>

