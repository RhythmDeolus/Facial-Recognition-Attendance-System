<template>
    <div class="max-w-md mx-auto">
        <div :key="rerenderSemesterKey" class="relative z-0 w-full mb-5 group">
            <label for="semesters" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a semester</label>
            <select v-model="semester_id" id="semesters" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="semester_id in Object.keys(semesters)" :value="semester_id">{{semesters[semester_id].start_date}}</option>
            </select>
        </div>
        <button type="submit"
            @click="checkForm"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
    </div>
</template>

<script setup>
import { useAccessToken } from '@/composables/auth';
import { useFetch } from '@/composables/fetch';
import {ref} from 'vue';

let rerenderSemesterKey = ref(0);

function rerenderSemesters() {
    rerenderSemesterKey.value += 1;
}

let semesters = []
let semester_id = null;

useFetch('/api_1/get_semesters', {}, 'GET').then((response) => {
    console.log(response)
    semesters = response;
    rerenderSemesters();
});

function checkForm(e) {
    if (Number(semester_id)) {
        useFetch( '/api_1/register_academic_calendar', {
            'semester_id': semester_id,
        }, 'POST').then((response) => {
            alert(response)
        });
    } 
}
</script>
