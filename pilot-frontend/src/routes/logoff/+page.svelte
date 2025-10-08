<script>
  import { onMount } from 'svelte';

  const API_BASE_URL = 'http://localhost:8000';
  let errorMessage = '';

  onMount(async () => {
    try {
      // Get the JWT tokens
      const accessToken = localStorage.getItem('accessToken');
      const refreshToken = localStorage.getItem('refreshToken');

      // Call backend logout endpoint to blacklist the refresh token
      if (accessToken && refreshToken) {
        await fetch(`${API_BASE_URL}/api/auth/logout/`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${accessToken}`
          },
          credentials: 'include',
          body: JSON.stringify({
            refresh: refreshToken
          })
        });
      }
    } catch (error) {
      console.error('Logout error:', error);
      errorMessage = 'Warning: Could not complete server logout';
    } finally {
      // Always clear local storage regardless of backend response
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      localStorage.removeItem('user');

      // Redirect to home page after a brief moment
      setTimeout(() => {
        window.location.href = '/';
      }, 500);
    }
  });
</script>

<svelte:head>
  <title>Logging out...</title>
</svelte:head>

<div class="logoff-container">
  <div class="logoff-message">
    <h1>Logging out...</h1>
    <p>You are being logged out. Please wait.</p>
  </div>
</div>

<style>
  .logoff-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }

  .logoff-message {
    text-align: center;
  }

  h1 {
    color: #333;
    font-size: 28px;
    margin-bottom: 10px;
  }

  p {
    color: #666;
    font-size: 16px;
  }
</style>
