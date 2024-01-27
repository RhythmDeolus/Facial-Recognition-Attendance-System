<template>
    <Navbar/>
    <center><H1>Student Registration</H1></center>
    <div >
        <p>Name : </p>
            <input type = 'text' v-model="name" name="name" required>
        <p>Roll Number : </p>
            <input type="text" v-model="id" name="id" required>
        
        <br>
        <br>
        <button type="button" @click="checkForm">Submit</button><button>Cancel</button>
    </div>
    <hr>
    <router-link to="/adminlogin">Admin Login</router-link>
    <hr>
        <router-link to="/home">Back to Home</router-link>
</template>

<script setup>
import Navbar from '@/components/Navbar.vue';

let name = null;
let id = null;

function checkForm(e) {
    if (name && Number(id)) {
        fetch('/api_1/register_student', {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json'
            },
            body: JSON.stringify({
                name: name,
                id: Number(id)
            })
        }).then(async (response) => {
           let val = await response.json() 
           alert(val)
        })
    }
    
}
</script>

<style>
</style>