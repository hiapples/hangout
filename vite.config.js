import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue'; // If you're using Vue

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 3000, // Change the port if needed
    open: true, // Opens the browser automatically
    cors: true, // Enable CORS
  },
  build: {
    outDir: 'dist', // Output directory for build files
    sourcemap: true, // Enable sourcemaps for debugging
  },
  resolve: {
    alias: {
      '@': '/src', // Set up alias for src directory
    },
  },
});
