import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import HeaderVue from './components/Header/Header.vue';
import FooterVue from './components/Footer/Footer.vue';
import HomeVue from './components/Home.vue';
import Task from './components/Task.vue';

// const routes = [
// 	{ path: '/', component: HomeVue },
// 	// { path: '/login', component: LoginVue },
// 	{ path: '/about', component: AboutVue },
// 	{ path: '/tasks', component: Task },
// 	// { path: '/:pathMatch(.*)*', name: 'NotFound', component: NotFoundVue },
// ];

// const router = createRouter({
// 	// Provide the history implementation to use. We are using the hash history for simplicity here.
// 	history: createWebHashHistory(),
// 	routes, // short for `routes: routes`
// });

const app = createApp(App);

//Global Registration

app.mount('#app');
