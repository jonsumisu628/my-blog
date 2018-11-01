# react-material-starter

## Getting Started
### Prerequisites

```bash
$ yarn -v
1.7.0

$ node -v
v10.9.0
```

### Development

#### Setup
```bash
$ yarn
```

#### Debug
```bash
$ yarn

$ yarn start
```

#### Commands
```bash
# open browser with webpack-dev-server in development mode
$ yarn start
# open browser with webpack-dev-server in production mode
$ yarn start:prod
# build Project in development mode
$ yarn build
# build Project in development mode
$ yarn build:dev
# build Project in production mode
$ yarn build:prod
# remove cache of hard-source-webpack-plugin
$ yarn cache-clean
# chack typescript lint with tslint
$ yarn lint
# show ubndle size of webpack
$ yarn size-analyze
# generate project documents
$ yarn docs
# deploy #  blank
$ yarn deploy
```

#### file size analyze
##### cmd
```bash
$ yarn size-analyze
```

##### web-view
uncomment `// new BundleAnalyzerPlugin()` in `webpack.config.(dev|prod).js`
```js
...
    plugins: [
        new BundleAnalyzerPlugin(), // <- uncomment
        new DefinePlugin(
            Object.entries(process.env)
                .map(x => ({["process.env." + x[0]]: JSON.stringify(x[1])}))
                .reduce((x, y) => Object.assign(x, y), {}),
        )
    ],
...
```

#### Generate Documents
```bash
$ yarn docs
```
