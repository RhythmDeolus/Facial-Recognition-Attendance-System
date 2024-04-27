<template>
    <div class="max-w-md mx-auto">
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
            <select @change="get_subjects()" v-model="course_id" id="courses" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="course_id in Object.keys(courses)" :value="course_id">{{courses[course_id].name}}</option>
            </select>
        </div>
        <div :key="rerenderSubjectKey" class="relative z-0 w-full mb-5 group">
            <label for="subjects" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a subject</label>
            <select v-model="subject_id" id="subjects" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="subject_id in Object.keys(subjects)" :value="subject_id">{{subjects[subject_id].name}}</option>
            </select>
        </div>
        <div :key="rerenderSemesterKey" class="relative z-0 w-full mb-5 group">
            <label for="semesters" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select a semester</label>
            <select v-model="semester_id" id="semesters" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                <option v-for="semester_id in Object.keys(semesters)" :value="semester_id">{{semesters[semester_id].start_date}}</option>
            </select>
        </div>
        <div class="relative max-w-sm">
            <div class="absolute inset-y-0 start-0 flex items-center ps-3.5 pointer-events-none">
                <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M20 4a2 2 0 0 0-2-2h-2V1a1 1 0 0 0-2 0v1h-3V1a1 1 0 0 0-2 0v1H6V1a1 1 0 0 0-2 0v1H2a2 2 0 0 0-2 2v2h20V4ZM0 18a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8H0v10Zm5-8h10a1 1 0 0 1 0 2H5a1 1 0 0 1 0-2Z"/>
                </svg>
            </div>
            <input datepicker id="something_weird_date" v-bind="class_date" type="text" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full ps-10 p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Select date">
        </div>
        
        <div class="max-w-[8rem] mx-auto">
            <label for="time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select start time:</label>
            <div class="relative">
                <div class="absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <input v-model="start_time" type="time" id="time" class="bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" min="09:00" max="18:00" value="00:00" required />
            </div>
        </div>

        <div class="max-w-[8rem] mx-auto">
            <label for="time" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Select end time:</label>
            <div class="relative">
                <div class="absolute inset-y-0 end-0 top-0 flex items-center pe-3.5 pointer-events-none">
                    <svg class="w-4 h-4 text-gray-500 dark:text-gray-400" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M2 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10S2 17.523 2 12Zm11-4a1 1 0 1 0-2 0v4a1 1 0 0 0 .293.707l3 3a1 1 0 0 0 1.414-1.414L13 11.586V8Z" clip-rule="evenodd"/>
                    </svg>
                </div>
                <input v-model="end_time" type="time" id="time" class="bg-gray-50 border leading-none border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" min="09:00" max="18:00" value="00:00" required />
            </div>
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
import { onMounted } from 'vue';
import { initFlowbite } from 'flowbite';
onMounted(() => {
    initFlowbite();
})

let class_date = null;
let start_time = null;
let end_time = null;

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

function checkForm(e) {
    let class_date = document.getElementById('something_weird_date').value;
    class_date = class_date.split('/')
    let temp = class_date[0];
    class_date[0] = class_date[1]
    class_date[1] = temp
    class_date = class_date.reverse();
    class_date = class_date.join('/');
    class_date = class_date.replace(/\//g, '-');
    console.log(class_date, start_time, end_time, semno, semester_id, course_id, subject_id);
    if (class_date && start_time && end_time && Number(semno) &&
        Number(semester_id) && Number(course_id)) {

        useFetch('/api_1/register_class', {
                'subject_id': subject_id,
                'course_id': course_id,
                'semester_id': semester_id,
                'semno': semno,
                'date': class_date,
                'start_time': start_time,
                'end_time': end_time
            }, 'POST').then((response) => {
                console.log(response)
                alert(response)
        });
    }
    
}
</script>
