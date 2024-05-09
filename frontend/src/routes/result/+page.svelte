<script>
    import {Card, Listgroup, GradientButton, Badge, Input, ButtonGroup, P} from 'flowbite-svelte';
    import { onMount } from 'svelte';
    
    let path = 'https://github.com/be-garam'
    
    let keyword_list = ['school', 'important', 'file'];

    let url_list = [
        {
            name: 'url1',
            path: path
        },
        {
            name: 'url2',
            path: path
        },
        {
            name: 'url3',
            path: path
        }
    ];

    let file_list = [
        {
            name: 'file1',
            path: path
        },
        {
            name: 'file2',
            path: path
        },
        {
            name: 'file3',
            path: path
        }
    ];

    let pre_chat_list = [];
    let chat_list = [];

    onMount(async () => {
        const res = await fetch('./chat.json');
        pre_chat_list = await res.json();
        chat_list = pre_chat_list.messages;
        console.log(chat_list.messages);
    });

</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100 gap-x-10 p-24">
    <div class="flex-none w-96 h-full flex-col space-y-10 justify-start">
        <Card class="bg-white space-y-6 flex-none">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white">🗝️ Your school's keyword</h3>
            <div class="flex flex-row space-x-2">
                {#each keyword_list as keyword (keyword)}
                    <Badge large color="indigo">{keyword}</Badge>
                {/each}
            </div> 
        </Card>
        <Card class="bg-white space-y-2 flex-auto">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white">👀 Seems Important</h3>
            <Listgroup items={url_list} let:item class="border-0 dark:!bg-transparent">
                <div class="flex flex-row space-x-2 items-center">
                    <p class="grow text-sm font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <GradientButton href={item.path} color="cyanToBlue" size="xs">🌊 Surf</GradientButton>
                </div>
            </Listgroup>
        </Card>
        <Card class="bg-white space-y-2 flex-auto">
            <h3 class="text-xl font-medium text-gray-900 dark:text-white">🗂️ File we found</h3>
            <Listgroup items={file_list} let:item class="border-0 dark:!bg-transparent">
                <div class="flex flex-row space-x-2 items-center">
                    <p class="grow text-sm font-medium text-gray-900 truncate dark:text-white">
                        {item.name}
                    </p>
                    <GradientButton href={item.path} color="cyanToBlue" size="xs">🌊 Surf</GradientButton>
                </div>
            </Listgroup>
        </Card>
    </div>
    <div class="flex-1 flex h-full flex-col space-y-4">
        <div class="flex-auto flex-col space-y-4">
            {#each chat_list as {speaker, message}}
                {#if speaker == 'user'}
                    <div class="w-full items-end flex">
                        <div class="w-2/5"></div>
                        <div class="w-3/5 p-4 bg-white rounded-lg border">
                            <P color="text-green-700 dark:text-green-500">{speaker}</P>
                            {message}
                        </div>
                    </div>
                {/if}
                {#if speaker == 'bot'}
                    <div class="w-full items-end flex">
                        <div class="w-3/5 p-4 bg-white rounded-lg border">
                            <P color="text-blue-700 dark:text-blue-500">{speaker}</P>
                            {message}
                        </div>
                        <div class="w-2/5"></div>
                    </div>
                {/if}
            {/each}
        </div>
        <div class=flex-none>
            <ButtonGroup class="w-full">
              <Input type="text" placeholder="💬 Chat here" size="lg" />
              <GradientButton color="cyanToBlue" size="lg">Send</GradientButton>
            </ButtonGroup>
        </div>
    </div>
</div>