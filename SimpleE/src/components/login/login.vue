<template>
 <div>
   <div class="jumbotron" id="reg-top" >
    <div class="container" id="register">
      <p>Build a house of your imaginings ere you build a house within the city walls</p>
    </div>
  </div>


    <el-form :model="LoginForm"   ref="LoginForm" label-width="0px" class="ms-content">

      <el-form-item  prop="email" >
       <label >email</label>
        <el-input type="text" v-model="LoginForm.email"  class="emailform"  placeholder="邮箱"></el-input>
      </el-form-item>



      <el-form-item prop="password">
        <label >Password</label>
        <el-input  type="password" v-model="LoginForm.password" class="form" placeholder=" 密码"></el-input>
      </el-form-item>


    <el-button type="checkbox"  @click="submitForm" class="btn btn-default" >登录</el-button>
    <p></p>
    <br>
       <p>还没账号，马上去<span ><el-button @click="toregin" id="registerButton">注册</el-button></span></p>
  </el-form>

   <div>
<!--     <div style="padding:10px 0;">-->
<!--       <a-player :music="songList" :showlrc="3" :narrow="false" theme="#b7daff" mode="circulation" v-if="flag" listmaxheight='96px' ref="player"></a-player>-->
<!--     </div>-->

   </div>

   <i class="iconfont icon-shoucangxing shoucang" :class="{'active':isSelected}" @click="toggleCollect">收藏</i>

  </div>

</template>

<!--vue中使用通过ref来获取dom元素 ，如果在普通的 DOM 元素上使用，引用指向的就是 DOM 元素; -->
<!--如果用在子组件上，引用就指向组件实例-->
<!--当 v-for 用于元素或组件的时候，引用信息将是包含 DOM 节点或组件实例的数组-->

<script>
  import { Message } from 'element-ui';
  import {GetMusicInfo, UserLogin,GetRes} from '../../api/finalApi'
  import QS from 'qs'
  import state from '../../store/store'
  import actions from '../../store/store'
  import axios from 'axios'
  import VueAplayer from 'vue-aplayer'
  export default {
    name: "login",
    components:{
      'a-player': VueAplayer
    },
    data: function () {
      return {

        LoginForm: {
          email:'',
          username: '',
          password: '',

        },

        isSelected:false,

    };

    },

    methods: {
      submitForm() {
        GetRes().then(res=> {
          //将json文件中的数据赋值给data里面的deviceList
          console.log(res.data)
        })

        // let data = {
        //   email:this.LoginForm.email,
        //   username:this.LoginForm.username,
        //   password:this.LoginForm.password
        //
        // }
        //
        //  let _data=QS.stringify(data)
        // UserLogin(_data).then( res=>{
        //   // console.log(res);
        //
        //   if(res.data) {
        //     this.$message({
        //       type: 'success',
        //       message: '登录成功'
        //     })
        //     localStorage.setItem('user',data.username)
        //     localStorage.setItem('email',data.email)
        //
        //     this.$router.push('/userpage')
        //   }
        //
        // })

      },
      toggleCollect(){
        this.isSelected = !this.isSelected
      },


      toregin() {
        this.$router.push('/register')

      },
        async init () {
//这边是引入了axios然后使用的get请求的一个音乐列表接口

//这边url随大家更改了
          let musicid = '';
          let data = await getMusicInfo(musicId);
//以下就是这边对请求的一个处理，看接口了
          if(data && data.data.showapi_res_code==0){
            this.musicList = data.data.showapi_res_body.pagebean.songlist;

            for(let i=0;i<=this.musicList.length;i++){
              if(i<=9){
                let obj={};
//url=>歌曲地址 title=>头部 author=>歌手 pic=>写真图片 lrc=>歌词
//其中url必须有，其他的都是非必须
                obj.title = this.musicList[i].songname;
                obj.author = this.musicList[i].singername;
                obj.url = this.musicList[i].url;
                obj.pic = this.musicList[i].albumpic_small;
                obj.lrc = this.musicList[i].irl;
//把数据一个个push到songList数组中，在a-player标签中使用 :music="songList" 就OK了
                this.songList.push(obj);
              }
            }
//因为是异步请求，所以一开始播放器中是没有歌曲的，所有给了个v-if不然会插件默认会先生成播放器，导致报错(这个很重要)
            this.flag = true;
          };
        }
    },
//     async mounted () {
// //异步加载，先加载出player再使用
//       await this.init();
//       let aplayer = this.$refs.player.control;
//       aplayer.play();
//     },



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

</style>
