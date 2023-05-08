const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  chainWebpack: (config) => {
    config.module
      .rule('url-loader')
      .test(/\.(woff|woff2|eot|ttf|otf)$/i)
      .use('url-loader')
      .loader('url-loader')
      .options({
        limit: 8192,
        fallback: require.resolve('file-loader'),
        name: 'fonts/[name].[hash:8].[ext]',
      })
      .end();
  },
})
