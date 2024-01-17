<template>
  <Navbar/>
    <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Name</th>
        <th>Day 01</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.name }}</td>
        <td>{{ user.day01 }}</td>
      </tr>
    </tbody>
  </table>
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