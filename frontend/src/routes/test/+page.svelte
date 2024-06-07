<script>
    import {GradientButton} from 'flowbite-svelte';
    let answer = "No answer yet";
    async function getAnswer() {
        let url = "http://10.125.208.189:9241/v1/chat/completions"
        const res = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'accept': 'application/json'
            },
            body: JSON.stringify({
                messages: [
                {
                    role: "school admissions specialist",
                    content: "hi"
                }
                ],
                model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
            })
        });
        const result = await res.json();
        answer = JSON.stringify(result.choices[0].message.content);
    }
</script>

<GradientButton outline color="cyanToBlue" class="w-40" on:click={getAnswer}>Answer</GradientButton>
<pre>
    <!-- {answer.choices["0"].message.content} -->
    {answer}
</pre>

