<template>
  <div>
    <a v-for="(item,i) in musicList" @click="play(item)">
      <img :src="item.pic">
      <span> {{item.title}}</span>
     </a>

<!--    <div class="header">-->
<!--&lt;!&ndash;      <div class="headertop">&ndash;&gt;-->
<!--&lt;!&ndash;      </div>&ndash;&gt;-->

<!--&lt;!&ndash;      <div class="headerbottom">&ndash;&gt;-->

<!--&lt;!&ndash;        <div class="line"></div>&ndash;&gt;-->



<!--&lt;!&ndash;      </div>&ndash;&gt;-->


<!--    </div>-->

    <div class="recommend">
      <p>歌曲推荐</p>
    </div>

    <div class="difkind">
      <ul>
        <li class="foryou"><a href="#" class="foryou1">每日推荐</a></li>
        <li><a href="#">夏天哎</a></li>
        <li><a href="#">天晴便心情</a></li>
        <li><a href="#">雨的声音</a></li>
        <li><a href="#">Euphoria</a></li>

      </ul>
    </div>

    <div id ="arrows"class="arrows">
      <span  title="0" id="left"class="arrow"><a href="#"><</a></span>
      <span  title="1" id="right" class="arrow" align="right "><a href='#'>></a></span>
    </div>

    <div  id= 'content' class="content">

      <div id="turn1" class="turn1">

        <div class="tear">
          <img src="../assets/images/sun.png" width="225" height="225">
          <span class="afraid"><a href="#">hhhhh</a></span>
          <span class="bro1">播放量3.1万</span>
        </div>

        <div class="korea">
          <img src="../assets/images/3.jpeg" width="225" height="225">
          <sapn class="origin"><a href="#">kkkkk</a></sapn>
          <sapn  class="bro2">播放量347.5万</sapn>
        </div>
      </div>
    </div>

    <div class="footer">


      <div class='footer-bottom'>
        <p style="font-size:10px"><a href="#">Jian er </a>|<a href="#"> About us </a>|<a href="#"> For the Process </a> </p>
        <p>Copyright © 2020 - Forever  All Rights Reserved.</p>
        <p>  Winds in the east, mist coming in.</p>
      </div>


  </div>
  </div>

</template>

<script>
  export default {
    name: "test",
    data() {
      return {
        keyword: '',
        musicList: [],
      }
    },
    created() {
      let self = this;
      FirstMusic().then((res) => {
        //将json文件中的数据赋值给data里面的deviceList
        // console.log(res.data)
        self.musicList = res.data.musicInfo;
        this.musicList=  res.data.musicInfo.map( item => {
          const newObj ={
            pic: item.music_pic,
            title: item.music_name,
            url: item.music_url,
            time:item.music_time,
            artist:item.music_singer
          }
          return newObj
        })
      })
    },
    methods(){
      play(item)
      {
        this.$router.push({
          path:'/Play',
          query:{
            url:item.url,
            pic:item.pic,
            artist:item.artist,
            time:item.time,
            title:item.title

          }
        })

      }
    }
  }
</script>

<style scoped>
  @import "../../common/found.css";


</style>
