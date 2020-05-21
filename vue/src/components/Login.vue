<template>
  <body id="poster">
    <div class="login-wrap" v-show="showLogin">
      <h3 class="login_title">账号登录</h3>
      <p v-show="showTishi">{{ tishi }}</p>
      <input type="text" placeholder="请输入用户名" v-model="username" />
      <input type="password" placeholder="请输入密码" v-model="password" />
      <button v-on:click="login">登录</button>
      <span v-on:click="ToRegister">没有账号？马上注册</span>
    </div>

    <div class="register-wrap" v-show="showRegister">
      <h3 class="register_title">注册账号</h3>
      <p v-show="showTishi">{{ tishi }}</p>
      <input type="text" placeholder="请输入用户名" v-model="newUsername" />
      <input type="password" placeholder="请输入密码" v-model="newPassword" />
      <input
        type="password"
        placeholder="请再次输入密码"
        v-model="newPassword_again"
      />
      <input type="text" placeholder="请输入电话号码" v-model="tel" />
      <button v-on:click="register">注册</button>
      <span v-on:click="ToLogin">已有账号？马上登录</span>
    </div>
  </body>
</template>

<style>
#poster {
  background: url("../assets/eva.jpg") no-repeat;
  background-position: center;
  height: 100%;
  width: 100%;
  background-size: cover;
  position: fixed;
}
body {
  margin: 0px;
}
.login-wrap {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.register-wrap {
  border-radius: 15px;
  background-clip: padding-box;
  margin: 90px auto;
  width: 350px;
  padding: 35px 35px 15px 35px;
  background: #fff;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
}
.login_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}
.register_title {
  margin: 0px auto 40px auto;
  text-align: center;
  color: #505458;
}
input {
  display: block;
  width: 250px;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
  margin-bottom: 10px;
  outline: none;
  border: 1px solid #888;
  padding: 10px;
  box-sizing: border-box;
}
p {
  color: red;
}
button {
  display: block;
  width: 250px;
  height: 40px;
  line-height: 40px;
  margin: 0 auto;
  border: none;
  background-color: gray;
  color: #fff;
  font-size: 16px;
  margin-bottom: 5px;
}
span {
  cursor: pointer;
}
span:hover {
  color: #41b883;
}
</style>

<script>

import { setCookie, getCookie } from '../assets/js/cookie.js'
export default {
  data () {
    return {
      showLogin: true,
      showRegister: false,
      showTishi: false,
      tishi: '',
      username: '',
      password: '',
      newUsername: '',
      newPassword: '',
      newPassword_again: '',
      tel: ''
    }
  },
  mounted () {
    /* 页面挂载获取cookie，如果存在username的cookie，则跳转到主页，不需登录 */
    if (getCookie('username')) {
      this.$router.push('/home')
    }
  },
  methods: {
    login () {
      if (this.username === '' || this.password === '') {
        alert('请输入用户名或密码')
      } else {
        let data = new FormData()
        data.append('username', this.username)
        data.append('password', this.password)
        /* 接口请求 */
        this.$axios.post('/login', data).then(res => {
          // console.log('asdasdas')
          console.log(res.data)
          // alert(res.data.ret)
          /* 接口的传值是(-1,该用户不存在),(0,密码错误)，同时还会检测管理员账号的值 */
          if (res.data.ret === -1) {
            this.tishi = res.data.msg
            this.showTishi = true
          } else if (res.data.ret === 0) {
            this.tishi = '登录成功'
            this.showTishi = true
            setCookie('username', this.username, 10)
            setTimeout(function () {
              this.$router.push('/home')
            }.bind(this), 1000)
          }
        })
      }
    },
    ToRegister () {
      this.showLogin = false
      this.showRegister = true
    },
    register () {
      if (this.newUsername === '' || this.newPassword === '' || this.newPassword_again === '' || this.tel === '') {
        alert('请正确输入信息')
      } else {
        let data = new FormData()
        data.append('username', this.newUsername)
        data.append('password', this.newPassword)
        data.append('confirm_password', this.newPassword_again)
        data.append('tel', this.tel)
        this.$axios.post('/register', data).then(res => {
          console.log(res.data)
          if (res.data.ret === -1) {
            this.tishi = res.data.msg
            this.showTishi = true
          } else if (res.data.ret === 0) {
            this.tishi = '注册成功'
            this.showTishi = true
          }
        })
      }
    },
    ToLogin () {
      this.showRegister = false
      this.showLogin = true
      this.showTishi = false
    }
  }
}
</script>
