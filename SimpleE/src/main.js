// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
// 安装其他插件的时候，可以直接在 main.js 中引入并 Vue.use()，但是 axios 并不能 use，只能每个需要发送请求的组件中即时引入
// ：即使已经在 main.js 中引入了 axios，并改写了原型链，也无法在 store.js 中直接使用 $ajax 命令
// 当请求成功时，会执行 .then，否则执行 .catch

// 这两个回调函数都有各自独立的作用域，如果直接在里面访问 this，无法访问到 Vue 实例

// 这时只要添加一个 .bind(this) 就能解决这个问题

// 换言之，这两种方案是相互独立的
// axios 改写为 Vue 的原型属性

// 首先在主入口文件main.js中引用，之后挂在vue的原型链上

// import axios from 'axios'
// Vue.prototype.$ajax= axios
//
// 在组件中使用
//
// this.$ajax.get('api/getNewsList').then((response)=>{
//   this.newsList=response.data.data;
// import App from './App'
// import router from './router'
import './assets/css/bootstrap.css'
import './assets/js/bootstrap.js'
import Global from './components/util/Global'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'default-passive-events'
import Axios from 'axios'
Vue.use({ Axios});
// import 'element-ui/lib/theme-chalk/index.css'; // 默认主题
// import store from './store/store'
// import './assets/css/theme-green/index.css'; // 浅绿色主题
// import './assets/css/icon.css';
// import api from './api/index'
// import './assets/iconfont/iconfont.css'
Vue.prototype.HOST ='/api'
Vue.prototype.GLOBAL = Global
Vue.config.productionTip = false
// Vue.prototype.$axios = axios
axios.defaults.baseURL = '/apis'
import axios from '../node_modules/axios'
Vue.prototype.$axios = axios
Vue.use(ElementUI)
import store from './store/store'
import $ from 'jquery'
import Vue from 'vue'
import App from './App'
import router from './router'
Vue.config.productionTip = false
import Router from 'vue-router'
const routerPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return routerPush.call(this, location).catch(error=> error)
}
// Vue.config.productionTip = false
/* eslint-disable no-new */
// 设置请求头部content-type:application/x-www-form-urlencoded
// Vue.http.options.emulateJSON = true
// Vue.http.options.emulateHTTP = true
// Vue.http.options.xhr = { withCredentials: true }
new Vue({
  el: '#app',
  router,
  // axios,
  store,
  components: { App },
  template: '<App/>'
})
