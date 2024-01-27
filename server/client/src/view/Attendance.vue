<template>
    <Navbar />
    <table :key="rerenderkey" border="1" align="center">
        <thead>
            <tr>
                <th>Student Name</th>
                <th>Student Id</th>
                <th v-for="date in dates" :key="date">{{ date.toLocaleDateString() }}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(n, index) in studentIdList.length" :key="index">
                <td>{{ studentdata[studentIdList[index]]?.name }}</td>
                <td>{{ studentIdList[index] }}</td>
                <td v-for="attendance in studentAttendance[studentIdList[index]]">
                    <div bgcolor="green" v-if="attendance"> Pre. </div>
                    <div bgcolor="red" v-if="!attendance"> Abs. </div>
                </td>
            </tr>
        </tbody>
    </table>
    <button @click="fetchAttendanceData()">Refresh</button>
</template>

<script setup>
Date.prototype.addDays = function(days) {
    var date = new Date(this.valueOf());
    date.setDate(date.getDate() + days);
    return date;
}

import Navbar from '@/components/Navbar.vue';
import {ref} from 'vue';

let rerenderkey = ref(1)

function rerender() {
    rerenderkey.value++;
}

let dates = []
let studentIdList = []
let studentAttendance = {}


let studentdata = {
    // 1: {name: 'rhythm'},
    // 2: {name:'vasu'},
    // 3: {name:'Amal'}
}
let attendanceData = {
    // '1': { id: 1, name: 'Rhythm', day: 1 },
    // '2': { id: 2, name: 'Vasu', day: 2 },
    // '3': { id: 3, name: 'Amal', day: 5 },
}

async function fetchAttendanceData() {
    try {
        const response = await fetch('/api_1/get_students');
        const students = await response.json();
        studentdata = students
        const response2 = await fetch('/api_1/get_attendance');
        const attendance = await response2.json();
        attendanceData = attendance;
        setTable(studentdata, attendance);
        rerender()
    } catch (error) {
        console.error(error);
    }
}

fetchAttendanceData();

function setTable(studentdata, attendanceData) {
    dates= []
    studentAttendance= {}
    studentIdList= Object.keys(studentdata)
    let maxDate = new Date(Object.values(attendanceData).reduce((a, b) => Math.max(a, Date.parse(b['time'])), -1))
    let minDate = new Date(Object.values(attendanceData).reduce((a, b) => Math.min(a, Date.parse(b['time'])), Infinity))


    for (let i = minDate; i <= maxDate; i = i.addDays(1)) {
        dates.push(i);
    }
    let failed = false;

    for (let id of studentIdList) {
        studentAttendance[id] = []
        for (let i = minDate; i <= maxDate; i = i.addDays(1)) {
            console.log(typeof i)
            let idx = -1;
            try {
                idx = Object.values(attendanceData).findIndex(a => a['id'] == id && (new Date(Date.parse(a['time'])))?.toLocaleDateString() === i?.toLocaleDateString());
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

<style></style>
