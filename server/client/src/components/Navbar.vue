<template>
  <nav class="navbar">
    <router-link to="/home">Home</router-link>
    <router-link to="/attendance">Attendance</router-link>
    <div class="dropdown">
      <button class="dropbtn">Register</button>
      <div class="dropdown-content">
        <router-link class="dropdown-list" to="/studentregistration">Register Student</router-link>
        <router-link class="dropdown-list" to="/cam">Register Face</router-link>
      </div>
    </div>
    <div class="dropdown">
      <button class="dropbtn">Contact Us</button>
      <div class="dropdown-content">
        <router-link to="/about">About</router-link>
        <router-link to="/contact">Contributors</router-link>
      </div>
    </div>
    <router-link to="/login">Login</router-link>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #292929;
  padding: 15px;
  display: flex;
  justify-content: space-around;
  border-radius: 0.5em;
}

.navbar a {
  color: white;
  text-align: center;
  padding: 14px 20px;
  text-decoration: none;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
  border-radius: 5rem;
}

.navbar a.active {
  background-color: #4caf50;
  color: white;
  border-radius: 25px;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropbtn {
  background-color: #292929;
  color:white;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  padding: 15px;
  text-decoration: None;
}

.dropbtn:hover{
  background-color: #ddd;
  color: black;
  border-radius: 5rem;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {
  background-color: #ddd;
}

.dropdown:hover .dropdown-content {
  display: block;
}

.visible {
  display: block;
}

.dropdown-list{
  border-radius: 0px;
}

router-link,button{
  font-family: Arial, Helvetica, sans-serif;
  font-size: 16px;
}
</style>
