<template>
    <div class="card-about">
    <Navbar/>
    <div class="container">
    <div class="heading-image"><img class="background-image" src="../assets/AMS-logo.jpeg" alt="Facial Attendance Image"></div>
    <div class="text">
    <h1>Attendance Management System</h1>
    </div>
    </div>
    </div>
</template>

<script>
</script>

<style scoped>

.text{
  font-family: 'Courier New', Courier, monospace;
  font-size: 2.5em;
  vertical-align: middle;
  text-align: right;
  display: flex;
  align-items: center;
}
.background-image{
  width: 100%;
}

.card-about {
  border-radius: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
}
.container{
  display:flex;
  flex-direction: row;
  min-height: 80vh;
}

.heading-image{
  display: flex;
  align-items: center;
}
</style>

