<template>    
<button data-drawer-target="sidebar-multi-level-sidebar" data-drawer-toggle="sidebar-multi-level-sidebar" aria-controls="sidebar-multi-level-sidebar" type="button" class="inline-flex items-center p-2 mt-2 ms-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
   <span class="sr-only">Open sidebar</span>
   <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
   <path clip-rule="evenodd" fill-rule="evenodd" d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z"></path>
   </svg>
</button>

<aside id="sidebar-multi-level-sidebar" class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0" aria-label="Sidebar">
   <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
      <ul class="space-y-2 font-medium">
        <template v-for="item in linkStruct">
            <li v-if="item[1] instanceof Array">
                        <button type="button" class="flex items-center w-full p-2 text-base text-gray-900 transition duration-75 rounded-lg group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700" :onclick="handle_toggle" :aria-controls="item[0]" :data-collapse-toggle="item[0]">
                  <svg class="flex-shrink-0 w-5 h-5 text-gray-500 transition duration-75 group-hover:text-gray-900 dark:text-gray-400 dark:group-hover:text-white" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 18 21">
                     <path d="M15 12a1 1 0 0 0 .962-.726l2-7A1 1 0 0 0 17 3H3.77L3.175.745A1 1 0 0 0 2.208 0H1a1 1 0 0 0 0 2h.438l.6 2.255v.019l2 7 .746 2.986A3 3 0 1 0 9 17a2.966 2.966 0 0 0-.184-1h2.368c-.118.32-.18.659-.184 1a3 3 0 1 0 3-3H6.78l-.5-2H15Z"/>
                  </svg>
                            <span class="flex-1 ms-3 text-left rtl:text-right whitespace-nowrap">{{item[0]}}</span>
                  <svg class="w-3 h-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 10 6">
                     <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 4 4 4-4"/>
                  </svg>
            </button>
            <ul :id="item[0]" class="hidden py-2 space-y-2">
                  <li v-for="link in item[1]">
                                <router-link :to="link[1]" class="flex items-center w-full p-2 text-gray-900 transition duration-75 rounded-lg pl-11 group hover:bg-gray-100 dark:text-white dark:hover:bg-gray-700">{{link[0]}}</router-link>
                  </li>
            </ul>
            </li>
            <li v-else>
                <router-link class="flex items-center p-2 text-gray-900 rounded-lg dark:text-white hover:bg-gray-100 dark:hover:bg-gray-700 group"  :to="item[1]">
                            <span class="ms-3">{{item[0]}}</span></router-link> 
            </li>
        </template>
      </ul>
   </div>
</aside>

<div class="p-4 sm:ml-64">
        <slot></slot>
</div>
</template>

<script setup>
import { useCheckAuth } from '@/composables/auth';

function handle_toggle(e){
    let target = e.target;
    if (target.tagName !== 'BUTTON')  target = target.closest('button');
    const collapse = target.getAttribute('data-collapse-toggle');
    console.log(target, collapse);
    const element = document.getElementById(collapse);
    element.classList.toggle('hidden');
}

const linkStruct = [
    [ 'Home' , '/' ],
    [ 'Attendance' , '/attendance' ],
    [ 'Register' , [
       ['Register Student' , '/studentregistration'],
       [ 'Register Face' , '/cam' ],
    ]],
    [ 'Contact Us' , [
       [ 'About' , '/about',],
       [ 'Contributors' , '/contact' ],
    ]],
    useCheckAuth()? [ 'Logout' , '/logout' ] : [ 'Login' , '/login' ]
];

</script>

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
