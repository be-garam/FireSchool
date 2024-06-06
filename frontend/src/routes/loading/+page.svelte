<script>
    import {GradientButton, Spinner} from 'flowbite-svelte';
    import { goto } from '$app/navigation';
    
    async function handleClick() {
        goto('/result/+page.svelte'); // navigate to /loading/+page.svelte
    }
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center">
        <p class="text-6xl">Surfing School...🌊🏄</p>
        <Spinner color="blue" size="12"/>
        <div class="flex flex-row space-x-2">
            <GradientButton href="/result" outline color="cyanToBlue" class="w-40">Loading</GradientButton>
            <GradientButton href="/test" outline color="cyanToBlue" class="w-40">test</GradientButton>
        </div>
    </div>
</div>