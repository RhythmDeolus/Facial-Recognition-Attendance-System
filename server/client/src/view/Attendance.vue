<template>
    <div class="background-image-container">
  <div class="card-about">
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
    </div>
    </div>
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

<style scoped>
.background-image-container {
  /* Set the background image */
  background-image: url('../assets/AMS-logo.jpeg');

  /* Set background size, position, and other properties as needed */
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;

  /* Set other styles for the container if needed */
  width: 100%;
  height: 700px;
   /* Or any desired height */
   
}
.card-about {
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  background-color: rgba(255, 255, 255, 0.9);
  padding: 20px;
  margin: 20px;
  backdrop-filter: blur(5px);
  min-height: 90vh;
}
    table {
        border-collapse: collapse;
        width: 80%;
        margin: 20px auto;
        border-radius: 20px;
        font-size: 1.5em;
        color: white;
        align-content: center;
        
    }

    th, td {
        padding: 10px;
        text-align: center;
        
    }
    tr{
        border-radius:10px;
    }

    th {
        background-color: #2B2C2B;
    }

    tr:nth-child(even) {
        background-color: #f2f2f2;
    }

    tr:hover {
        background-color: #ddd;
    }

    div[bgcolor="green"] {
        background-color: green;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    }

    div[bgcolor="red"] {
        background-color: red;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
    }

    button {
        margin: 20px auto;
        display: block;
        padding: 10px 20px;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>

