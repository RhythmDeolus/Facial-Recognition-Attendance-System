<template>
    <div :key="rerenderkey" class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div :key="rerenderkey" class="relative z-0 w-full mb-5 group">
            <label for="semesters" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a semester</label>
            <select @change="fetchAttendanceData()" v-model="semester_id" id="semesters" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="semester_id in Object.keys(semesters)" :value="semester_id">{{displaySemester(semesters, semester_id)}}</option>
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
                    <th scope="col" class="px-6 py-3">
                        Classes Attended
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Classes Missed
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Attendance Percentage
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in computedAttendances" :key="item[0]"
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[0] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[1] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[2] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[3] }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[4] }}</th>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script setup>

import { useFetch } from '@/composables/fetch';
import { computed } from 'vue';

import {ref} from 'vue';

function displaySemester(semesters, semester_id) {
    return `${new Date(semesters[semester_id].start_date).toLocaleString()} - ${new Date(semesters[semester_id].end_date).toLocaleString()}`;
}

let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}

let semesters = []

let semester_id = null;

useFetch('/api_1/get_semesters_student', {}, 'GET').then((response) => {
    console.log(response)
    semesters = response;
    rerender();
});


let attendances = ref([]);
let search = ref('');

let computedAttendances = computed(() => {
    let term = search.value.toLowerCase();
    if (term)
    return attendances.value.filter((attendance) => {
        return attendance[1].toLowerCase().includes(term);
    });
    return attendances.value;
});


async function fetchAttendanceData() {
    try { 
        if (!semester_id) {
            return;
        }
        let attendanceData = await useFetch('/api_1/get_attendance_for_student', {}, 'GET');
        let subject_classes = {}
        for (let attendance of Object.values(attendanceData)) {
            if (!subject_classes[attendance.subject_id]) {
            let classes = await useFetch('/api_1/get_classes_for_subject_student', {
                subject_id: attendance.subject_id,
                semester_id: semester_id
            }, 'GET');
            subject_classes[attendance.subject_id] = classes;
            }
        }
        setTable(attendanceData, subject_classes);
        rerender()
    } catch (error) {
        console.error(error);
    }
}


function setTable(attendanceData, subject_classes) {
    attendances.value = [];

    for (let subject in subject_classes) {
        let total_classes = Object.keys(subject_classes[subject]).length;
        if (total_classes == 0) {
            continue;
        }
        let attended_classes = 0;
        let subject_name = "";
        for (let attendance of Object.values(attendanceData)) {
            if (attendance.subject_id == subject) {
                subject_name = attendance.subject_name;
                attended_classes += 1;
            }
        }
        let data = []
        data.push(subject);
        data.push(subject_name);
        data.push(attended_classes);
        data.push(total_classes - attended_classes);
        data.push((attended_classes / total_classes) * 100);
        attendances.value.push(data);
    }
}





</script>
