import Vue from 'vue'
import Router from 'vue-router'
// import Singer from 'cpnts/singer/singer'
// import Recommend from 'cpnts/recommend/recommend'
// import Rank from 'cpnts/rank/rank'
// import Search from 'cpnts/search/search'
// import MusicList from 'cpnts/music-list/music-list'
// import SingerDetail from 'cpnts/singer-detail/singer-detail'
// import RankDetail from 'cpnts/rank-detail/rank-detail'
// import User from 'cpnts/user/user'

Vue.use(Router)

const Recommend = (resolve) => {
  import('../components/recommend').then((module) => {
    resolve(module)
  })
}

const SList = (resolve) => {
  import('../components/Slist').then((module) => {
    resolve(module)
  })
}

export default new Router({
  routes: [

    {
      path: '/index',
      component: Recommend,
    },

    {
      path: '/index/slist',
      component: SList
    },

  ]
})
