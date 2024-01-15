<template>
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

<script setup>
      let studentdata = {
        1 : 'rhythm' , 
        2 : 'vasu' , 
        3 : 'Amal'

      }
      let attendancedata = {
        0 : {'rhythm' : 'day01'} 
      }
      let users = [
        { id: 1, name: 'Rhythm', day01: '' },
        { id: 2, name: 'Vasu', day01: '' },
        { id: 3, name: 'Amal', day01: '' }
      ]
     

    
</script>

<style>
</style>