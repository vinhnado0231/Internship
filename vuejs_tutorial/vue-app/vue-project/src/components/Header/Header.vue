<template>
	<header class="header">
		<a href="#" class="logo">Developer</a>
		<nav class="nav-items">
			<a href="/">Home</a>
			<a href="/about">About</a>
			<a href="#">Contact</a>
			<component :is="currentView" />
		</nav>
	</header>
</template>
<script setup>
import './Header.css';
import { ref, computed } from 'vue';
import Home from '../Home.vue';
import About from '../About.vue';

const routes = {
	'/': Home,
	'/about': About,
};

const currentPath = ref(window.location.hash);

window.addEventListener('hashchange', () => {
	currentPath.value = window.location.hash;
});

const currentView = computed(() => {
	return routes[currentPath.value.slice(1) || '/'] || NotFound;
});
</script>
