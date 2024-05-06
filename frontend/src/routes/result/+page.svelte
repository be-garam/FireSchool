<script>
    import {GradientButton} from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    
    async function handleClick() {
        goto('/result/+page.svelte'); // navigate to /loading/+page.svelte
    }
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center">
        <p class="text-6xl">Result🔥</p>
    </div>
</div>