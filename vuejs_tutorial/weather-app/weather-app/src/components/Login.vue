<template>
	<div class="login">
		<h2>Login</h2>

		<!-- Form for login -->
		<form @submit.prevent="login">
			<label for="username">Username:</label>
			<input type="text" id="username" v-model="username" required />

			<label for="password">Password:</label>
			<input type="password" id="password" v-model="password" required />

			<button type="submit">Login</button>
		</form>

		<!-- Display a message based on login status -->
		<p v-if="loggedIn">You are logged in!</p>
		<p v-else-if="loginFailed">Login failed. Please check your credentials.</p>
	</div>
</template>

<script>
export default {
	data() {
		return {
			username: '',
			password: '',
			loggedIn: false,
			loginFailed: false,
		};
	},
	methods: {
		login() {
			// Example: Check username and password (replace with your authentication logic)
			if (this.username === 'example' && this.password === 'password') {
				this.loggedIn = true;
				this.loginFailed = false;
			} else {
				this.loggedIn = false;
				this.loginFailed = true;
			}
		},
	},
};
</script>

<style scoped>
/* Thêm các kiểu CSS theo ý muốn của bạn */
.login {
	text-align: center;
	margin-top: 50px;
}

form {
	display: flex;
	flex-direction: column;
	max-width: 300px;
	margin: 0 auto;
}

label {
	margin-top: 10px;
}

input {
	margin-bottom: 15px;
	padding: 8px;
	font-size: 14px;
}

button {
	padding: 10px 20px;
	font-size: 16px;
	cursor: pointer;
}

p {
	margin-top: 15px;
	color: red; /* Màu sắc có thể thay đổi */
}
</style>
