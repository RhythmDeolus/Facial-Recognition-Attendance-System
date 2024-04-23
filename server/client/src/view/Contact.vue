<template>
  <div class="background-image-container">
    <div class="card-about">
      <div class="card-container">
        <a href="https://github.com/rhythmdeolus" class="card-link">
        <div class="card-student">
          <img src="../assets/student.png" alt="Student Image" class="student-icon">
          <div class="card-content">
            <h3>Rhythm Deolus</h3>
            <p>52222107</p>
            <p>MCA Student</p>
          </div>
        </div>
      </a>
      <a href="https://github.com/ritiks5" class="card-link">
        <div class="card-student">
          <img src="../assets/student.png" alt="Student Image" class="student-icon">
          <div class="card-content">
            <h3>Ritik Sharma</h3>
            <p>52211208</p>
            <p>MCA Student</p>
          </div>
        </div>
      </a>
      <a href="https://github.com/" class="card-link">
        <div class="card-student">
          <img src="../assets/student.png" alt="Student Image" class="student-icon">
          <div class="card-content">
            <h3>Adarsh Singh</h3>
            <p>52212102</p>
            <p>MCA Student</p>
          </div>
        </div>
      </a>
      </div>
    </div>
  </div>
</template>

<script>
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
  flex-wrap: wrap;
  justify-content: space-around;
  margin: 2rem auto;
  padding-top: 100px;
}

.card-student {
  width: 350px;
  background-color: rgba(255, 255, 255, 0.9);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.5);
  border-radius: 5px;
  margin: 1rem;
  text-align: center;
  backdrop-filter: blur(9px);
  min-width: px;
}

.student-icon {
  margin:20px;
  width: 150px; /* Adjust the width as needed */
  height: 150px; /* Adjust the height as needed */
  border-radius: 50%; /* Makes the image round */
  padding: 1.5rem;
  border:3px solid black;
}

.card-content {
  padding: 1rem;
}

h3 {
  margin-bottom: 0.5rem;
}

.card-link {
  text-decoration: none; /* Remove underline */
  color: inherit; /* Inherit color from parent */
  cursor: pointer; /* Show pointer cursor on hover */
}

.card-link:hover .card-student {
  /* Add hover effect */
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transform: translateY(-2px);
}

</style>
