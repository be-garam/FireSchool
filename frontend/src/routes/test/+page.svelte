<script>
    import {GradientButton} from 'flowbite-svelte';
    let answer = "No answer yet";
    async function getAnswer() {
        let url = "http://10.125.208.189:9241/v1/models"
        const res = await fetch(url, {
            method: 'GET',
            // body: JSON.stringify({
            //     messages: [
            //     {
            //         role: "school admissions specialist",
            //         content: "hi"
            //     }
            //     ],
            //     model: "OpenBuddy/openbuddy-llama3-8b-v21.1-8k"
            // })
        });
        console.log(res);
        answer = await res.json();
        console.log("Answer:");
        console.log(answer);
    }
</script>

<GradientButton outline color="cyanToBlue" class="w-40" on:click={getAnswer}>Answer</GradientButton>
<pre>
    {answer}
</pre>

