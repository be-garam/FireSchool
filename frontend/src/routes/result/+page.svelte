<script>
    import { onMount } from 'svelte';
    import { fetchDataQuery } from '$lib/fetchDataQuery.js';
    import { GradientButton, Badge, Input, ButtonGroup, P, Spinner } from 'flowbite-svelte';
    import { page } from '$app/stores';

    // getting School name from URL
    let schoolData = null;
    let error = null;
    let school_name = null;

    // add school_data by fetching from API
    $: {
        school_name = new URLSearchParams($page.url.search).get('school_name');
    }

    onMount(async () => {
        if (!school_name) {
            error = 'No school name provided';
            return;
        }

        try {
            const rawData = await fetchDataQuery("api/school_data", "POST", { school_name });
            schoolData = rawData;
        } catch (err) {
            error = err.message;
        }
    });

    let keyword_list = [];
    let url_list = [];
    let file_list = [];

    $: if (schoolData) {
        keyword_list = schoolData.keywords || [];
        url_list = schoolData.links || [];
        file_list = schoolData.files || [];
    }

    // Chat list: not going to added in DB just calling api
    let pre_chat_list = [];
    let chat_list = [];

    onMount(async () => {
        const res = await fetch('./chat.json');
        pre_chat_list = await res.json();
        chat_list = pre_chat_list.messages;
        console.log(chat_list.messages);
    });

    export let data = { messages: [] };

    if (!data.messages) {
        data.messages = [];
    }

    let question;
    // Chatting
    let loading = false;

    async function chat() {
        try {
            // 유저의 질문을 먼저 메시지 리스트에 추가하고 입력 필드 초기화
            data = {
                ...data,
                messages: [
                    ...data.messages,
                    { speaker: 'user', message: question },
                    { speaker: 'bot', message: '...' } // 임시 메시지로 스피너를 표시
                ]
            };
            question = ''; // 입력 필드 초기화

            // 로딩 상태 설정
            loading = true;

            // API 호출
            const chat_response = await fetchDataQuery("api/chat/completions", "POST", { chat: question, school_name });
            console.log(chat_response);

            // 메시지 리스트에서 임시 메시지 제거하고 실제 응답 추가
            data.messages = data.messages.map((msg, index) => 
                index === data.messages.length - 1
                    ? { speaker: 'bot', message: chat_response.message }
                    : msg
            );

            // 로딩 상태 해제
            loading = false;

        } catch (err) {
            error = err.message;
            console.log(error);
            loading = false;
        }
    }

    function handleSubmit(event) {
        event.preventDefault();
        chat();
    }
</script>

{#if !schoolData && !error}
    <div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
        <div class="flex flex-col space-y-10 items-center justify-center">
            <p class="text-6xl">Surfing School...🌊🏄</p>
            <Spinner color="blue" size="12"/>
        </div>
    </div>
{:else}
    {#if error}
        <div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
            <div class="flex flex-col space-y-10 items-center justify-center w-fit container mx-auto w-fit">
                <p class="text-6xl">Error</p>
                <p class="text-xl">{error}</p>
                <GradientButton href="/" outline color="cyanToBlue" class="w-40">🏠 Home</GradientButton>
            </div>
        </div>
    {:else}
        <div class="flex items-center justify-center h-screen w-screen bg-neutral-100 divide-x-2">
            <div class="flex-none w-80 h-full flex-col space-y-14 justify-start bg-white py-12 px-4">
                <div class="space-y-6 flex-none">
                    <h3 class="text-xl font-medium text-gray-900 dark:text-white">🗝️ Your school's keyword</h3>
                    <div class="flex flex-row space-x-2">
                        {#each keyword_list as keyword (keyword)}
                            <Badge large color="indigo">{keyword}</Badge>
                        {/each}
                    </div> 
                </div>
                <div class="space-y-6 flex-auto">
                    <h3 class="text-xl font-medium text-gray-900 dark:text-white">👀 Seems Important</h3>
                    <div class="flex flex-col space-y-2">
                        {#each url_list as item, index (index)}
                            <div class="flex flex-row space-x-2 items-center rounded bg-slate-100 px-2 py-2">
                                <p class="grow text-sm font-medium text-gray-900 truncate dark:text-white line-clamp-1">
                                    {item}
                                </p>
                                <GradientButton href={item} color="cyanToBlue" size="xs">🌊 Surf</GradientButton>
                            </div>
                        {/each}
                    </div>
                </div>
                <div class="space-y-6 flex-auto">
                    <h3 class="text-xl font-medium text-gray-900 dark:text-white">🗂️ Files we found</h3>
                    <div class="flex flex-col space-y-2">
                        {#each file_list as item, index (index)}
                            <div class="flex flex-row space-x-2 items-center rounded bg-slate-100 px-2 py-2">
                                <p class="grow text-sm font-medium text-gray-900 truncate dark:text-white line-clamp-1">
                                    {item}
                                </p>
                                <GradientButton href={item} color="cyanToBlue" size="xs">🌊 Surf</GradientButton>
                            </div>
                        {/each}
                    </div>
                </div>
            </div>
            <div class="flex-1 flex h-full flex-col space-y-4 py-12 px-64">
                <div class="flex-auto flex-col space-y-4 overflow-y-auto">
                    {#if Array.isArray(data.messages)}
                        {#each data.messages as messages, index (index)}
                            {#if messages.speaker == 'user'}
                                <div class="w-full items-end flex">
                                    <div class="w-2/5"></div>
                                    <div class="w-3/5 p-4 bg-white rounded-lg border">
                                        <P color="text-green-700 dark:text-green-500">{messages.speaker}</P>
                                        {messages.message}
                                    </div>
                                </div>
                            {/if}
                            {#if messages.speaker == 'bot'}
                                <div class="w-full items-end flex">
                                    <div class="w-3/5 p-4 bg-white rounded-lg border">
                                        <P color="text-blue-700 dark:text-blue-500">{messages.speaker}</P>
                                        {#if messages.message === '...'}
                                            <Spinner color="blue" size="6"/>
                                        {:else}
                                            {messages.message}
                                        {/if}
                                    </div>
                                    <div class="w-2/5"></div>
                                </div>
                            {/if}
                        {/each}
                    {:else}
                        <p>No messages available</p>
                    {/if}
                </div>
                <div class=flex-none>
                    <form on:submit={handleSubmit}>
                        <ButtonGroup class="w-full">
                            <Input type="text" placeholder="💬 Chat here" size="lg" name="chat" bind:value={question} autocomplete="off"/>
                            <GradientButton color="cyanToBlue" size="lg" type="submit">Send</GradientButton>
                        </ButtonGroup>
                    </form>
                </div>
            </div>
        </div>
    {/if}
{/if}
