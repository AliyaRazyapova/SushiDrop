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

const webpack = require('webpack');

module.exports = {
  configureWebpack: {
    resolve: {
      fallback: {
        crypto: require.resolve('crypto-browserify'),
        util: require.resolve('util/'),
        stream: require.resolve('stream-browserify'),
      },
    },
    plugins: [
      new webpack.ProvidePlugin({
        process: 'process/browser',
      }),
    ],
  },
};

