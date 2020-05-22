import Vue from 'vue';
import Router from 'vue-router';
import PageFirst from "../components/PageFirst";
import Login from "../components/login/login";
import Register from "../components/register/Register"
import showBook from "../components/showbook/showBook";
import VueResource from 'vue-resource'
import lookBook from "../components/lookBook";
import adminLogin from "../components/adminLogin";
import ManagerPage from "../components/ManagerPage";
import searchList from "../components/searchList";
import userPage from "../components/userPage";
import myRecord from "../components/myRecord";
import broadcast from "../components/broadcast";
import player from "../components/player";
import Play from "../components/Play";
import FirstPage from "../components/FirstPage";
import anotherFirst from "../components/anotherFirst";
import test from "../components/test";

// import iView from 'iview'
// import 'iView/dist/styles/iview.css'
Vue.use(Router)
Vue.use(VueResource)
// Vue.use(iView)

export default new Router({
  routes: [
    {
      path: '/',
      component:test

    },
    {
      path: '/login',
      component:Login
    },
    {
      path:'/register',
      component:Register
    },
    {
      path:'/adminlogin',
      component:adminLogin
    },

    {path:'/showBook',
      component:showBook,
    },
    {
      path:'/managerpage',
      component:ManagerPage
    },
    {
      path:'/lookBook',
      component:lookBook
    },
    {
      path:'/searchbook',
      component:searchList
    },
    {
      path:'/userpage',
      component:userPage
    },
    {
      path:'/myRecord',
      component:myRecord
    },
    {
      path:'/broadcast',
      component:broadcast
    },
    {
      path:'/play',
      component:player
    }



  ]
})
const path = require('path')
//
// 首先，在ProxyTable模块中设置了‘/api’，
// target中设置服务器地址，也就是接口的开头那段地址，
// 例如‘172.0.0.1’，然后我们在调用接口的时候，
// 就可以全局使用‘/api’，这时候‘/api’的作用就相当于‘172.0.0.1’，
// 比如接口的地址是‘172.0.0.1/user/info’，我们就可以使用‘/api/user/info’
//
// 那pathRewrite是用来干嘛的呢，
// 这里的作用，相当于是替代‘/api’，如果接口中是没有api的，
// 那就直接置空，就像我截图的一样，如果接口中有api，
// 那就得写成{‘^/api’:‘/api’}，可以理解为一个重定向或者重新赋值的功能。
