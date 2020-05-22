import Vue from 'vue'
import Vuex from 'vuex'
Vue.use(Vuex)

const state= {
  // user: JSON.parse(localStorage.getItem('user')) || '',
  src:'',
  pic:'',
  title:'',
  time:''
}
const mutations={
  LOGIN(state){
    // state.user=JSON.parse(localStorage.getItem('user'))
  },
  LOGOUT(state){
    state.user=''
  },
 ADMINLOGIN(state){
    // state.administer=JSON.parse(localStorage.getItem('administer'))
  },
  ADMINLOGOUT(state)
  {
    state.adminer = ''
  },
  getSong(state)
  {

  }


}
// mutations设置状态state actions驱动mutations
const actions= {
  login({commit}) {
    commit('LOGIN')
  },
  // 用户登出
  logout({commit}) {
    commit('LOGOUT')
  },
  adminlogin({commit}) {
    commit('ADMINLOGIN')
  },
  // 管理员登录
  adminlogout({commit}) {
    commit('ADMINLOGOUT')

  }
}

export default new Vuex.Store({
  state,
  mutations,
  actions,

})






