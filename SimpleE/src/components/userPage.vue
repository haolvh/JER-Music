<template>


  <el-button-group>
    <el-button   id="find" type="primary" @click="toFind">借阅</el-button>
    <br>
    <p></p>
    <el-button id="borrow" type="primary" @click="toBorrow">查找</el-button>
    <br>
    <p></p>
    <p></p>
    <p></p>
    <el-button id="return" type="primary" @click="toReturn">还书</el-button>
  </el-button-group>

</template>

<script>
  export default {
    name: "userPage",
    methods:{
      toFind(){
        this.$router.push('/lookbook')
      },
      toBorrow()
      {
        this.$router.push('/searchbook')
      },
      toReturn()
      {
        this.$router.push('/myRecord')
      }
    }
  }
</script>

<style scoped>
  #find
  {
    margin-top:50%;
    background-color:#66b1ff;
  }
  #borrow{
    margin-top:40%;
    background-color: #31708f;
  }
  #return{
    margin-top:40%;
  }

</style>
