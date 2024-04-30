<template>
    <div :key="rerenderkey" class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div :key="rerenderCourseKey" class="relative z-0 w-full mb-5 group">
            <label for="courses" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a course</label>
            <select @change="get_subjects()" v-model="course_id" id="courses" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="course_id in Object.keys(courses)" :value="course_id">{{courses[course_id].name}}</option>
            </select>
        </div>
        <div :key="rerenderSubjectKey" class="relative z-0 w-full mb-5 group">
            <label for="subjects" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a subject</label>
            <select @change="fetchAttendanceData()" v-model="subject_id" id="subjects" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="subject_id in Object.keys(subjects)" :value="subject_id">{{subjects[subject_id].name}}</option>
            </select>
        </div>
        <div :key="rerenderSemesterKey" class="relative z-0 w-full mb-5 group">
            <label for="semesters" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a semester</label>
            <select @change="fetchAttendanceData()" v-model="semester_id" id="semesters" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="semester_id in Object.keys(semesters)" :value="semester_id">{{semesters[semester_id].start_date}}</option>
            </select>
        </div>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">
                    Class ID
                    </th>
                    <th scope="col" class="px-6 py-3">
                    Date
                    </th>
                    <th scope="col" class="px-6 py-3">
                    Start Time
                    </th>
                    <th scope="col" class="px-6 py-3">
                        End Time
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Calendar ID </th>
                    <th scope="col" class="px-6 py-3">
                        Timetable ID
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in classs" :key="item[0]"
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
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ item[5] }}</th>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script setup>
import { useFetch } from '@/composables/fetch';
import { computed } from 'vue';

function displaySubject(subjects, subject_id) {
    return `${new Date(subjects[subject_id].start_date).toLocaleString()} - ${new Date(subjects[subject_id].end_date).toLocaleString()}`;
}

let rerenderCourseKey = ref(0);

function rerenderCourses() {
    rerenderCourseKey.value += 1;
}
let courses = []
let course_id = null;

useFetch('/api_1/get_courses', {}, 'GET').then((response) => {
    console.log(response)
    courses = response;
    rerenderCourses();
});

let rerenderSubjectKey = ref(0);

function rerenderSubjects() {
    rerenderSubjectKey.value += 1;
}

let subjects = []
let subject_id = null;

function get_subjects() {
    if (!Number(course_id)) return;
    useFetch('/api_1/get_subjects_for_course', {
        course_id: course_id
    }, 'GET').then((response) => {
        console.log(response)
        subjects = response;
        rerenderSubjects();
    });
}

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

import {ref} from 'vue';

let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}


let classs = ref([]);
let search = ref('');



async function fetchAttendanceData() {
    try { 
        if (!Number(subject_id) || !Number(semester_id)) return;
        let classData = await useFetch('/api_1/get_classes_for_subject', {
            subject_id: subject_id,
            semester_id: semester_id
        }, 'GET');
        console.log(classData);
        setTable(classData);
        rerender()
    } catch (error) {
        console.error(error);
    }
}

function setTable(classData) {
    classs.value = [];
    let classIds = Object.keys(classData);
    for (let id of classIds) {
        let data = []
        data.push(id);
        data.push(classData[id].date);
        data.push(classData[id].start_time);
        data.push(classData[id].end_time);
        data.push(classData[id].academic_calendar_id);
        data.push(classData[id].timetable_id);
        classs.value.push(data);
    }
}


</script>
