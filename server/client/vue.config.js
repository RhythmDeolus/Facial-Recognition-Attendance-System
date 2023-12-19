const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  outputDir: "../dist",
  //relative to outputDir
  assetsDir: "static",
  transpileDependencies: true
})
