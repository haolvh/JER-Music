<template>
  <div>

<span id="chineseName">用户名:</span>

    <el-tag
      id="uName"
   color="lavender">
      cyq
    </el-tag>

    <el-table :data="record">
      <el-table-column
        prop="book_name"
      label="已借书"
      width="180">
    </el-table-column>

      <el-table-column label="操作">-->
        <template slot-scope="scope">
          <el-button size="mini" type="danger" icon="el-icon-delete" @click="handleDelete(scope.$index, scope.row)">还书
          </el-button>
        </template>
      </el-table-column>


    </el-table>
    <el-button type="success" @click="handleSubmit">确认还书</el-button>


  </div>
</template>

<script>
  import {returnPost} from "../api/finalApi";

  export default {

    data() {


      let user = localStorage.getItem('user')
      let email=localStorage.getItem('email')
      let bookRecord = localStorage.getItem('bookRecord')
      let bf = JSON.parse(bookRecord)
      return {
        userName: user,
        record: bf,
        returnBook:[]
      }
    },
    methods:
        {

          handleDelete(index, row) {
            this.record.splice(index, 1);
            let that =row
            this.returnBook.push(that)

            console.log(this.returnBook)


            // console.log(that)
            // console.log(this.record)
          },
          handleSubmit() {
            let returnData = {
              // user: localStorage.getItem('user'),
              email:localStorage.getItem('email'),
              returnBook: this.returnBook
            }
            console.log(this.returnBook)
            // console.log(returnData)
            returnPost(returnData).then(res => {
              this.$message({
                type: 'success',
                message: '还书成功'
              })


            }).catch(err => {
              console.log(err)
            })
            this.$router.push('/userpage')
          }
        }
  }



</script>

<style scoped>
  #toTop{
    margin-top:10%;
    font-size: 20px;
  }
  #uName{
    margin-top:10%
  }
  #chineseName{
    margin-top:10%;
    font-size:20px;
    color: #31708f;
  }
  #but{
    margin-top: 20%;
  }

</style>
