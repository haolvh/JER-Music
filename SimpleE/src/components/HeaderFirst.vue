<template>
  <div class="navbar navbar-default navbar-fixed-top">
    <ul class="container">
      <ul class="navbar-header">
        <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a href="reactive.html" class="navbar-brand">简迩音乐</a>
      </ul>


      <ul class="navbar-collapse  collapse">
<!--        注释-->


        <ul class="nav navbar-nav navbar-right">
          <li class="dropdown">
            <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              admin
              <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="dLabel">
              <li> <a href="#"><span class="glyphicon glyphicon-grain" @click="toLogin">学生</span> </a></li>
                <li> <a href="#"><span class="glyphicon glyphicon-grain" @click="toTest">test</span> </a></li>
            </ul>


          </li>
          <li><a href="#bbs"> <router-link to ='/' ><span class="glyphicon glyphicon-off"></span></router-link></a></li>

        </ul>
      </ul>
    </ul>
  </div>

  <!--  <div>-->
<!--    <nav class="navbar navbar-default navbar-fixed-top">-->
<!--      <div class="container">-->
<!--        <div class="navbar-header">-->
<!--          <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">-->
<!--            <span class="icon-bar"></span>-->
<!--            <span class="icon-bar"></span>-->
<!--            <span class="icon-bar"></span>-->
<!--          </button>-->
<!--          <a href="reactive.html" class="navbar-brand">图书管理</a>-->
<!--        </div>-->


<!--        <div class="navbar-collapse  collapse">-->
<!--          <ul class="nav navbar-nav">-->
<!--            <li class="active"><span class="glyphicon glyphicon-cloud">后台首页</span><span class="glyphicon glyphicon-user"><router-link to="/login"  v-slot="{ href, route, navigate, isActive, isExactActive }">注册</router-link></span></li>-->

<!--            <li><span class="glyphicon glyphicon-leaf">查找</span></li>-->
<!--            <li><a><span class="glyphicon glyphicon-book">借阅书籍</span></a></li>-->
<!--          </ul>-->
<!--          <ul class="nav navbar-nav navbar-right">-->
<!--            <li class="dropdown">-->
<!--              <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">-->
<!--                admin-->
<!--                <span class="caret"></span>-->
<!--              </a>-->
<!--              <ul class="dropdown-menu" aria-labelledby="dLabel">-->
<!--                <li> <a href="#"><span class="glyphicon glyphicon-tree-deciduous"> 昂</span>  </a></li>-->
<!--                <li> <a href="#"><span class="glyphicon glyphicon-grain"> keke</span> </a></li>-->
<!--              </ul>-->

<!--            </li>-->

<!--          </ul>-->
<!--        </div>-->
<!--      </div>-->
<!--    </nav>-->
<!--  </div>-->
</template>

<script>
  import {GetRes} from "../api/finalApi";
  const ColorThief = require('colorthief');
  export default {
    name: "HeaderFirst",
    //组件的方法methods,所有的方法都应该在methods里定义，然后在created或者mounted里 使用this调用方法，用这种方式实现初始化
    methods: {
      toLogin() {
        this.$router.push('/broadcast')

    },
      created()
      {
        GetRes().then((res) => {
          console.log(res)
        })
      }
      ,
      toManage() {
        this.$router.push('/adminlogin')
      },
      tobroadcast() {
        this.$router.push('/broadcast')
      } ,
      toTest() {
        GetRes().then((res) => {
          console.log(res)
        })
      }
    },

  }
</script>

<style scoped>
  body{
    font-family: 'Microsoft Sans Serif';
  }
  #getDark{
    background-color: #0f0f0f;
  }

  /*给图标加背景*/
  .maiziicon{
    background: #3c3c3c;
    color: #fff;
    border-radius: 50%;
    width:40px;
    height: 50px;
    text-align: center;
    line-height: 40px;
    margin-rigrfht: 10px;
  }

  .navbar-default{
    background-color: #fff;
    border:none;
    box-shadow:0px 5px 10px 0px  #31708f;


  }
  .navbar-default .navbar-brand{
    font-size: 30px;
    font-weight: bold;
    color:#337ab7;
    height: 70px;
    line-height: 35px;

  }
  .navbar-default .navbar-nav>li>a{
    height:70px;
    line-height: 40px;
    font-size:16px;
    font-weight: bold;
  }

  .navbar-default .navbar-toggle{
    border-color: #5bc0de;
    background-color: #afd9ee;
  }
  .navbar-default .navbar-toggle .icon-bar{
    background-color: #31708f;
  }
  #home{
    background: url("../assets/images/4.png");
    background-size: 100% 700px;
    margin-top:70px;
    text-align: center;
    color:#fff;
    margin-top:70px;
  }
  .darker{
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.2);
    padding:90px 0;
    border-radius: 1%;
    box-shadow: -10px 5px 5px #b3b7b2;;
  }
  .p1{
    font-size: 20px;
    margin-bottom: 30px;
    color: lavender;
  }
  .p2{
    color: lavender
  }
  .soshut{
    width:90%;

    border-radius: 20%;
  }
  .col-md-4 img{
    border-radius: 50%;
    width:200px;
    height:200px;
  }
  #bbs{
    padding:100px;
    text-align:center;
    background: url("../assets/images/2.png");
    background-size: 100% 100%;
    border-radius: 5%;
    box-shadow: -10px -5px 15px #ce8483;
    margin: 0 auto;
  }
  #bbs a:hover{
    color: #ce8483;
    text-decoration: none;
  }
  #bbs h1{
    font-size: 18px;
    font-weight: bold;

  }
  #bbs p{
    font-size: 15px;
  }
  #bbs img{
    margin:0 auto;
  }

  #poem{
    padding:80px;
    text-align:center;
    background: url("../assets/images/10.jpeg");
    background-size: 100% 100%;
    border-radius: 5%;
    box-shadow: -10px -5px 15px #5e5e5e;
    padding: 0 auto;

  }
  #poem p{
    font-size: 16px;
    color: #5e5e5e;
    line-height: 40px;
  }
  #three{
    background: url("../assets/images/sun.png") no-repeat;
    background-size: 100% 100%;
    height:600px;
    border-radius: 10%;

  }
  .lvjing2{
    width:100%;
    height:100%;
    background:rgba(0,0,0,0.2);
    border-radius: 1%;

  }
  .three{
    margin:0 auto;

  }
  footer{
    text-align: center;
    width:100%;
    color:#9d9d9d;
    background: #31708f;
    padding:20px 20px;
    line-height: 30px;

  }
  .active{
    color: #0f0f0f;
  }


</style>
