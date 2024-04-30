<template>
    <div :key="rerenderkey" class="relative overflow-x-auto shadow-md sm:rounded-lg">
        <div class="flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
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
            <div>
        <!--     <label for="table-search" class="sr-only">Search</label> -->
        <!--     <div class="relative"> -->
        <!--         <div -->
        <!--             class="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none"> -->
        <!--             <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor" -->
        <!--                 viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"> -->
        <!--                 <path fill-rule="evenodd" -->
        <!--                     d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z" -->
        <!--                     clip-rule="evenodd"></path> -->
        <!--             </svg> -->
        <!--         </div> -->
        <!--         <input type="text" id="table-search" -->
        <!--             class="block p-2 ps-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" -->
        <!--             placeholder="Search for items"> -->
        <!--     </div> -->
        </div>
        <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th scope="col" class="px-6 py-3">
                        Student Name
                    </th>
                    <th scope="col" class="px-6 py-3">
                        Roll Number
                    </th>
                    <th v-for="class_c in classes" :key="class_c">{{ classesDict[class_c].date }}<br/>
                        {{ (classesDict[class_c].start_time).toString().slice(0, -3) }} - {{ (classesDict[class_c].end_time).toString().slice(0,-3) }} 
                    </th> </tr>
            </thead>
            <tbody>
                <tr v-for="(n, index) in studentIdList.length" :key="index"
                    class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600">
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ studentdata[studentIdList[index]]?.name }}</th>
                    <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white"
                        style="color:white">{{ studentIdList[index] }}</th>
                    <td class="px-6 py-4" v-for="attendance in studentAttendance[studentIdList[index]]">
                        <div bgcolor="green" v-if="attendance">✅</div>
                        <div bgcolor="red" v-if="!attendance">❌</div>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
    </div>
</template>

<script setup>
import { useFetch } from '@/composables/fetch';
import {ref} from 'vue';
import { onMounted } from 'vue';
import { initFlowbite } from 'flowbite';
onMounted(() => {
    initFlowbite();
})
Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
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


let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}

let classes = []
let classesDict = {}
let studentIdList = []
let studentAttendance = {}


let studentdata = {
    1: {name: 'rhythm'},
    2: {name:'vasu'},
    3: {name:'Amal'}
}
let attendanceData = {
    '1': { id: 1, name: 'Rhythm', day: 1 },
    '2': { id: 2, name: 'Vasu', day: 2 },
    '3': { id: 3, name: 'Amal', day: 5 },
}
let classesData = {
}

async function fetchAttendanceData() {
    try { 
        if (!Number(subject_id) || !Number(semester_id)) return;
        studentdata = await useFetch('/api_1/get_students_for_course', {
        course_id: course_id
        }, 'GET');
        attendanceData = await useFetch('/api_1/get_attendance_for_subject', {
            subject_id: subject_id
        }, 'GET');
        classesData = await useFetch('/api_1/get_classes_for_subject', {
            subject_id: subject_id,
            semester_id: semester_id
        }, 'GET');
        console.log(studentdata, attendanceData)
        setTable(studentdata, attendanceData, classesData);
        rerender()
    } catch (error) {
        console.error(error);
    }
}

function setTable(studentdata, attendanceData, classesData) {
    studentAttendance= {}
    studentIdList= Object.keys(studentdata)
    classes= Object.keys(classesData)
    classesDict = classesData

    let failed = false;

    for (let id of studentIdList) {
        studentAttendance[id] = []
        for (let c in classesData) {
            let idx = -1;
            try {
                idx = Object.values(attendanceData).findIndex(a => a['class_id'] == c);
            } catch(e) {
                console.log(e);
                failed = true;
                break;
            }
            if (idx >= 0) {
                studentAttendance[id].push(true);
            } else {
                studentAttendance[id].push(false);
            }
        }
        if (failed) break;
    }
}
</script>
