<template>
  <div class="card-layout">
    <div class="background-image-container">
      <div class="card-about">
        <div class="nav">
        <Navbar />
      </div>
        <div class="card-container">
          <div class="card">
            <center><h1>Enroll Face Data</h1></center>
            <div class="input-container">
              <p>Student ID</p>
              <input type='text' v-model="id" required class="input-box">
            </div>
            <div class="video-container">
              <video ref="video" autoplay></video>
              <button @click="captureImage" class="capture-btn">Capture Image</button>
              <canvas ref="canvas" style="display: none;"></canvas>
              <img v-if="capturedImage" :src="capturedImage" alt="Captured Image" class="captured-image" />
            </div>
            <div class="button-container">
              <button @click="checkForm" class="submit">Submit</button>
              <button class="cancel">Cancel</button>
            </div>
          </div>
        </div>
      </div>
      <div class="extra-btn">
        <router-link to='/AdminLogin'>
          <button class="admin">Admin Login</button>
        </router-link>
        <router-link to="/home">
          <button class="home">Back to Home</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
export default {
  components: {
    Navbar,
  },
  data() {
    return {
      capturedImage: null,
      id: null
    };
  },
  mounted() {
    this.setupCamera();
  },
  methods: {
    checkForm(e) {
      if (Number(this.id) && this.capturedImage) {
        fetch('/api_1/register_student_face', {
          method: 'POST',
          headers: {
            "Content-Type": 'application/json'
          },
          body: JSON.stringify({
            id: Number(this.id),
            image: this.capturedImage.replace(/^data:\w+\/\w+;base64,/, '')
          })
        }).then(async (response) => {
          let val = await response.json()
          alert(val)
        })
      }
    },
    async setupCamera() {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        this.$refs.video.srcObject = stream;
      } catch (error) {
        console.error('Error accessing camera:', error);
      }
    },
    captureImage() {
      const video = this.$refs.video;
      const canvas = this.$refs.canvas;
      const context = canvas.getContext('2d');

      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;

      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      const dataUrl = canvas.toDataURL('image/png');

      this.capturedImage = dataUrl;
    },
  },
};
</script>

<style scoped>
.card-layout {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.background-image-container {
  background-image: url('../assets/AMS-logo.jpeg');
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  width: 100%;
  height: 100%;
  padding: 20px;
}

.card-about {
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.5);
  background-color: rgba(255, 255, 255, 0.9);
  padding: 20px;
  backdrop-filter: blur(5px);
}

.card-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
}

.card {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
  max-width: 400px;
  height:500px;
  overflow-y: scroll;
  width: 100%;
  display: flex;
  flex-direction: column;
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
  margin-bottom: 10px;
}

.video-container {
  margin-top: 20px;
  position: relative;
}

.video-container video {
  width: 100%;
  border-radius: 10px;
}

.capture-btn {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  padding: 10px 20px;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  border: none;
  cursor: pointer;
}

.captured-image {
  margin-top: 10px;
  border-radius: 10px;
  width: 100%;
}

.button-container {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.submit,
.cancel {
  flex: 1;
  padding: 10px 0;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
  border-radius: 5px;
}

.submit {
  background-color: #28a745;
  color: white;
  margin-right: 10px;
}

.cancel {
  background-color: #dc3545;
  color: white;
}

.submit:hover,
.cancel:hover {
  background-color: transparent;
  color: black;
}

.extra-btn {
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}

.admin,
.home {
  padding: 10px 20px;
  border-radius: 15px;
  cursor: pointer;
  transition: background-color 0.3s, color 0.3s;
}

.admin {
  background-color: #007bff;
  color: white;
}

.home {
  background-color: #28a745;
  color: white;
}

.admin:hover,
.home:hover {
  background-color: transparent;
  color: black;
}


</style>
