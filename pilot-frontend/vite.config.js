import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

// Use backend:8000 in Docker, localhost:8000 for local dev
const BACKEND_URL = process.env.DOCKER_ENV ? 'http://backend:8000' : 'http://localhost:8000';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/media': {
				target: BACKEND_URL,
				changeOrigin: true
			},
			'/api': {
				target: BACKEND_URL,
				changeOrigin: true
			}
		}
	}
});
