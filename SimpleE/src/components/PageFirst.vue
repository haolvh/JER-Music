<template>
  <div>


<section id="home">
  <ul class="darker">
    <ul class="container">
      <ul  class="row">
        <ul class="col-md-1"></ul>
        <ul class="col-md-10">
          <p class="p1">长久地遗忘着屋顶</p>
          <p class="p1">却永记屋顶之上的天空</p>

          <p class="p2" >任何事物都不会再次发生</p>
          <p class="p2" >重现时也不相同</p>
          <p class="p2" > 因此我们出生时毫无经验</p>
          <p class="p2" >死时也总是感到陌生</p>
<!--          <img src= '../assets/images/6.jpg' class="img-responsive soshut">-->

        </ul>
        <ul class="col-md-1">

        </ul>



      </ul>
    </ul>
  </ul>



</section>





<section id="three">

  <div class="lvjing2">

    <div class="container">

      <div class="row">

        <div class="col-md-6 circle"></div>
        <div class="col-md-6 circle"></div>




      </div>
    </div>
  </div>
</section>

<footer>
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <p>
          ©&nbsp lalalalahahahage
        </p>
      </div>
    </div>
  </div>
</footer>

</div>
</template>
<script>
  import axios from 'axios'
  import  VueAplayer from 'vue-aplayer'
  export default {
    name: "PageFirst",
     components:{
      'a-player':VueAplayer
     },
    data() {

      return {


      }

    }
  }
</script>

<style scoped>
  body{
    font-family: 'Microsoft Sans Serif';
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
    margin-right: 10px;
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
