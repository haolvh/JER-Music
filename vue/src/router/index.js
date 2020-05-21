// import Vue from 'vue'
// import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
// import Login from '@/components/Login'

// Vue.use(Router)

// export default new Router({
//   routes: [
//     {
//       path: '/',
//       name: 'HelloWorld',
//       component: HelloWorld
//     }
//     {
//       path: '/',
//       name: 'Login',
//       component: Login
//     }
//   ]
// })

import Vue from 'vue'
import Router from 'vue-router'
/* 引入页面 */
import Main from '@/components/Main'
import Home from '@/components/Home'
import Test from '@/components/Login'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)

/* 配置路由 */
export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/login',
      name: 'Test',
      component: Test
    },
    {
      path: '/main',
      name: 'Main',
      component: Main
    },
    {
      path: '/home',
      name: 'Home',
      component: Home
    }
  ]
})
