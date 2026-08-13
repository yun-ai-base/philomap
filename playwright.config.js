// Playwright 冒烟测试配置
// 本地静态服务器由 webServer 自动启动（Python http.server），无需手动开服务
const { defineConfig } = require('@playwright/test');

module.exports = defineConfig({
  testDir: './tests',
  timeout: 30000,
  retries: 0,
  workers: 1, // 单 worker，避免多个页面并发请求导致数据竞争
  preserveOutput: 'always', // 不清理 test-results，避免沙箱 trash 拦截
  outputDir: 'C:/Users/yun/AppData/Local/Temp/philomap-test-results',
  use: {
    baseURL: 'http://127.0.0.1:8911',
    headless: true,
    viewport: { width: 1440, height: 900 },
    actionTimeout: 10000,
    trace: 'off',
  },
  webServer: {
    command: '"C:/Users/yun/.workbuddy/binaries/python/versions/3.13.12/python.exe" -m http.server 8911 --bind 127.0.0.1',
    url: 'http://127.0.0.1:8911/index.html',
    reuseExistingServer: true,
    timeout: 15000,
  },
});
