<template>
    <div :key="rerenderkey" class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div :key="rerenderSemesterKey" class="relative z-0 w-full mb-5 group">
            <label for="semesters" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a semester</label>
            <select @change="fetchAttendanceData()" v-model="semester_id" id="semesters" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="semester_id in Object.keys(semesters)" :value="semester_id">{{displaySemester(semesters, semester_id)}}</option>
            </select>
        </div>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">
                    Timetable ID
                    </th>
                    <th scope="col" class="px-6 py-3">
                    Course ID
                    </th>
                    <th scope="col" class="px-6 py-3">
                    Semester ID
                    </th>
                    <th scope="col" class="px-6 py-3">
                    Semester No.
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in computedTimetables" :key="item[0]"
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[0] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[1] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[2] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[3] }}</th>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script setup>
import { useFetch } from '@/composables/fetch';
import { computed } from 'vue';

function displaySemester(semesters, semester_id) {
    return `${new Date(semesters[semester_id].start_date).toLocaleString()} - ${new Date(semesters[semester_id].end_date).toLocaleString()}`;
}


import {ref} from 'vue';

let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}

let rerenderSemesterKey = ref(0);

function rerenderSemesters() {
    rerenderSemesterKey.value += 1;
}

let semesters = [];
let semester_id = null;
useFetch('/api_1/get_semesters', {}, 'GET').then((response) => {
    console.log(response)
    semesters = response;
    rerenderSemesters();
});

let timetables = ref([]);
let search = ref('');

let computedTimetables = computed(() => {
    if (semester_id)
    return timetables.value.filter((timetable) => {
        return timetable[2] == semester_id;
    });
    return timetables.value;
});


async function fetchAttendanceData() {
    try { 
        let timetableData = await useFetch('/api_1/get_timetables', {
        }, 'GET');
        console.log(timetableData);
        setTable(timetableData);
        rerender()
    } catch (error) {
        console.error(error);
    }
}

fetchAttendanceData();

function setTable(timetableData) {
    timetables.value = [];
    let timetableIds = Object.keys(timetableData);
    for (let id of timetableIds) {
        let data = []
        data.push(id);
        data.push(timetableData[id].course_id);
        data.push(timetableData[id].semester_id);
        data.push(timetableData[id].sem_no);
        timetables.value.push(data);
    }
}


</script>
