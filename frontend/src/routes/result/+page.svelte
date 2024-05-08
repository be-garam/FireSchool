<script>
    import {Card, Listgroup, GradientButton, Badge} from 'flowbite-svelte';
    
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
</script>

<div class="flex items-center justify-center h-screen w-screen bg-neutral-100 gap-x-24 p-24">
    <div class="flex-none w-96 flex-col space-y-10 justify-start">
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
                    <GradientButton href={item.path} outline color="pinkToOrange" class="w-40">Fire🔥</GradientButton>
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
                    <GradientButton href={item.path} outline color="pinkToOrange" class="w-40">Fire🔥</GradientButton>
                </div>
            </Listgroup>
        </Card>
    </div>
    <div class="flex-1 bg-white">
        03
    </div>
</div>