<template>
    <Layout v-if="isIncluded">
        <router-view /> 
    </Layout>
    <router-view v-else />
</template>

<script setup>
import Layout from "@/components/Layout.vue";
import { useRoute } from "vue-router";
import { onUpdated, computed } from "vue";
const excludedRoutes =  new Set(['AdminLogin', 'Login']);
const isIncluded = computed(() => !excludedRoutes.has(route.name));
const route = useRoute();
onUpdated(() => console.log(excludedRoutes.has(route.path), excludedRoutes, route.path));


</script>


