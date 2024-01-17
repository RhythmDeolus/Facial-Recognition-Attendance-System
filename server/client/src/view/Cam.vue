<template>
  <Navbar/>
  <h1>Enroll Facial Data</h1>
  <form action="">
      <p>Student ID</p>
          <input type = 'text'>
      
  <div>
    <video ref="video" autoplay></video>
    <button @click="captureImage">Capture Image</button>
    <canvas ref="canvas" style="display: none;"></canvas>
    <img v-if="capturedImage" :src="capturedImage" alt="Captured Image" />
  </div>
  <br>
  <br>
      <button>Submit</button><button>Cancel</button>
  </form>
</template>

<script>
import Navbar from '@/components/Navbar.vue';
export default {
  components: {
    Navbar, // Register the Navbar component
  },
  data() {
    return {
      capturedImage: null,
    };
  },
  mounted() {
    this.setupCamera();
  },
  methods: {
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

      // Set the canvas dimensions to match the video feed
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;

      // Draw the current frame from the video feed onto the canvas
      context.drawImage(video, 0, 0, canvas.width, canvas.height);

      // Convert the canvas content to a data URL (base64-encoded image)
      const dataUrl = canvas.toDataURL('image/png');

      // Set the captured image in the data property
      this.capturedImage = dataUrl;
    },
  },
};
</script>

<style scoped>
/* Add your component-specific styles here */
</style>
