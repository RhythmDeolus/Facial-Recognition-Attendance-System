<template>    
<nav class="bg-white border-gray-200 dark:bg-gray-900">
    <div class="flex flex-wrap justify-between items-center mx-auto max-w-screen-xl p-4">
        <a href="/" class="flex items-center space-x-3 rtl:space-x-reverse">
            <img src="../assets/logo.png" class="h-8" alt="Flowbite Logo" />
            <span class="self-center text-2xl font-semibold whitespace-nowrap dark:text-white">Attendance System</span>
        </a>
        <div class="flex items-center space-x-6 rtl:space-x-reverse">
            <a href="tel:5541251234" class="text-sm  text-gray-500 dark:text-white hover:underline">(555) 412-1234</a>
            <router-link v-if="!useCheckAuth()" to="/login" class="text-sm  text-blue-600 dark:text-blue-500 hover:underline">Login</router-link>
            <router-link v-else to="/logout" class="text-sm  text-blue-600 dark:text-blue-500 hover:underline">Logout</router-link>
        </div>
    </div>
</nav>

<button data-drawer-target="sidebar-multi-level-sidebar" data-drawer-toggle="sidebar-multi-level-sidebar" aria-controls="sidebar-multi-level-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
   <span class="sr-only">Open sidebar</span>
   <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
   <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
   </svg>
</button>

    <aside id="sidebar-multi-level-sidebar" class="absolute left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0 top-auto" style="{top: auto}" aria-label="Sidebar">
   <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
      <ul class="space-y-2 font-medium">
        <template v-for="item in linkStruct">
            <li v-if="item[1] instanceof Array">
                        <button type="button" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700" :onclick="handle_toggle" :aria-controls="item[0]" :data-collapse-toggle="item[0]">
                <svg v-if='item[0] in svgs' v-html="svgs[item[0]]" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" :fill="fills[item[0]]" viewBox="0 0 23 23" class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white">
                            </svg>
                  <svg v-else class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 21">
                     <path d="M15 12a1 1 0 0 0 .962-.726l2-7A1 1 0 0 0 17 3H3.77L3.175.745A1 1 0 0 0 2.208 0H1a1 1 0 0 0 0 2h.438l.6 2.255v.019l2 7 .746 2.986A3 3 0 1 0 9 17a2.966 2.966 0 0 0-.184-1h2.368c-.118.32-.18.659-.184 1a3 3 0 1 0 3-3H6.78l-.5-2H15Z"/>
                  </svg>
                            <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">{{item[0]}}</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/> </svg>
            </button>
            <ul :id="item[0]" class="hidden py-2 space-y-2">
                  <li v-for="link in item[1]">
                                <router-link :to="link[1]" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{link[0]}}</router-link>
                  </li>
            </ul>
            </li>
            <li v-else>
                <router-link class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"  :to="item[1]">
                            <span class="ms-3">{{item[0]}}</span></router-link> 
            </li>
        </template>
      </ul>
   </div>
</aside>

<div class="p-4 sm:ml-64">
        <slot></slot>
</div>
</template>

<script setup>
import { useCheckAuth } from '@/composables/auth';

function handle_toggle(e){
    let target = e.target;
    if (target.tagName !== 'BUTTON')  target = target.closest('button');
    const collapse = target.getAttribute('data-collapse-toggle');
    console.log(target, collapse);
    const element = document.getElementById(collapse);
    element.classList.toggle('hidden');
}

const svgs = {
    'Attendance': `<path fill-rule="evenodd" d="M6 2a2 2 0 0 0-2 2v15a3 3 0 0 0 3 3h12a1 1 0 1 0 0-2h-2v-2h2a1 1 0 0 0 1-1V4a2 2 0 0 0-2-2h-8v16h5v2H7a1 1 0 1 1 0-2h1V2H6Z" clip-rule="evenodd"/>`,
    'Student': `<path fill-rule="evenodd" d="M12 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8Zm-2 9a4 4 0 0 0-4 4v1a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2v-1a4 4 0 0 0-4-4h-4Z" clip-rule="evenodd"/>`,
    'Course': `<path fill-rule="evenodd" d="M11 4.717c-2.286-.58-4.16-.756-7.045-.71A1.99 1.99 0 0 0 2 6v11c0 1.133.934 2.022 2.044 2.007 2.759-.038 4.5.16 6.956.791V4.717Zm2 15.081c2.456-.631 4.198-.829 6.956-.791A2.013 2.013 0 0 0 22 16.999V6a1.99 1.99 0 0 0-1.955-1.993c-2.885-.046-4.76.13-7.045.71v15.081Z" clip-rule="evenodd"/>`,
    'Subject': `<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.779 17.779 4.36 19.918 6.5 13.5m4.279 4.279 8.364-8.643a3.027 3.027 0 0 0-2.14-5.165 3.03 3.03 0 0 0-2.14.886L6.5 13.5m4.279 4.279L6.499 13.5m2.14 2.14 6.213-6.504M12.75 7.04 17 11.28"/>`,
    'Semester': `<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z"/>`,
    'Academic Calendar': `<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 10h16m-8-3V4M7 7V4m10 3V4M5 20h14a1 1 0 0 0 1-1V7a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v12a1 1 0 0 0 1 1Zm3-7h.01v.01H8V13Zm4 0h.01v.01H12V13Zm4 0h.01v.01H16V13Zm-8 4h.01v.01H8V17Zm4 0h.01v.01H12V17Zm4 0h.01v.01H16V17Z"/>`,
    'Timetable': `<path fill-rule="evenodd" d="M10 5a2 2 0 0 0-2 2v3h2.4A7.48 7.48 0 0 0 8 15.5a7.48 7.48 0 0 0 2.4 5.5H5a2 2 0 0 1-2-2v-7a2 2 0 0 1 2-2h1V7a4 4 0 1 1 8 0v1.15a7.446 7.446 0 0 0-1.943.685A.999.999 0 0 1 12 8.5V7a2 2 0 0 0-2-2Z" clip-rule="evenodd"/>
  <path fill-rule="evenodd" d="M10 15.5a5.5 5.5 0 1 1 11 0 5.5 5.5 0 0 1-11 0Zm6.5-1.5a1 1 0 1 0-2 0v1.5a1 1 0 0 0 .293.707l1 1a1 1 0 0 0 1.414-1.414l-.707-.707V14Z" clip-rule="evenodd"/>`,
    'Classes' : `<path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m10.827 5.465-.435-2.324m.435 2.324a5.338 5.338 0 0 1 6.033 4.333l.331 1.769c.44 2.345 2.383 2.588 2.6 3.761.11.586.22 1.171-.31 1.271l-12.7 2.377c-.529.099-.639-.488-.749-1.074C5.813 16.73 7.538 15.8 7.1 13.455c-.219-1.169.218 1.162-.33-1.769a5.338 5.338 0 0 1 4.058-6.221Zm-7.046 4.41c.143-1.877.822-3.461 2.086-4.856m2.646 13.633a3.472 3.472 0 0 0 6.728-.777l.09-.5-6.818 1.277Z"/>`,
    'Contact Us': `<path d="M7.978 4a2.553 2.553 0 0 0-1.926.877C4.233 6.7 3.699 8.751 4.153 10.814c.44 1.995 1.778 3.893 3.456 5.572 1.68 1.679 3.577 3.018 5.57 3.459 2.062.456 4.115-.073 5.94-1.885a2.556 2.556 0 0 0 .001-3.861l-1.21-1.21a2.689 2.689 0 0 0-3.802 0l-.617.618a.806.806 0 0 1-1.14 0l-1.854-1.855a.807.807 0 0 1 0-1.14l.618-.62a2.692 2.692 0 0 0 0-3.803l-1.21-1.211A2.555 2.555 0 0 0 7.978 4Z"/>`

};

const fills = {
    'Attendance': 'currentColor',
    'Student': 'currentColor',
    'Course': 'currentColor',
    'Subject': 'none',
    'Semester': 'none',
    'Calendar': 'none',
    'Timetable': 'currentColor',
    'Classes': 'none',
    'Contact Us': 'currentColor'
};

const linkStruct = [
    [ 'Attendance' , [
       ['List Attendance' , '/attendance'],
    ]],
    [ 'Student' , [
       ['Register Student' , '/studentregistration'],
       [ 'Register Face' , '/cam' ],
       [ 'List Students' , '/list_students' ],
    ]],
    [ 'Course' , [
       ['Register Course' , '/register_course'],
       ['List Courses' , '/list_courses'],
    ]],
    [ 'Subject' , [
       ['Register Subject' , '/register_subject'],
       ['List Subjects' , '/list_subjects'],
    ]],
    [ 'Semester' , [
       ['Register Semester' , '/register_semester'],
       ['List Semesters' , '/list_semesters'],
    ]],
    [ 'Academic Calendar' , [
       ['Register Calendar' , '/register_calendar'],
       ['Assign Calendar' , '/assign_calendar'],
       ['List Calendars' , '/list_calendars'],
    ]],
    [ 'Timetable' , [
       ['Register Timetable' , '/register_timetable'],
       ['List Timetables' , '/list_timetables'],
    ]],
    [ 'Classes' , [
       ['Register Class' , '/register_class'],
       ['List Classes' , '/list_classes'],
    ]],
    [ 'Contact Us' , [
       [ 'About' , '/about',],
       [ 'Contributors' , '/contact' ],
    ]],
];

</script>

<style scoped>
aside {
    top: auto;
}
</style>
