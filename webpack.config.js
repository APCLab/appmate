const path = require('path')
const webpack = require('webpack')

module.exports = {
	entry: {
    app: './appmate/static/js/app.js',
  },
	output: {
		path: path.resolve(__dirname, './appmate/static/js'),
		filename: 'build.js',
	},
  resolveLoader: {
    root: path.join(__dirname, 'node_modules'),
  },
	module: {
		loaders: [
			{
				test: /\.vue$/,
				loader: 'vue',
			},
			{
				test: /\.js$/,
				loader: 'babel',
				exclude: /node_modules/,
			},
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file',
        query: {
          name: '[name].[ext]?[hash]'
        }
      },
		]
  },
  babel: {
    presets: ['es2015'],
    plugins: ['transform-runtime'],
  },
  // plugins: [
  //   new webpack.ProvidePlugin({
  //     $: "jquery",
  //     jQuery: "jquery",
  //     "window.jQuery": "jquery",
  //     semantic: "./static/semantic/semantic.min.js",
  //   }),
  // ]
}
