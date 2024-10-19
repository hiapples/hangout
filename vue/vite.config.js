// vite.config.js
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue'; // 如果你使用的是 Vue

export default defineConfig({
  plugins: [vue()], // 插件配置
  server: {
    host: 'localhost', // 服务器主机
    port: 5173,       // 服务器端口
    open: true,       // 启动时自动打开浏览器
  },
  build: {
    outDir: 'dist', // 构建输出目录
  },
});
