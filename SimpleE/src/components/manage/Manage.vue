<template>
  <section class="box">
    <div class="head">
      <h3>{{this.$route.name}}</h3>
    </div>
    <div class="main">
      <h4>用户列表</h4>
      <el-table
        :data="CurUsers"
        style="width: 100%">
        <el-table-column
          prop="date"
          label="注册时间"
          min-width="10%">
        </el-table-column>
        <el-table-column
          prop="name"
          label="用户名"
          min-width="10%">
        </el-table-column>

        <el-table-column
          prop="email"
          label="邮箱"
          min-width="15%">
        </el-table-column>
        <el-table-column
          prop="tel"
          label="电话"
          min-width="15%">
        </el-table-column>
        <el-table-column
          prop="sendnum"
          min-width="20%"
          label="发货量">
        </el-table-column>
        <el-table-column label="操作" width="130" align="center">
          <template slot-scope="scope">
            <el-button type="text" icon="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            <el-button type="text" icon="el-icon-delete" class="red" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
          </template>
        </el-table-column>

      </el-table>
    </div>
  </section>
</template>
<script>
  import {GetUsers} from '../../api/admin'
  export default {
    // ..
    data () {
      return {
        users: [],
        CurUsers: []
      }
    },
    methods: {
      handleDelete(index,CurUsers)
      {
        bookInfo.splice(index,1)
      },
      // 获取所有用户
      AllUsers () {
        GetUsers({type: 'all'}).then(res => {
          // console.log(res)
          this.users = res.data.users
        }).then(usersendnumm => {
          // 获取用户的发货量
          if (this.users.length !== 0) {
            let names = []
            for (let i = 0; i < this.users.length; i++) {
              names.push(this.users[i].name)
            }
            // console.log(names)
            UserSendNum({names: names}).then(res => {
              // console.log(res)
              for (let i = 0; i < this.users.length; i++) {
                this.users[i].sendnum = res.data.nums[i]
              }
              // console.log(this.users)
              this.CurUsers = this.users
            })
          }
        })
      }
    },
    mounted () {
      this.AllUsers()
    }
  }
</script>
<style lang="less" scoped>
  @import '../../../common/index';
  .box {
    .head {
      .leftborder;
    }
    .main {
      .learncontent;
      .el-table {
        .avatar {
          width: 60px;
          height: 60px;
          border-radius: 30px;
        }
      }
    }
  }
</style>
