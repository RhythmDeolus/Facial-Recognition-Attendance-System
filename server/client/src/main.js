import { VueElement, createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHashHistory, createWebHistory } from 'vue-router'
import HomeVue from './view/Home.vue'
import AboutVue from './view/About.vue'
import LoginVue from './view/Login.vue'
import ContactVue from './view/Contact.vue'
import AttendanceVue from './view/Attendance.vue'
import AdminLoginVue from './view/AdminLogin.vue'
import StudentRegistrationVue from './view/StudentRegistration.vue'
import CamVue from './view/Cam.vue'
import RegisterCourseVue from './view/Course/RegisterCourse.vue'
import ListCoursesVue from './view/Course/ListCourses.vue'
import RegisterSubjectVue from './view/Subject/RegisterSubject.vue'
import ListSubjectsVue from './view/Subject/ListSubjects.vue'
import RegisterSemesterVue from './view/Semester/RegisterSemester.vue'
import ListSemestersVue from './view/Semester/ListSemesters.vue'
import RegisterCalendarVue from './view/Calendar/RegisterCalendar.vue'
import AssignCalendarVue from './view/Calendar/AssignCalendar.vue'
import ListCalendarsVue from './view/Calendar/ListCalendars.vue'
import RegisterTimetableVue from './view/Timetable/RegisterTimetable.vue'
import ListTimetablesVue from './view/Timetable/ListTimetables.vue'
import RegisterClassVue from './view/Class/RegisterClass.vue'
import ListClassesVue from './view/Class/ListClasses.vue'
import ListStudentsVue from './view/ListStudents.vue'

import './assets/main.css'


// 1. Define route components.
// These can be imported from other files

// 2. Define some routes
// Each route should map to a component.
// We'll talk about nested routes later.
const routes = [
    { path: '/home', component: HomeVue, name: 'Home' },
    { path: '/about', component: AboutVue },
    { path: '/attendance', component: AttendanceVue },
    { path: '/contact', component: ContactVue },
    { path: '/login', component: LoginVue, name: "Login" },
    { path: '/adminlogin', component: AdminLoginVue, name: "AdminLogin" },
    { path: '/studentregistration', component: StudentRegistrationVue },
    { path: '/cam', component: CamVue },
    { path: '/register_course', component: RegisterCourseVue },
    { path: '/list_courses', component: ListCoursesVue },
    { path: '/register_subject', component: RegisterSubjectVue },
    { path: '/list_subjects', component: ListSubjectsVue },
    { path: '/register_semester', component: RegisterSemesterVue },
    { path: '/list_semesters', component: ListSemestersVue },
    { path: '/register_calendar', component: RegisterCalendarVue },
    { path: '/assign_calendar', component: AssignCalendarVue },
    { path: '/list_calendars', component: ListCalendarsVue },
    { path: '/register_timetable', component: RegisterTimetableVue },
    { path: '/list_timetables', component: ListTimetablesVue },
    { path: '/register_class', component: RegisterClassVue },
    { path: '/list_classes', component: ListClassesVue },
    { path: '/list_students', component: ListStudentsVue },
    { path: '/', component: HomeVue },
]

// 3. Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes, // short for `routes: routes`
})


router.beforeEach(async (to, from) => {
    console.log(to, from);
    if (!localStorage.getItem('token') && (to.name !== 'Login' && to.name !== 'AdminLogin')) {
        console.log('1 login')
        return 'Login'
    } else if (localStorage.getItem('token') && (to.name === 'Login' || to.name === 'AdminLogin')) {
        console.log('2 home')
        return 'Home'
    } else if (to.path === '/logout') {
        console.log('3 logout')

        localStorage.removeItem('token')
        return 'Login'
    }
})


// 5. Create and mount the root instance.
const app = createApp(App)

// Make sure to _use_ the router instance to make the
// whole app router-aware.
app.use(router)

app.mount('#app')

// Now the app has started! 
