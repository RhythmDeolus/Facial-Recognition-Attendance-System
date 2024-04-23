<template>
  <div class="max-w-md mx-auto">
    <div class="relative z-0 w-full mb-5 group">
      <input type="text" name="floating_rollno" id="floating_rollno" v-model="id"
        class="block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer"
        placeholder=" " required />
      <label for="floating_rollno"
        class="peer-focus:font-medium absolute text-sm text-gray-500 dark:text-gray-400 duration-300 transform -translate-y-6 scale-75 top-3 -z-10 origin-[0] peer-focus:start-0 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto peer-focus:text-blue-600 peer-focus:dark:text-blue-500 peer-placeholder-shown:scale-100 peer-placeholder-shown:translate-y-0 peer-focus:scale-75 peer-focus:-translate-y-6">
        Roll no
      </label>
    </div>
    <div class="video-container">
      <video ref="video" autoplay></video>
      <button type="submit" @click="captureImage"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Capture</button>
      <canvas ref="canvas" style="display: none;"></canvas>
      <img v-if="capturedImage" :src="capturedImage" alt="Captured Image" class="captured-image" />
    </div>
    <button type="submit" @click="checkForm"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Sumbit</button>
    <button type="submit"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Cancel</button>
  </div>

  <!-- <div class="card-layout">
    <div class="background-image-container">
      <div class="card-about">
        <div class="nav">
        </div>
        <div class="card-container">
          <div class="card">
            <center>
              <h1>Enroll Face Data</h1>
            </center>
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
    </div>
  </div> -->
</template>

<script>
import { useAccessToken } from '@/composables/auth';
export default {
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
            "Content-Type": 'application/json',
            "Authorization": `Bearer ${useAccessToken()}`
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
