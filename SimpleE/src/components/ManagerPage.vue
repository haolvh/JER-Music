<template>
  <div id="marTop" >

    <el-table

      style="width: 100%">

      <el-table-column label="用户">
        <template slot-scope="scope">
          <el-button type="text" style="display: block" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">展开</el-button>
        </template>
      </el-table-column>


      <el-table-column label="图书">
        <template slot-scope="scope">
          <el-button type="text" style="display: block" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">展开</el-button>
        </template>
      </el-table-column>


    </el-table>
  </div>
</template>

<script>
  import {GetBooksInfo} from "../api/finalApi";

  export default {
    name: "ManagePage",
    data() {
      return {
        bookInfo: [{
          bookName: 'ajishdi',
          bookNum
        }]

      }
    },
    mounted()
    {
      this.changestyle()
    },

    methods:{
      changestyle(){
        var col1=document.getElementsByName("el-table_1_column_1");
        col1.style.Width="5%"
      },


      getInfo() {

        GetBooksInfo().then(res => {
          console.log('habo')
          console.log("hello"+res.data)
          this.bookInfo=res.data
          this.bookName = res.data.bookName
          this.press = res.data.press;
          this.pressTele = res.data.pressTele
          this.comment = res.data.comment
        })
      }
    }


  }
</script>

<style scoped>
  #marTop
  {
    margin-top:10%
  }
  #miniColumn{
    width:51%;
  }
</style>

