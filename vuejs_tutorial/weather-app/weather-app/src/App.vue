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
</script>

<style scoped></style>
