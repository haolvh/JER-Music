<template>
  <div>

  <div id="marTop" >

<!--    <div class="search">-->
<!--&lt;!&ndash;      <div class="search-box">&ndash;&gt;-->
<!--      <div class="yuyin"></div>-->
<!--      <div class="input" @click="showlist">-->
<!--      <el-input type="text" v-model="keyword" class="input" placeholder="请输入搜索内容" id="inputvalue"></el-input>-->
<!--      <el-button type="info" plain class="btn" @click="search">搜索</el-button>-->
<!--    </div>-->
<!--    </div>-->
<!--    <div>-->

      <div class="search" >
        <div class="yuyin"></div>
        <div class="input">
<!--                  <input type="text" value="" placeholder="搜索音乐、歌曲、电台" id="inputvalue"@keydown="search">-->
          <el-input type="text"  class="input" value="" id="inputvalue" placeholder="请输入搜索内容"></el-input>
<!--          <el-button type="info" plain class="btn" value="" placeholder="搜索音乐、歌曲、电台"  >搜索</el-button>-->
        </div>
      </div>

      <el-button type="info" plain class="btn" value="" placeholder="搜索音乐、歌曲、电台" @click="search" >搜索</el-button>




      <h2 v-if="isShowTip">没有搜索到匹配结果</h2>
  </div>
<!--    </div>-->
<!--  </div>-->

    <el-table
      :data="resultList"
      style="width: 100%">

      <el-table-column type="index">
      </el-table-column>

      <el-table-column
        prop="title"
        label="歌曲名"
        width="290">

      </el-table-column>

      <el-table-column
        prop="singer"
        label="歌手"
        width="290">
      </el-table-column>

      <el-table-column
        prop="time"
        label="播放时长" width="290">
      </el-table-column>

    </el-table>


  <a v-for="(item,i) in musicList">
    <img src="item.pic">
    <span> {{item.title}}</span>
    </a>

</div>
</template>

<script>

  import {GetBooksInfo,FirstMusic} from "../api/finalApi";
  export default {


    data() {
      return {
        keyword: '',
        musicList: [],
        resultList: [],
        isShowTip: false
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
            pic: item.picUrl,
            title: item.mucisTitle,
            url: item.musicUrl,
            time:item.time,
            singer:item.singer
          }
          return newObj
        })
      })
    },
    methods: {
      search() {
        if (this.keyword == '') {   //如果没有输入内容，不让往下执行
          return
        } else {
          this.resultList = []   //每次搜索对结果数组做初始化
          this.musicList.forEach((item) => {  //把初始数据进行遍历
            /**
             下面是把初始数据中的每一条数据的四个字段分别去和输入的内容进行匹配，
             如果某一字段中包含输入的内容，就往resultList中加
             **/
            if (item.title.indexOf(this.keyword) > -1 ||
                 item.singer.indexOf(this.keyword) > -1 ){
              this.resultList.push(item)
            }
            });
          if (this.resultList.length== 0) {   //如果没有匹配结果，就显示提示信息
            this.isShowTip = true
          }
          this.resultList.map((item) => {  //遍历
            item.title = this.brightKeyword(item.title)
            item.singer = this.brightKeyword(item.singer)
          }) //到这里search方法结束
        }
        console.log(this.resultList)
      },
      // searchMusic() {
      //   //调用接口
      //   this.$http.get(`https://autumnfish.cn/search?keywords=${this.inputValue}`).then(response => {
      //     // console.log(response);
      //     //将结果添加到musicList中
      //     this.musicList = response.body.result.songs;
      //
      //
      //   }, response => {
      //     // error callback
      //     alert("出错了")
      //   });
      // },
      brightKeyword(val) {
        let keyword = this.keyword   //获取输入框输入的内容
        if (val.indexOf(keyword) !== -1) {  //判断这个字段中是否包含keyword
          //如果包含的话，就把这个字段中的那一部分进行替换成html字符
          return val.replace(keyword, `${keyword}`)
          // return val
        } else {
          return val
        }
      }
    }
  }



</script>

  /*#marTop*/
  /*{*/
  /*  margin-top:10%*/
  /*}*/
  /*#miniColumn{*/
  /*  width:51%;*/
  /*}*/
<style lang="stylus" rel="stylesheet/stylus">
  @import '../../common/sty.styl';
  .search
    background:#2e6da4
    height:46px
    display :flex
    margin-top: 80px;
    .yuyin
      flex-basis:80px
      background:url(../assets/images/5.png) no-repeat;
      background-position:center center
      background-size: 40px 40px
    .input
      flex:1
      input
        width:80%
        height:30px
        border-radius:5px
        margin-top:10px

        color:#c6c7c9
        font-size:12px
        padding-left:30px
    .music
      flex-basis: 40px
      text-align:center
      span
        line-height: 46px
        color: #ffffff
      img
        width: 20px
        height: 20px
        margin-left: 10px;
        margin-top: 13px;
  .searchresult
    position :absolute
    top: 46px
    left:0
    bottom:0
    width:100%
    background: #ffffff
    z-index:10
    .list-ul
      li
        display:flex
        .img
          &.active
            color: #d33a31
          flex-basis:48px
          text-align :center
          line-height: 56px
          color:#999999
        .title
          flex :1
          border-1px(#ddd)
          .music-name
            &.active
              color: #d33a31
            line-height: 32px
            font-size: 18px
            color :#333
          p
            font-size: 16px
            color:#949494
            i
              display :inline-block
              width:16px
              height:16px
              background-image:url(../assets/images/5.png)
              background-position:center center
              background-size: 16px 16px
              background-repeat:no-repeat
              vertical-align:middle
            span
              &.active
                color: #d33a31
              vertical-align:middle
              font-size:12px
        .menu
          flex-basis:48px
          margin-top: 12px
          border-1px(#ddd)
          .menu-img
            width:36px
            height:26px
            background-position:center center
            background-size: 18px 18px
            background-repeat:no-repeat
            border:1px solid #d3d4da
            border-radius:4px
        .menu:nth-child(3)
          .menu-img
            background-image:url(../assets/images/5.png)
        .menu:nth-child(4)
          .menu-img
            background-image:url(../assets/images/5.png)
</style>
