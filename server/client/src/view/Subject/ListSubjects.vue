<template>
    <div :key="rerenderkey" class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div :key="rerenderCourseKey" class="relative z-0 w-full mb-5 group">
            <label for="courses" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a course</label>
            <select @change="fetchAttendanceData()" v-model="course_id" id="courses" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="course_id in Object.keys(courses)" :value="course_id">{{courses[course_id].name}}</option>
            </select>
        </div>
        <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
            <label for="table-search" class="sr-only">Search</label>
            <div class="relative">
                <div
                    class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
                    <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor"
                        viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                        <path fill-rule="evenodd"
                            d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                            clip-rule="evenodd"></path>
                    </svg>
                </div>
                <input v-model="search" type="text" id="table-search"
                    class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                    placeholder="Search for items">
            </div>
        </div>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">
                    Subject ID
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Subject Name
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in computedSubjects" :key="item[0]"
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[0] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[1] }}</th>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script setup>
import { useFetch } from '@/composables/fetch';
import { computed } from 'vue';


import {ref} from 'vue';

let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}

let rerenderCourseKey = ref(0);

function rerenderCourses() {
    rerenderCourseKey.value += 1;
}

let courses = [];
let course_id = null;
useFetch('/api_1/get_courses', {}, 'GET').then((response) => {
    console.log(response)
    courses = response;
    rerenderCourses();
});

let subjects = ref([]);
let search = ref('');

let computedSubjects = computed(() => {
    let term = search.value.toLowerCase();
    if (term)
    return subjects.value.filter((subject) => {
        return subject[0].toLowerCase().includes(term) ||
        subject[1].toLowerCase().includes(term);
    });
    return subjects.value;
});


async function fetchAttendanceData() {
    try { 
        let subjectData = await useFetch('/api_1/get_subjects_for_course', {
        course_id: course_id
        }, 'GET');
        console.log(subjectData);
        setTable(subjectData);
        rerender()
    } catch (error) {
        console.error(error);
    }
}

function setTable(subjectData) {
    subjects.value = [];
    let subjectIds = Object.keys(subjectData);
    for (let id of subjectIds) {
        let data = []
        data.push(id);
        data.push(subjectData[id].name);
        subjects.value.push(data);
    }
}


</script>
