<template>
    <nav class="navbar">
      <router-link to="/Home">Home</router-link>
      <router-link to="/attendance">Attendance</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/Contact">Contact Us</router-link>
    </nav>
  </template>
  
  <style scoped>
  .navbar {
    background-color: #c4f5b5;
    padding: 15px;
    display: flex;
    justify-content: space-around;
  }
  
  .router-link {
    text-decoration: none;
    color: black;
    padding: 10px;
    border-radius: 5px;
    &:hover {
      background-color: #555;
    }
  }
  </style>
  