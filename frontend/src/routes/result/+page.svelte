<script>
    import { onMount } from 'svelte';
    import { fetchDataQuery } from '$lib/fetchDataQuery.js';
    import { GradientButton, Modal, Label, Input, Helper, ButtonGroup, P, Spinner, Textarea, Alert } from 'flowbite-svelte';

    import { page } from '$app/stores';
    import { goto } from '$app/navigation';
    import { writable } from 'svelte/store';

    // small screen
    let isSmallScreen = false;

    onMount(() => {
        const updateScreenSize = () => {
            isSmallScreen = window.innerWidth <= 1300;
        };

        window.addEventListener('resize', updateScreenSize);
        updateScreenSize();

        return () => {
            window.removeEventListener('resize', updateScreenSize);
        };
    });

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

    // routing to home
    function navigateHome() {
        goto('/');
    }

    // routing to join
    let path = "https://github.com/be-garam/FireSchool"

    // open the link in a new tab
    function moveToLink(link) {
        console.log(link);
        try {
            window.open(link, '_blank');
        } catch (err) {
            alertMessage = 'Failed to open link';
            alertType = 'error';
        }
    }

    // modal for error report
    let formModal = writable(false);
    let errorReport = '';
    
    // setting for alert
    let alertMessage = '';
    let alertType = 'success';
    let showAlert = writable(false);

    // post error to dev
    async function postError() {
        try {
            console.log('Error:', errorReport);
            console.log('School:', school_name);
            const errorResponse = await fetchDataQuery("api/user_report_error", "POST", { school_name: school_name, error: errorReport });
            console.log(errorResponse);
            if (errorResponse.result === "error reported successfully") {
                alertMessage = 'Successfully posted the error to Dev!';
                alertType = 'success';
                showAlert.set(true);
                formModal.set(false); // 모달 닫기
            } else {
                throw new Error('Unexpected response from server');
            }
        } catch (err) {
            console.error('Failed to post error:', err);
            alertMessage = 'Failed to post error to Dev!';
            alertType = 'error';
            showAlert.set(true);
        }
    }

    function handleErrorSubmit(event) {
        event.preventDefault();
        postError();
    }

    function openFormModal() {
        formModal.set(true);
    }

    function closeAlert() {
        showAlert.set(false);
    }

</script>

<style>
    .home {
      cursor: pointer;
    }
</style>

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
        {#if isSmallScreen}
            <div class="flex items-center justify-center h-screen w-screen bg-neutral-100">
                <p class="text-6xl"> 🫷 Strech me!😖 🫸</p>
            </div>
        {:else}
            <div class="flex items-center justify-center h-screen w-screen bg-white">
                {#if $showAlert}
                    <Alert dismissable color="blue" on:close={closeAlert => showAlert = false} class="fixed top-0 left-1/2 transform -translate-x-1/2 mt-4 z-50">
                        {alertMessage}
                    </Alert>
                {/if}
                <div class="flex flex-none w-80 h-full flex-col space-y-8 justify-start bg-grayCustomSide px-6">
                    <div class="flex flex-row space-x-2 py-4">
                        <p class="text-xl font-medium text-gray-900 dark:text-white w-full text-grayCustom">🌊 SurfSchool</p>
                        <button class="w-6 h-6" on:click={navigateHome}>
                            <img src="/home.svg" alt="Logo" class="home" />
                        </button>
                    </div>
                    <div class="flex-none">
                        <h3 class="text-l font-medium text-grayCustomDark dark:text-white py-2">🗝️ Your school's keyword</h3>
                        <div class="flex flex-row space-x-2">
                            {#each keyword_list as keyword (keyword)}
                                <div class="w-fit rounded bg-grayCustomCard px-2 py-2">
                                    <p class="grow font-medium text-xl text-slate-950 truncate">
                                        {keyword}
                                    </p>
                                </div>
                            {/each}
                        </div> 
                    </div>
                    <div class="flex-none">
                        <h3 class="text-l font-medium text-grayCustomDark py-2">👀 Seems Important</h3>
                        <div class="flex flex-col space-y-2">
                            {#each url_list as item, index (index)}
                                <button class="flex flex-row space-x-2 items-center rounded bg-grayCustomCard px-2 py-2 rounded-lg" on:click={() => moveToLink(item)}>
                                    <p class="grow text-sm font-normal text-lg text-slate-950 truncate max-w-56">
                                        {item}
                                    </p>
                                    <button class="w-5 h-5">
                                        <img src="/open.svg" alt="Logo" class="open" />
                                    </button>
                                </button>
                            {/each}
                        </div>
                    </div>
                    <div class="grow">
                        <h3 class="text-l font-medium text-grayCustomDark py-2">🗂️ Files we found</h3>
                        <div class="flex flex-col space-y-2">
                            {#each file_list as item, index (index)}
                                <button class="flex flex-row space-x-2 items-center rounded bg-grayCustomCard px-2 py-2 rounded-lg" on:click={() => moveToLink(item)}>
                                    <p class="grow text-sm font-normal text-lg text-slate-950 truncate max-w-56">
                                        {item}
                                    </p>
                                    <button class="w-5 h-5">
                                        <img src="/open.svg" alt="Logo" class="open" />
                                    </button>
                                </button>
                            {/each}
                        </div>
                    </div>
                    <div class="flex-none py-8">
                        <GradientButton type="submit" color="cyanToBlue" class="w-full" href={path}>🌊 Want to join?</GradientButton>        
                    </div>
                </div>
                <div class="flex-1 flex h-full flex-col">
                    <div class="flex flex-row space-x-2 px-6 py-4">
                        <p class="text-xl font-medium text-gray-900 dark:text-white w-full text-grayCustom">{school_name}</p>
                        <button class="w-6 h-6" on:click={openFormModal}>
                            <img src="/error.svg" alt="Logo" class="error" />
                        </button>
                    </div>
                    <div class="flex-auto overflow-y-auto px-60">
                        <div class="flex-col space-y-4 w-full h-full">
                            {#if Array.isArray(data.messages)}
                                {#each data.messages as messages, index (index)}
                                    {#if messages.speaker == 'user'}
                                        <div class="w-full items-end flex">
                                            <div class="w-2/5"></div>
                                            <div class="w-3/5 p-4 bg-grayCustomLight rounded-lg border">
                                                <P color="text-green-700 dark:text-green-500">{messages.speaker}</P>
                                                {messages.message}
                                            </div>
                                        </div>
                                    {/if}
                                    {#if messages.speaker == 'bot'}
                                        <div class="w-full items-end flex">
                                            <div class="w-4/5 p-4 rounded-lg">
                                                <P color="text-blue-700 dark:text-blue-500">{messages.speaker}</P>
                                                {#if messages.message === '...'}
                                                    <Spinner color="blue" size="6"/>
                                                {:else}
                                                    {messages.message}
                                                {/if}
                                            </div>
                                            <div class="w-1/5"></div>
                                        </div>
                                    {/if}
                                {/each}
                            {:else}
                                <p>No messages available</p>
                            {/if}
                        </div>
                    </div>
                    <div class="flex px-60 py-4">
                        <div class="flex flex-col space-y-2 items-center justify-center w-full">
                            <form on:submit={handleSubmit} class="w-full">
                                <ButtonGroup class="w-full grayCustom">
                                    <Input type="text" placeholder="💬 Chat here" size="lg" name="chat" bind:value={question} autocomplete="off"/>
                                    <GradientButton color="cyanToBlue" size="lg" type="submit">Send</GradientButton>
                                </ButtonGroup>
                            </form>
                            <Helper class="text-sm">
                                Always remember that GPT results may be inaccurate.
                            </Helper>
                        </div>
                    </div>
                </div>
            </div>

            <Modal bind:open={$formModal} size="xs" autoclose={false} class="w-full">
                <form class="flex flex-col space-y-6" action="#" on:submit={handleErrorSubmit}>
                    <h3 class="mb-4 text-xl font-medium text-gray-900 dark:text-white">Help Developer to check Issue</h3>
                    <div class="flex flex-col space-y-2">
                        <Label for="errorReport" class="mb-2">Your message</Label>
                        <Textarea id="errorReport" placeholder="Error you've faced" rows="4" bind:value={errorReport} />
                    </div>  
                    <GradientButton type="submit" color="cyanToBlue" class="w-full">Send Error to Dev</GradientButton>
                </form>
            </Modal>
        {/if}
    {/if}
{/if}
