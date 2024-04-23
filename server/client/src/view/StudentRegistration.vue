<template>
    <div class="background-image-container">
        <div class="card-about">
        <div class="card-container">
    <div class="card">
      <center><h1>Student Registration</h1></center>
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
          <button class="admin" >Admin Login</button>
        </router-link>
        <router-link to="/home">
          <button class="home" >Back to Home</button>
        </router-link>
        </div>
    </div>
  </div>
    </div>
</div>
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
}

.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;

  /* Black with 50% opacity */
}

.card {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3); /* Soft shadow effect */
  max-width: 400px;
  width: 100%;
  display: flex;
  flex-direction: column;
  
}

.button-container {
  display: flex;
  gap:5px;
  justify-content: center;
}

.submit,
.cancel {
  border: 2px solid transparent;
  border-radius: 20px;
  background-color: transparent;
  padding: 10px 20px;
  cursor: pointer;
  border-color: green;
  
  
  transition: border-color 0.3s, background-color 0.3s;
}

.cancel{
  border: 2px solid red;
}

.submit:hover {
  border-color: green;
  color:white;
  background-color: green;
}

.cancel:hover {
  border-color: red;
  color:white;
  background-color: red;
}

.submit:hover,
.cancel:hover {
  color: #fff;
}
h1{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 2.5em;
    color: black;
}
p{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 1.5em;
    color: black;
}

.input-box{
  border:2px solid gray;
  padding:10px 5px 10px 5px;
  border-radius: 50px;
  font-size: 20px;
}

.input-container{
  display: flex;
  flex-direction: column;
  margin-bottom: 25px;
}

.admin,
.home {
  border: 2px solid blue;
  border-radius: 20px;
  background-color: transparent;
  padding: 10px 20px;
  cursor: pointer;
  transition: border-color 0.3s, background-color 0.3s, color 0.3s;/* Added color transition */

}

.home{
  border: 2px solid green;
}

.admin:hover,
.home:hover {
  color: #fff; /* Change text color on hover */
}

.admin:hover {
  border-color: blue; /* Change border color on hover */
  background-color: blue; /* Change background color on hover */
}

.home:hover {
  border-color: green; /* Change border color on hover */
  background-color: green; /* Change background color on hover */
}

.extra-btn{
  display: flex;
  flex-direction: column;
  gap:5px;
  padding : 15px 5px 5px 5px;
}
</style>
