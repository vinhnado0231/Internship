<template>
	<div class="container p-0">
		<div class="d-flex">
			<div class="card main-div w-100">
				<div class="p-3">
					<h2 class="mb-1 day">{{ formatDay(latestTimeline?.time) }}</h2>
					<p class="text-light date mb-0">
						{{ formatDate(latestTimeline?.time) }}
					</p>
					<small>{{ formatTime(latestTimeline?.time) }}</small>
					<h2 class="place">
						<i
							class="fa fa-location"
							style="margin-bottom: 20px; margin-top: 50px">
							Rio
						</i>
						<small>City</small>
					</h2>
					<div class="temp">
						<h1 class="weather-temp" style="margin-left: 300px">
							{{ weatherData?.temperature }}&deg;
						</h1>

						<h2 class="text-light" style="margin-left: 300px">
							{{ weatherData?.description }}
						</h2>
					</div>
				</div>
			</div>
		</div>
	</div>
	<div class="card card-2 w-100">
		<table class="m-4">
			<tbody>
				<tr>
					<th>Temperature</th>
					<td>{{ weatherData?.temperature }}&deg;C</td>
				</tr>
				<tr>
					<th>Humidity</th>
					<td>{{ weatherData?.humidity }}%</td>
				</tr>
				<tr>
					<th>Wind Speed</th>
					<td>{{ weatherData?.windSpeed }} m/s</td>
				</tr>
			</tbody>
		</table>
		<DayWeather :weatherData="weatherData" />
		<div id="div_Form" class="d-flex m-3 justify-content-center">
			<form action="">
				<input type="button" value="Change Location" class="btn btn-primary" />
			</form>
		</div>
	</div>
</template>

<script setup>
import DayWeather from './DayWeather.vue';
import { ref, onMounted } from 'vue';
import axios from 'axios';

const weatherData = ref(null);
let latestTimeline = null;

onMounted(async () => {
	try {
		const response = await axios.get(
			'https://api.tomorrow.io/v4/weather/forecast?location=20,-35&apikey=y9E4AoEatwTvLS9h93VCGqabPDaTVHJL'
		);
		latestTimeline = response.data.timelines.minutely[0];
		if (latestTimeline) {
			weatherData.value = {
				temperature: latestTimeline.values.temperature,
				humidity: latestTimeline.values.humidity,
				windSpeed: latestTimeline.values.windSpeed,
				description: 'Data from api.tommorrow.io', // Bạn cần thay thế thông tin này bằng thông tin thích hợp
			};
		}
	} catch (error) {
		console.error('Error fetching weather data:', error);
	}
});

const formatDay = (time) => {
	if (!time) return '';
	const date = new Date(time);
	const days = [
		'Sunday',
		'Monday',
		'Tuesday',
		'Wednesday',
		'Thursday',
		'Friday',
		'Saturday',
	];
	return days[date.getDay()];
};

const formatDate = (time) => {
	if (!time) return '';
	const date = new Date(time);
	const options = { year: 'numeric', month: 'long', day: 'numeric' };
	return date.toLocaleDateString('en-US', options);
};

const formatTime = (time) => {
	if (!time) return '';
	const date = new Date(time);
	const options = { hour: 'numeric', minute: 'numeric', hour12: true };
	return date.toLocaleTimeString('en-US', options);
};
</script>

<style scoped>
body {
	background-color: #343d4b;
}
.weather-temp {
	margin: 0;
	font-weight: 700;
	font-size: 4em;
}

h2.mb-1.day {
	font-size: 3rem;
	font-weight: 400;
}
.main-div {
	border-radius: 20px;
	color: #fff;
	background-image: url('https://t4.ftcdn.net/jpg/05/49/86/39/360_F_549863991_6yPKI08MG7JiZX83tMHlhDtd6XLFAMce.jpg');
	background-size: cover;
	background-position: center;
	background-blend-mode: overlay;
	background-color: rgba(0, 0, 0, 0.5);
	background-repeat: no-repeat;
}

.temp {
	position: absolute;
	bottom: 0;
}
.main-div:hover {
	transform: scale(1.1);
	transition: transform 0.5s ease;
	z-index: 1;
}

.card-2 {
	background-color: #212730;
}
.card-details {
	margin-left: 19px;
}
.h1_Left {
	position: absolute;
	bottom: 25px;
	left: 16px;
	font-size: 3vw;
	line-height: 1.2;
}
.h3_Left {
	font-size: 1rem;
}

table {
	position: absolute;
	left: 15px;
	border-collapse: separate;
	width: 85%;
	text-align: left;
	max-width: 600px;
	margin: 0 auto;
}

th,
td {
	font-size: 18px;
	color: #fff;
}
td {
	text-align: right;
}
table,
tr:hover {
	color: red;
}
.change_btn {
	background-image: linear-gradient(to right, cyan, magenta);
}

.change_btn:hovere {
	transform: scale(0.9);
	transition: transform 0.1s ease;
}
</style>
