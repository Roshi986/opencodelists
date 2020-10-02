const path = require("path");

module.exports = {
  entry: {
    builder: "./static/src/js/builder/index.jsx",
    codelist: "./static/src/js/codelist.js",
    "codelist-version": "./static/src/js/codelist-version.js",
    tree: "./static/src/js/tree/index.jsx",
  },
  output: {
    path: path.resolve(__dirname, "static", "dist", "js"),
    filename: "[name].bundle.js",
  },
  resolve: {
    extensions: [".js", ".jsx"],
  },
  module: {
    rules: [
      {
        test: /\.jsx$/,
        loader: "babel-loader",
      },
    ],
  },
};
