<template>
  <div>
    <div v-show="showFlag" class="musicmenu-wrapper" key="musicmenu">
      <div>
        <div class="back">
          <img src="../assets/images/5.png" alt="" width=24 height=24>
        </div>
        <div class="title-name">
          歌单
        </div>

          <img src="../assets/images/sun.png" alt="" width=24 height=24>
        </div>
      </div>
      <div ref="menuWrapper" class="list-wrapper">
        <div>
          <header>
            <div class="menu-user">
              <div class="user-img" >
                <img :src="coverImgUrl" alt="" width="100%">
              </div>
              <div class="user-info">
            <span>
             {{name}}
            </span>
                <div class="user-name">
                  <img src="../assets/images/9.jpg" alt="">
                </div>
              </div>
            </div>
            <div class="menu-info">
              <ul class="info-ul">
                <li>
                  <div class="info-img"></div>
                  <p>14633</p>
                </li>
                <li>
                  <div class="info-img"></div>
                  <p>434</p>
                </li>
                <li>
                  <div class="info-img"></div>
                  <p>80</p>
                </li>
                <li>
                  <div class="info-img"></div>
                  <p>下载</p>
                </li>
              </ul>
            </div>

          </header>
      </div>
      </div>
    </div>

</template>

<script type="text/ecmascript-6">
  import BScroll from 'better-scroll';
  import {FirstMusic} from '../api/finalApi'
  export default {
    name: 'anotherFirst',
    data() {
      return {
        showFlag: false,
        musiclist: {},
        number: -1,
        coverImgUrl: '',
        name: '',
        description: '',
        id: '',
        creator: '',
        trackCount: 0,
        opacity: 0
      };
    },
    methods: {}
  }
</script>

<style lang="stylus" rel="stylesheet/stylus">
  .musicmenu-wrapper
    position:absolute
    top:0
    left:0
    width:100%
    height:100%
    background: #ffffff
    z-index:100
    &.fade-enter-active, &.fade-leave-active
      transition: all 0.2s linear
      transform translate3d(0, 0, 0)
    &.fade-enter, &.fade-leave-active
      opacity: 0
      transform translate3d(100%, 0, 0)
    .menu-title
      position:fixed
      width:100%
      top:0
      display :flex
      z-index: 110
      .back
        flex-basis:40px
        display :inline-block
        img
          margin-top:12px
          margin-left: 12px
      .title-name
        flex :1
        display :inline-block
        height 48px
        line-height:48px
        text-align center
        font-size:18px
        color:#fff
      .setting
        flex-basis:40px
        display :inline-block
        img
          margin-top:12px
    .list-wrapper
      position:absolute
      top:0
      left:0
      width:100%
      height:100%
      overflow :hidden
      header
        position relative
        color: #fff
        padding-top:48px
        overflow hidden
        background: rgba(7, 17, 27, 0.5)
        .menu-user
          margin:16px 20px 0 20px
          display:flex
          .user-img
            flex-basis:150px
          .user-info
            padding-left:10px
            padding-right:20px
            flex:1
            span
              display:block
              margin-top: 20px
              letter-spacing: 1px
              line-height :1.3
            .user-name
              p
                display:inline-block
                vertical-align:top
                line-height:30px
                height: 30px
                font-size:18px
              img
                vertical-align:top
                height:24px
                margin-top 3px
        .menu-info
          .info-ul
            margin-bottom:8px
            display:flex
            li
              flex:1
              .info-img
                height:48px
                background-size:24px 24px
                background-repeat:no-repeat
                background-position:center center
              p
                text-align:center
                line-height: 20px
                font-size:14px
                color:#c2bebc
            li:nth-child(1)
              .info-img
                background-image:url('../assets/images/5.png')
            li:nth-child(2)
              .info-img
                background-image:url('../assets/images/3.png')
            li:nth-child(3)
              .info-img
                background-image:url('../assets/images/14.jpeg')
            li:nth-child(4)
              .info-img
                background-image:url('../assets/images/1.jpg')
        .background
          position absolute
          top: 0
          left 0
          width 100%
          height 100%
          z-index -1
          filter blur(10px)
      .menu-list
        background:#fbfcfd
        .list-title
          display:flex
          .img
            flex-basis:48px
            height:48px
            background:url(../assets/images/3.jpeg) no-repeat
            background-position:center center
            background-size: 24px 24px
          .title
            flex :1
            line-height:48px
            font-size: 18px
            border-1px(#ddd)
            span
              font-size:14px
              color:#949494
          .menu
            flex-basis:48px
            height:48px
            background:url(../assets/images/2.png) no-repeat
            background-position:center center
            background-size: 24px 24px
            border-1px(#ddd)
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
                  background-image:url(../assets/images/3.jpeg)
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
                background-image:url(../assets/images/4.png)
            .menu:nth-child(4)
              .menu-img
                background-image:url(../assets/images/6.jpeg)
</style>
