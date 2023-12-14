import { createRouter, createWebHistory } from 'vue-router';
import Home from './components/Home.vue';
import Login from './components/Login.vue';
import Weather from './components/Weather.vue';

const routes = [
	{ path: '/', component: Home },
	{ path: '/login', component: Login },
	{ path: '/weather', component: Weather },
];

export const router = createRouter({
	history: createWebHistory(),
	routes,
});

// export default router;
