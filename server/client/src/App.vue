<template>
    <Layout>
        <router-view /> 
    </Layout>
</template>

<script>
import Layout from "@/components/Layout.vue";

export default {
  name: 'App',
  components: {
    Layout,
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>

