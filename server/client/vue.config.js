const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    //relative to outputDir
    devServer: {
        proxy: {
            '/api_1': {
                target: 'http://127.0.0.1:8000'
            }
        },
        port: 4000,
    },
    transpileDependencies: true,
    lintOnSave: false,
})
