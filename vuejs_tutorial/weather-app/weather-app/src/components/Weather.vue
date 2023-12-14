<template>
	<div class="app">
		<div
			class="header container-fluid p-5 bg-light d-flex flex-column align-items-center">
			<h1 class="mb-5">Weather App</h1>
			<div class="d-flex justify-content-center">
				<div class="searchbar flex-grow-1 mx-2">
					<input
						type="text"
						class="input form-control"
						v-model="city"
						placeholder="Enter a city" />
				</div>
				<button class="btn btn-primary">
					Search <i class="fas fa-search"></i>
				</button>
			</div>
		</div>
	</div>
	<WeatherDisplay></WeatherDisplay>
</template>

<script setup>
import { ref } from 'vue';
import WeatherDisplay from './WeatherDisplay.vue';
const city = ref('');
const showWeather = ref(false);

const searchWeather = async () => {
	showWeather.value = false;
	await this.$nextTick();
	showWeather.value = true;
};
</script>

<style scoped>
body {
	background-color: #121212 !important;
}

.app {
	display: flex;
	flex-direction: column;
}

.header {
	border-bottom: 1px solid #dee2e6;
}

.searchbar {
	flex: 1;
	width: 500px;
}

.input {
	width: 100%;
}
</style>
