// vue.config.js
module.exports = {
    outputDir: '../flask/static/dist',
    devServer: {
      proxy: 'http://localhost:5000'  
    },
    pwa: {
      name: 'HANG OUT',
      themeColor: 'black',//浏览器工具栏的主题颜色
      msTileColor: 'black',//Windows 设备上磁贴的背景颜色
      appleMobileWebAppCapable: 'yes',//全屏模式显示
      appleMobileWebAppStatusBarStyle: 'black',//设置 iOS 设备上的状态栏的样式颜色
      workboxOptions: {
        // skip waiting on the new service worker
        skipWaiting: true,
        clientsClaim: true,
      }
    }
  }
    