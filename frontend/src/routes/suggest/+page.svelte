<script>
    import { onMount } from 'svelte';
    import { fetchData } from '$lib/fetchData.js';
    import { fetchDataQuery } from '$lib/fetchDataQuery.js';
    import { goto } from '$app/navigation';

    import { Input, Label, InputAddon, ButtonGroup, GradientButton, Alert } from 'flowbite-svelte';
    import { Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox, TableSearch } from 'flowbite-svelte';

    
    // get suggested schools lists
    let suggestedSchools = [];
    let showAlert = false;
    let alertMessage = '';
    let alertType = '';

    async function loadSuggestedSchools() {
        try {
            const data = await fetchData("api/suggested_school_list", "GET");
            suggestedSchools = data.reverse().slice(0, 5); // 최신순 정렬 후 5개 항목만 저장
        } catch (error) {
            console.error('Failed to load suggested schools:', error);
        }
    }

    onMount(() => {
        loadSuggestedSchools();
    });

    let school_link = "";
    let user_name = "";
    let school_name = "";

    // post suggested school
    async function postSuggestedSchool() {
        if (user_name && school_name) {
            try {
                console.log(user_name, school_name, school_link);
                const data = await fetchDataQuery("api/user_suggest_school", "POST", { user_name: user_name, school_name: school_name, school_link: school_link});
                console.log(data);
                showAlert = true;
                alertMessage = 'Successfully posted the suggested school!';
                alertType = 'success';
                loadSuggestedSchools();
            } catch (error) {
                console.error('Failed to post suggested school:', error);
                showAlert = true;
                alertMessage = 'Failed to post suggested school!';
                alertType = 'error';
            }
        }
    }

    function handleSubmit(event) {
        event.preventDefault();
        postSuggestedSchool();
    }

    const closeAlert = () => {
        alert('Clicked closeAlert.');
    };

    // routing to home
    function navigateHome() {
        goto('/');
    }

</script>

<div class="flex flex-col items-center justify-center h-screen w-screen bg-neutral-100">
    {#if showAlert}
        <Alert dismissable color="blue" on:close={closeAlert => showAlert = false} class="fixed top-0 left-1/2 transform -translate-x-1/2 mt-4 z-50">
            {alertMessage}
        </Alert>
    {/if}
    <div class="flex flex-row space-x-2 py-4 px-6 w-full">
        <p class="text-xl font-medium text-gray-900 dark:text-white w-full text-grayCustom">🌊 SurfSchool</p>
        <button class="w-6 h-6" on:click={navigateHome}>
            <img src="/home.svg" alt="Logo" class="home" />
        </button>
    </div>
    <div class="flex flex-col space-y-10 items-center justify-center container mx-auto w-fit h-full">
        <p class="text-6xl">Plz Suggest Your Schools</p>
        <div class="flex flex-none w-full flex-col space-y-8 justify-start bg-grayCustomSide px-6 py-8 rounded-lg border">
            <form class="flex flex-col space-y-4 items-center w-full" on:submit={handleSubmit}>
                <div class="flex flex-row space-x-4 w-full">
                    <div class="w-full">
                        <Label for="user_name" class="mb-2">Your id</Label>
                        <Input type="text" id="user_name" placeholder="John" bind:value={user_name} required />
                    </div>
                    <div class="w-full">
                        <Label for="school_name" class="mb-2">School name</Label>
                        <Input type="text" id="school_name" placeholder="University" bind:value={school_name} required />
                    </div>
                </div>
                <div class="w-full">
                    <Label for="school_link" class="mb-2">School's link</Label>
                    <ButtonGroup class="w-full">
                        <InputAddon>http://</InputAddon>
                        <Input type="text" id="school_link" placeholder="example.com" bind:value={school_link} required />
                    </ButtonGroup>
                </div>
                <GradientButton type="submit" color="cyanToBlue" class="w-40 text-base">🌊 Surf</GradientButton>        
            </form>
        </div>
    </div>
    <div class="flex flex-col space-y-2 w-full py-4 px-6">
        <p class="font-medium"> recent 5 submition</p>
        <Table class="min-w-full mt-4">
            <TableHead>
                <TableHeadCell>User Name</TableHeadCell>
                <TableHeadCell>School Name</TableHeadCell>
                <TableHeadCell class="w-full">School Link</TableHeadCell>
            </TableHead>
            <TableBody>
                {#each suggestedSchools as school}
                    <TableBodyRow>
                        <TableBodyCell>{school.user_name}</TableBodyCell>
                        <TableBodyCell>{school.school_name}</TableBodyCell>
                        <TableBodyCell>{school.school_link}</TableBodyCell>
                    </TableBodyRow>
                {/each}
            </TableBody>
        </Table>
    </div>
</div>
