<script>
    import { Input, Helper} from 'flowbite-svelte';
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
    <div class="flex flex-col space-y-10 items-center justify-center">
        <p class="text-6xl">Let's Fire School 🤜🔥🏫</p>
        <div class="w-max max-w-4xl w-852 flex flex-col space-y-2 ">
            <div class="w-full">
                <Input type="url" id="website" placeholder="Enter School code to fire" required />
            </div>
            <Helper class="text-sm">
                We’ll never share your details. Read our <a href="/" class="font-medium text-primary-600 hover:underline dark:text-primary-500"> Privacy Policy </a>
            </Helper>
        </div>
    </div>
</div>