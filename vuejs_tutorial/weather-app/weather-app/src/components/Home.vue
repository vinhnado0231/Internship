<template>
	<div class="home">
		<h1>Welcome to Our Website</h1>
		<p>Explore amazing features and content.</p>

		<!-- Login Button -->
		<button @click="goToLogin">Login</button>
	</div>
</template>

<script>
export default {
	methods: {
		// Phương thức chuyển hướng đến trang đăng nhập
		goToLogin() {
			this.$router.push('/login'); // Điều này giả định rằng bạn đã cài đặt Vue Router và có một route có tên là 'login'
		},
	},
};
</script>

<style scoped>
/* Thêm các kiểu CSS theo ý muốn của bạn */
.home {
	text-align: center;
	margin-top: 50px;
}

button {
	padding: 10px 20px;
	font-size: 16px;
	cursor: pointer;
}
</style>
