<template>
    <div class="max-w-md mx-auto">
        <div class="relative z-0 w-full mb-5 group">
            <input type="text" name="floating_email" id="floating_email"
            v-model="name"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" " required />
            <label for="floating_email"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Name</label>
        </div>
        <div class="relative z-0 w-full mb-5 group">
            <input type="text" name="floating_rollno" id="floating_rollno"
            v-model="id"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" " required />
            <label for="floating_rollno"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Roll No.</label>
        </div>
        <div class="relative z-0 w-full mb-5 group">
            <input type="text" name="floating_rollno" id="floating_rollno"
            v-model="semno"
            class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
            placeholder=" " required />
            <label for="floating_rollno"
                class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Semester No.</label>
        </div>
        <div :key="rerenderCourseKey" class="relative z-0 w-full mb-5 group">
            <label for="courses" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a course</label>
            <select v-model="course_id" id="courses" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="course_id in Object.keys(courses)" :value="course_id">{{courses[course_id].name}}</option>
            </select>
        </div>
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
let name = null;
let id = null;
let semno = null;

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
    if (name && Number(id) && Number(semno) &&
        Number(semester_id) && Number(course_id)) {
        useFetch( '/api_1/register_student', {
            'name': name,
            'id': id,
            'course_id': course_id,
            'semester_id': semester_id,
            'semno': semno
        }, 'POST').then((response) => {
            console.log(response);
            alert(response);
        });
    }
    e.preventDefault(); 
}
</script>
