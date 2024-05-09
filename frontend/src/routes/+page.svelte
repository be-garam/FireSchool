<script>
    import { Input, Helper, GradientButton} from 'flowbite-svelte';
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center">
        <p class="text-6xl">Let's Surf School 🌊🏄🏫</p>
        <div class=" flex flex-col space-y-2 w-100">
            <div class="w-full flex flex-row space-x-2">
                <div class="w-full">
                    <Input type="url" id="website" placeholder="Enter School code to fire" required />
                </div>
                <GradientButton href="/loading" outline color="cyanToBlue" class="w-40">🌊 Surf</GradientButton>
            </div>  
            <Helper class="text-sm">
                We’ll never share your details. Read our <a href="/" class="font-medium text-primary-600 hover:underline dark:text-primary-500"> Privacy Policy </a>
            </Helper>
        </div>
    </div>
</div>