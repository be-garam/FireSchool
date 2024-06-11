<script>
    import { onMount } from 'svelte';
    import { Select, Helper, GradientButton} from 'flowbite-svelte';
    import { fetchData } from '$lib/fetchData.js';
    import { goto } from '$app/navigation';

    // for select field
    let selected;
    let schools = [];

    async function loadSchools() {
        try {
            const data = await fetchData("api/school_list", "GET");
            let newSchools = [];
            // for 루프를 사용하여 schools 변수 업데이트
            for (let i = 0; i < data.length; i++) {
                newSchools.push({
                    value: data[i], 
                    name: data[i]
                });
            }
            schools = newSchools;
        } catch (error) {
            console.error('Failed to load schools:', error);
        }
    }

    function handleSubmit(event) {
        event.preventDefault();
        goto(`/result?school_name=${encodeURIComponent(selected)}`);
    }

    // 컴포넌트가 마운트될 때 API 호출
    onMount(() => {
        loadSchools();
    });
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center container mx-auto w-fit">
        <p class="text-6xl">Let's Surf School 🌊🏄🏫</p>
        <div class="flex flex-col space-y-2 w-full items-center">
            <form class="w-full flex flex-row space-x-2" on:submit|preventDefault={handleSubmit}>
                <div class="w-full">
                    <Select placeholder="Enter School code to fire" items={schools} bind:value={selected} required />
                </div>
                <GradientButton type="submit" outline color="cyanToBlue" class="w-40">🌊 Surf</GradientButton>        
            </form>
            <Helper class="text-sm">
            Don't see the school you want? <a href="/suggest" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Click here</a>
            </Helper>
        </div>
    </div>
</div>