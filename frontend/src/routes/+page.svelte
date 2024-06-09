<script>
    import { onMount } from 'svelte';
    import { Select, Helper, GradientButton} from 'flowbite-svelte';
    import { fetchData } from '$lib/fetchData.js';

    let selected;
    let schools = [];

    // API 호출을 통해 데이터를 가져오는 함수
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

    // 컴포넌트가 마운트될 때 API 호출
    onMount(() => {
        loadSchools();
    });
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center w-fit container mx-auto w-fit">
        <p class="text-6xl">Let's Surf School 🌊🏄🏫</p>
        <div class="flex flex-col space-y-2 w-full items-center">
            <div class="w-full flex flex-row space-x-2">
                <div class="w-full">
                    <Select placeholder="Enter School code to fire" items={schools} bind:value={selected} required />
                </div>
                <GradientButton href="/loading" outline color="cyanToBlue" class="w-40">🌊 Surf</GradientButton>
            </div>  
            <Helper class="text-sm">
                We’ll never share your details. Read our <a href="/" class="font-medium text-primary-600 hover:underline dark:text-primary-500"> Privacy Policy </a>
            </Helper>
        </div>
    </div>
</div>