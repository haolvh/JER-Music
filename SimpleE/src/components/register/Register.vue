<template>
    <div>
      <div class="jumbotron" id="reg-top" >
        <div class="container" id="register">
          <p>Join us</p>
        </div>
      </div>
      <el-form
        :model="RegisterData"
        ref="RegisterData"
        class="regform"
        label-width="0">

        <el-form-item  prop="email" >
          <label >邮箱</label>
          <el-input type="text" v-model="RegisterData.email" class="form"  placeholder="邮箱"></el-input>
        </el-form-item>

        <el-form-item  prop="username" >
          <label >账户名</label>
          <el-input type="text" v-model="RegisterData.username" class="form"  placeholder="用户名"></el-input>
        </el-form-item>

        <el-form-item>
          <label >设置密码</label>
          <el-input  type="password" v-model="RegisterData.password" class="form" placeholder=" 密码"></el-input>
        </el-form-item>

        <el-form-item>
          <label>
            <input type="checkbox"> Check me out
          </label>

        </el-form-item>

        <el-form-item >
          <el-button
            type="primary"
            class="submitBtn  btn btn-default " plain
            @click.native.prevent="submit"
          >
            注册
          </el-button>

          <hr>
          <p>已经有账号，马上去<span class="to" ><el-button @click="toLogin">登录</el-button></span></p>
        </el-form-item>


      </el-form>
    </div>

  </template>


<script>
  import {UserRegister} from  '../../api/finalApi'
  import QS from 'qs'
  export default {
    name: "Register",
    data() {
      return {
          RegisterData: {
            email:'',
            username: '',
            password: '',
          },


          }
        },
    methods: {

      submit() {
        let RegisterData = {
          email: this.RegisterData.email,
          username: this.RegisterData.username,
          password: this.RegisterData.password,
        }
        let _RegisterData = QS.stringify(RegisterData)
        // 调用借口，执行axios请求获取返回的数据
        UserRegister(_RegisterData).then(res => {
          console.log(res)
          // 让页面给个提示
          this.$message({
            type: 'success',
            message: '注册成功'
          })
          this.$router.push('/userpage')
          // localStorage.setItem('user', JSON.stringify(user))
          // this.$store.dispatch('login')
          // this.route.push('/lookbook')
        })

      },
      toLogin() {
        this.$router.push('./login')
    },


      }

  }

</script>

<style scoped>
  #register{
    font-size: 30px;

  }


  .form{
    margin: 0 auto;
    padding: 0;
    height: 34px;
    line-height: 1.42857143;
    color: #555;
    background-color: #fff;
    background-image: none;
    border-radius: 4px;
    transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s, -webkit-box-shadow ease-in-out .15s;
    width:200px
  }
  .confirmpass{

    width: 30%;
    margin: 0 auto;


  }



</style>
