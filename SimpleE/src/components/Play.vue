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


                <!--          <img src= '../assets/images/6.jpg' class="img-responsive soshut">-->
                  <a-player  class= "broadcast" :music="songList" :show-lrc="true" :narrow="false" theme="#b7daff" mode="circulation" v-if="flag" list-max-height='96px' ref="player"></a-player>
                  <p></p>


  <i class="iconfont  shoucang el-icon-goods " :class="{'active':isSelected}" @click="toggleCollect"> 收藏</i>
  <p></p>
  <i class="iconfont download el-icon-download " :class="{'active':isdownload}" @click="download"><a :href="songList.src"  class="down" download="music"> 下载</a></i>

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
  import { Message } from 'element-ui';
  import {GetMusicInfo} from '../api/finalApi'
  import QS from 'qs'
  import axios from 'axios'
  import VueAplayer from 'vue-aplayer'
  import saveAs from 'file-saver';
  var FileSaver = require('file-saver');
  VueAplayer.disableVersionBadge = true
  export default {
    name: "Play",
    components:{
      'a-player':VueAplayer
    },
    data: function () {
      return {
        flag:true,
        musicList:'',
        // songList:[],
        isSelected:false,
        isdownload:false,
        // songList: {
        //   title: 'aLIEz',
        //   artist: '澤野弘之',
        //   pic: this.$route.query.music_pic,
        //   src: 'http://ws.stream.qqmusic.qq.com/C400003PF4kK0xqo1t.m4a?guid=4776407682&vkey=232C8C81C49F0E35C5DC67A4B04462B3EA05FA82CA26A30EF5BE5BD87DF3E7246032CD0EA3B0EDD4DA336E502657FAA5E0035D4D2B445056&uin=0&fromtag=66',
        //   lrc: null
        // },
          songList:{
            title:this.$route.query.title,
            artist:this.$route.query.artist,
            pic:this.$route.query.pic,
            src:this.$route.query.src,
            lrc:null

        }


      };

    },
    // created() {
    //   let self = this
    //   GetBooksInfo().then((res) => {
    //     //将json文件中的数据赋值给data里面的deviceList
    //     // console.log(res.data)
    //     self.bookList = res.data.bookInfo
    //   })
    // },
    async mounted () {
//异步加载，先加载出player再使用
//       await this.init();
      let aplayer = this.$refs.player.control;
      aplayer.play();
    },

    methods: {

      async init () {

        let url = '';
        let res = await GetMusicInfo( 'http://musictest.free.idcfengye.com');
        //以下就是这边对请求的一个处理，看接口了
        if(res&&res.ret==0){
          this.songList = res.data;
          this.songList.title=res.data.songname;
          this.songList.artist=res.data.author;
          this.songList.src=res.data.url;
          this.songList.pic='http://pic.xiami.net/images/album/img31/59831/7064167921410329023_1.jpg';
        }
//因为是异步请求，所以一开始播放器中是没有歌曲的，所有给了个v-if不然会插件默认会先生成播放器，导致报错(这个很重要)
        this.flag = true;
      },

      download()
      {

        this.isdownload= !this.isdownload
        // FileSaver.saveAs(obj.url)
      },

      toggleCollect(){
        this.isSelected = !this.isSelected

        let returnData = {
          songname:this.songList.title,
        }
        console.log(this.returnBook)
        // console.log(returnData)
        returnPost(returnData).then(res => {
          this.$message({
            type: 'success',
            message: '收藏成功'
          })


        }).catch(err => {
          console.log(err)
        })
        // this.$router.push('/userpage')
      }



    },






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
  .shoucang{
    font-size: 16px;
  }
  .shoucang.active{
    color: palevioletred;
  }

  .download{
     color: white;
    font-size: 16px;
  }
  .download.active{
    color: #b3d8ff;
  }
.broadcast
{
  margin-top:100px;
}
  .down{
    color: white;
  }
</style>
