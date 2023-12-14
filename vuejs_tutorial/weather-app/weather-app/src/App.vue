<template>
	<div>
		<HeaderVue></HeaderVue>

		<router-view></router-view>

		<FooterVue></FooterVue>
	</div>
</template>

<script setup>
import HeaderVue from './components/Header/Header.vue';
import FooterVue from './components/Footer/Footer.vue';
import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Weather from './components/Weather.vue';

// Tạo router instance
// export const router = createRouter({
// 	history: createWebHistory(),
// 	routes: [
// 		{ path: '/', component: Home },
// 		{ path: '/login', component: Login },
// 		{ path: '/weather', component: Weather },
// 	],
// });
//
</script>

<style scoped></style>
