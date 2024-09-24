// vue.config.js
module.exports = {
    outputDir: 'dist',
    devServer: {
      proxy: 'http://localhost:8000'  // PHP 服务器的地址
    },
    pwa: {
      name: 'HANG OUT',
      themeColor: '#292929',//浏览器工具栏的主题颜色
      msTileColor: '#292929',//Windows 设备上磁贴的背景颜色
      appleMobileWebAppCapable: 'yes',//全屏模式显示
      appleMobileWebAppStatusBarStyle: 'black',//设置 iOS 设备上的状态栏的样式颜色
      workboxOptions: {
        // skip waiting on the new service worker
        skipWaiting: true,
        clientsClaim: true,
      }
    }
  }
    