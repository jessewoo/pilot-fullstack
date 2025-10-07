<script>
  let username = '';
  let email = '';
  let password = '';
  let confirmPassword = '';
  let firstName = '';
  let lastName = '';
  let error = '';
  let loading = false;

  const API_BASE_URL = 'http://localhost:8000';

  async function handleRegister(event) {
    event.preventDefault();
    loading = true;
    error = '';

    // Client-side validation
    if (password !== confirmPassword) {
      error = 'Passwords do not match';
      loading = false;
      return;
    }

    if (password.length < 8) {
      error = 'Password must be at least 8 characters long';
      loading = false;
      return;
    }

    try {
      const response = await fetch(`${API_BASE_URL}/api/auth/register/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify({
          username: username,
          email: email,
          password: password,
          first_name: firstName,
          last_name: lastName
        })
      });

      const data = await response.json();

      if (response.ok && data.success) {
        // Store token in localStorage
        localStorage.setItem('authToken', data.token);
        localStorage.setItem('user', JSON.stringify(data.user));

        // Redirect to home page
        window.location.href = '/';
      } else {
        error = data.message || 'Registration failed. Please try again.';
      }
    } catch (err) {
      console.error('Registration error:', err);
      error = 'Network error. Please try again.';
    } finally {
      loading = false;
    }
  }
</script>

<div class="register-container">
  <div class="register-card">
    <h1>Create Account</h1>

    <form on:submit={handleRegister}>
      {#if error}
        <div class="error-message">
          {error}
        </div>
      {/if}

      <div class="form-row">
        <div class="form-group">
          <label for="firstName">First Name</label>
          <input
            type="text"
            id="firstName"
            bind:value={firstName}
            placeholder="First name"
            disabled={loading}
          />
        </div>

        <div class="form-group">
          <label for="lastName">Last Name</label>
          <input
            type="text"
            id="lastName"
            bind:value={lastName}
            placeholder="Last name"
            disabled={loading}
          />
        </div>
      </div>

      <div class="form-group">
        <label for="username">Username *</label>
        <input
          type="text"
          id="username"
          bind:value={username}
          placeholder="Choose a username"
          required
          disabled={loading}
        />
      </div>

      <div class="form-group">
        <label for="email">Email *</label>
        <input
          type="email"
          id="email"
          bind:value={email}
          placeholder="Enter your email"
          required
          disabled={loading}
        />
      </div>

      <div class="form-group">
        <label for="password">Password *</label>
        <input
          type="password"
          id="password"
          bind:value={password}
          placeholder="Create a password (min 8 characters)"
          required
          disabled={loading}
        />
      </div>

      <div class="form-group">
        <label for="confirmPassword">Confirm Password *</label>
        <input
          type="password"
          id="confirmPassword"
          bind:value={confirmPassword}
          placeholder="Confirm your password"
          required
          disabled={loading}
        />
      </div>

      <button type="submit" class="register-button" disabled={loading}>
        {loading ? 'Creating account...' : 'Create Account'}
      </button>
    </form>

    <div class="footer-links">
      Already have an account? <a href="/login">Login here</a>
    </div>
  </div>
</div>

<style>
  .register-container {
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 20px;
  }

  .register-card {
    background: white;
    border-radius: 8px;
    padding: 40px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    width: 100%;
    max-width: 500px;
  }

  h1 {
    margin: 0 0 30px 0;
    color: #333;
    text-align: center;
    font-size: 28px;
  }

  .form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
  }

  .form-group {
    margin-bottom: 20px;
  }

  label {
    display: block;
    margin-bottom: 8px;
    color: #555;
    font-weight: 500;
    font-size: 14px;
  }

  input {
    width: 100%;
    padding: 12px 15px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 14px;
    transition: border-color 0.3s;
    box-sizing: border-box;
  }

  input:focus {
    outline: none;
    border-color: #667eea;
  }

  input:disabled {
    background-color: #f5f5f5;
    cursor: not-allowed;
  }

  .register-button {
    width: 100%;
    padding: 12px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    font-weight: 600;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    margin-top: 10px;
  }

  .register-button:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
  }

  .register-button:disabled {
    opacity: 0.6;
    cursor: not-allowed;
    transform: none;
  }

  .error-message {
    background-color: #fee;
    color: #c33;
    padding: 12px 15px;
    margin-bottom: 20px;
    border-radius: 4px;
    border-left: 4px solid #c33;
    font-size: 14px;
  }

  .footer-links {
    margin-top: 20px;
    text-align: center;
    font-size: 14px;
    color: #666;
  }

  .footer-links a {
    color: #667eea;
    text-decoration: none;
  }

  .footer-links a:hover {
    text-decoration: underline;
  }
</style>
