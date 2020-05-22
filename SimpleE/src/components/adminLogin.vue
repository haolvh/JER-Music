<template>
  <div>
    <div class="jumbotron" id="reg-top" >
      <div class="container" id="register">
        <p>Welcome</p>
      </div>
    </div>


    <el-form :model="AdminLoginForm" :rules="rules"  ref="LoginForm" label-width="0px" class="ms-content">
      <el-form-item  prop="username" >
        <label >username</label>
        <el-input type="text" v-model="AdminLoginForm.username" class="form"  placeholder="用户名"></el-input>
      </el-form-item>

      <el-form-item prop="password">
        <label >Password</label>
        <el-input  type="password" v-model="AdminLoginForm.password" class="form" placeholder=" 密码"></el-input>
      </el-form-item>


      <el-button type="checkbox" :loading="logining"   @click.native.prevent="submitForm" class="btn btn-default" >登录</el-button>
      <!--//prevent阻止默认-->


    </el-form>
  </div>

</template>
<!--vue中使用通过ref来获取dom元素 ，如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素; -->
<!--如果用在子组件上，引用就指向组件实例-->
<!--当 v-for 用于元素或组件的时候，引用信息将是包含 DOM 节点或组件实例的数组-->

<script>
  // import {LoginU} from '../../api/newapi'
  import $ from 'jquery'
  import { Message } from 'element-ui';
  import {AdminLogin} from '../api/finalApi'

  export default {
    name: "adminLogin",
    components:{
    },
    data: function () {
      return {
        AdminLoginForm: {
          adminname: '',
          password: '',


        },
        logining: false,
        rules: {
          adminname: [{required: true}],
          password: [{required: true,max:14,min:6,trigger:blur}]
        }
      };

    },

    methods: {
      submitForm() {
        this.$refs.AdminLoginForm.validate(valid => {
          if (valid) {
            this.logining = false
            // console.log('开始请求后台数据，验证返回之类的操作！')
            // 登录作为参数的用户信息
            let LoginParams = {
              adminname: this.AdminLoginForm.adminname,
              password: this.AdminLoginForm.password
            }
            // 调用axios登录接口
            AdminLogin(LoginParams).then(res => {
              console.log('jhhh')
              console.log(res)
              this.logining = false
              // 根据返回的code判断是否成功
              let {code, msg, user} = res.data
              if (code !== 200) {
                this.$message({
                  type: 'error',
                  message: msg
                })
              } else {
                this.$message({
                  type: 'success',
                  message: msg
                })
                // 将返回的数据注入sessionStorage
                localStorage.setItem('user', JSON.stringify(user))
                // 在这里挂上，官方说的分发，登录的action
                this.$store.dispatch('login')
                // console.log(user)
                // 跳转到我的信息的页面
                this.$router.push('/managerpage')

              }
            })

          } else {
            console.log(' login error')
          }
        })

      },

      toregin() {
        this.$router.push('/managepage')


      }
    }
  }
  // localStorage和sessionStorage属性允许在Web浏览器中保存键/值对。
  // localStorage对象存储没有过期日期的数据。
  // 当浏览器关闭时，数据不会被删除，并且将在第二天，一周或一年中可用。
  // localStorage属性是只读的
  //   保存数据到localStorage的语法：
  // localStorage.setItem("key", "value");
</script>

<style scoped>
  #reg-top{
    background: #2b669a;
  }
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






  #registerButton{
    border-radius:10%;
  }





</style>
