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
        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">Roll no</label>
    </div>
    <button type="submit"
      @click="checkForm"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Submit</button>
  </div>

  <!-- <div class="background-image-container">
    <div class="card-about">
      <div class="card-container">
        <div class="card">
          <center>
            <h1>Student Registration</h1>
          </center>
          <form action="">
            <div class="input-container">
              <p>Name :</p>
              <input class="input-box" v-model="name" name="name" type='text' required>
              <p>Roll Number :</p>
              <input class="input-box" v-model="id" name="id" type="text" required>
            </div>
            <div class="button-container">
              <button class="submit" @click="checkForm">Submit</button>
              <button class="cancel">Cancel</button>
            </div>
          </form>
          <div class="extra-btn">
            <router-link to='/adminlogin'>
              <button class="admin">Admin Login</button>
            </router-link>
            <router-link to="/home">
              <button class="home">Back to Home</button>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div> -->
</template>

<script setup>
import { useAccessToken } from '@/composables/auth';

let name = null;
let id = null;

function checkForm(e) {
    if (name && Number(id)) {
        fetch('/api_1/register_student', {
            method: 'POST',
            headers: {
                "Content-Type": 'application/json',
                'Authorization': `Bearer ${useAccessToken()}`
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