<template>
	<header class="header">
		<a href="#" class="logo">Developer</a>
		<nav class="nav-items">
			<a href="/">Home</a>
			<a href="/about">About</a>
			<a href="#">Contact</a>
			<a href="#">Login</a>
			<a href="#">Register</a>

			<component :is="currentView" />
		</nav>
	</header>
</template>
<script setup>
import './Header.css';
</script>
