<template>
	<HeaderVue></HeaderVue>
	<About></About>
	<!-- <LoginVue></LoginVue> -->
	<!-- <div id="app">
		<task v-bind:tasks="tasks"></task>
	</div> -->
	<!-- <router-link></router-link> -->
	<FooterVue></FooterVue>
</template>
<script>
import { ref } from 'vue';
import HeaderVue from './components/Header/Header.vue';
import FooterVue from './components/Footer/Footer.vue';
import LoginVue from './components/Login.vue';
import Task from './components/Task.vue';
import About from './components/About.vue';

export default {
	name: 'App',
	components: {
		HeaderVue,
		FooterVue,
		Task,
		About,
	},
	setup() {
		const tasks = ref([
			{
				id: 1,
				title: 'Learn Vue JS',
				completed: true,
			},
			{
				id: 2,
				title: 'Watch Netflix',
				completed: true,
			},
			{
				id: 3,
				title: 'Go shopping',
				completed: false,
			},
			{
				id: 4,
				title: 'Learn guitar',
				completed: false,
			},
			{
				id: 5,
				title: 'Send email',
				completed: false,
			},
		]);

		return { tasks };
	},
};
</script>
