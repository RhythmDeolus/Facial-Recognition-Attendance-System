<template>
    <Navbar/>
    <center><H1>Student Registration</H1></center>
    <form action="">
        <p>Name : </p>
            <input type = 'text'>
        <p>Email ID : </p>
            <input type="text">
        <p>Roll Number : </p>
            <input type="text">
        
        <br>
        <br>
        <button>Submit</button><button>Cancel</button>
    </form>
    <hr>
    <a href="/AdminLogin">Admin Login</a>
    <hr>
        <a href="./Home">Back to Home</a>
</template>

<script>
import Navbar from '@/components/Navbar.vue';

export default {
  components: {
    Navbar, // Register the Navbar component
  },
  // Your component logic goes here
};
</script>

<style>
</style>