<template>
  <div>

    <div class="jumbotron" id="reg-top" >
      <div class="container" id="register">
        <p>Build a house of your imaginings ere you build a house within the city walls</p>
      </div>
    </div>


    <div>
      <div style="padding:30px 0;">
        <a-player :music="songList" :show-lrc="true" :narrow="false" theme="#b7daff" mode="circulation" v-if="flag" list-max-height='96px' ref="player"></a-player>
        <p></p>

      </div>
  </div>

      <i class="iconfont  shoucang el-icon-goods " :class="{'active':isSelected}" @click="toggleCollect">收藏</i>
      <p></p>
      <i class="iconfont download el-icon-download " :class="{'active':isdownload}" @click="download">下载</i>
    <a :href="songList.src" download="music">下载</a>

<!--    <a-player autoplay :music="{-->
<!--  title: 'Preparation',-->
<!--  author: 'Hans Zimmer/Richard Harvey',-->
<!--  src: 'http://ws.stream.qqmusic.qq.com/C400003PF4kK0xqo1t.m4a?guid=4776407682&vkey=232C8C81C49F0E35C5DC67A4B04462B3EA05FA82CA26A30EF5BE5BD87DF3E7246032CD0EA3B0EDD4DA336E502657FAA5E0035D4D2B445056&uin=0&fromtag=66',-->
<!--  pic: 'http://devtest.qiniudn.com/Preparation.jpg',-->
<!--  lrc: '[00:00.00]lrc here\n[00:01.00]aplayer'-->
<!--}">-->
<!--    </a-player>-->

   </div>


</template>

<!--vue中使用通过ref来获取dom元素 ，如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素; -->
<!--如果用在子组件上，引用就指向组件实例-->
<!--当 v-for 用于元素或组件的时候，引用信息将是包含 DOM 节点或组件实例的数组-->
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
    name: "broadcast",
    components:{
      'a-player': VueAplayer
    },
    data: function () {
      return {
        flag:true,
        musicList:'',
        // songList:[],
        isSelected:false,
        isdownload:false,
        songList: {
          title: 'aLIEz',
          artist: '澤野弘之',
          pic: 'http://pic.xiami.net/images/album/img31/59831/7064167921410329023_1.jpg',
          src: 'http://ws.stream.qqmusic.qq.com/C400003PF4kK0xqo1t.m4a?guid=4776407682&vkey=232C8C81C49F0E35C5DC67A4B04462B3EA05FA82CA26A30EF5BE5BD87DF3E7246032CD0EA3B0EDD4DA336E502657FAA5E0035D4D2B445056&uin=0&fromtag=66',
          lrc: null
        },
      //   songList:{
      //     title:'',
      //         artist:'',
      //     pic:'',
      //     src:'',
      //     lrc:null
      //
      // }


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
  .emailform{
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
  .shoucang{
    font-size: 32px;
  }
  .shoucang.active{
    color: palevioletred;
  }

  .download{
    font-size: 32px;
  }
  .download.active{
    color: #b3d8ff;
  }


</style>
