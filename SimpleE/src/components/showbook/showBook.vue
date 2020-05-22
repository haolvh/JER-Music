
<template>
  <div class="section">
    <!-- 所有商品 -->
    <div class="allprod">
      <h4>所有书籍</h4>
      <el-table
        :data="prods"
        style="width: 100%">
        <el-table-column
          prop="name"
          label="商品名"
          min-width="40%">
        </el-table-column>
        <el-table-column
          prop="booknum"
          label="总量"
          min-width="10%">
        </el-table-column>
        <el-table-column
          prop="price"
          label="评价"
          min-width="10%">
        </el-table-column>

        <el-table-column
          min-width="20%"
          label="操作">
          <template slot-scope="scope">
            <el-button
              type="danger"
              @click="EditProd(scope.$index, scope.row)">编辑商品</el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
    <!-- 编辑商品 -->
    <el-dialog title="编辑商品" :visible.sync="dialogFormVisible" width="90%">
      <el-form ref="editprod" :rules="prodrules" :model="editprod">
        <el-form-item label="商品名" prop="name">
          <el-input v-model="editprod.name" placeholder="请输入商品名"></el-input>
        </el-form-item>
        <el-form-item label="书本评价" prop="info">
          <!-- <mavon-editor  ref="md" @imgAdd="$imgAdd" @imgDel="$imgDel" v-model="editprod.info"></mavon-editor> -->
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="exitEdit">取 消</el-button>
        <el-button type="primary" @click="submitEdit">确 定</el-button>
      </div>
    </el-dialog>
  </div>

</template>
<script>
  import {getAllLocalProds, editLocalProd} from '../../api/newapi'
  export default {
  // <el-table-column
  // prop="bookName"
  // label="书名"
  // width="180">
  //     </el-table-column>
  //     <el-table-column
  // prop="press"
  // label="出版社">
  //     </el-table-column>
  //     <el-table-column
  // prop="pressTele"
  // label="出版社电话">
  //     </el-table-column>
  //     <el-table-column
  // prop="comment"
  // label="评分">
  //     </el-table-column>
  //     <el-table-column label="操作" align="left">
  //     <template slot-scope="scope">
  //     <el-button  type="success" icon="el-icon-check"  @click="handleEdit(scope.$index, scope.row)">添加</el-button>
  //     <el-button type="danger" icon="el-icon-delete" style="color: #2c3e50" @click.native.prevent="handleDelete(scope.$index, scope.row)">删除</el-button>
  //     </template>
  //     </el-table-column>
  //     </el-table>

  // ..
    data () {
      return {
        prodName: '',
        prods: [],
        dialogFormVisible: false,
        imageUrl: '',
        editprod: {
          name: '',
          price: '',
          desc: '',
          info: ''
        },
        prodrules: {
          name: [
            {
              required: true,
              trigger: 'blur'
            },
            {
              min: 3,
              max: 15,
              message: '长度在 3 到 15 个字',
              trigger: 'blur'
            }
          ],

          desc: [
            {
              required: true,
              message: '请输入商品简介',
              trigger: 'blur'
            }
          ]
        }
      }
    },
    methods: {
      // 获取所有商品
      getallprods () {
        getAllLocalProds().then(res => {
          console.log(res)
          this.prods = res.data
        })
      },
      // 编辑商品
      EditProd (row, rowIndex) {
        this.editprod = rowIndex
        this.dialogFormVisible = true
        // console.log(this.imageUrl)
      },
      // 退出编辑商品
      exitEdit () {
        this.dialogFormVisible = false
      },
      // 确认修改并提交
      submitEdit () {
        this.$refs.editprod.validate(valid => {
          if (valid) {
            const updatedParams = {
              id: this.editprod._id,
              name: this.editprod.name,
              info: this.$refs.mdedit.mdinfo
            }
            // console.log(updatedParams)
            editLocalProd(updatedParams).then(res => {
              this.$notify({
                title: '商品修改成功',
                message: res.data.name,
                type: 'success',
                offset: 100
              })
              this.dialogFormVisible = false
              this.getallprods()
            })
          } else {
            this.$message({
              type: 'danger',
              message: '请验证后再提交修改'
            })
          }
        })
      }
    },
    mounted () {
      this.getallprods()
    }
  }
</script>
<style lang="less" scoped>
  @import url("//unpkg.com/element-ui@2.13.0/lib/theme-chalk/index.css");
  @import '../../../common/index';
  .section {
    .serchprod {
      .learncontent;
      .serch-input {
        width: 70%;
      }
      .serch-btn {
        width: 29%;
      }
    }
    .allprod {
      .learncontent;
      .table-image {
        width: 60px;
        height: 60px;
        border-radius: 30px;
      }
    }
    .el-form {
      text-align: left;
      .el-select {
        width: 100%;
      }
      .el-switch {
        margin: 10px 0 0 0;
      }
      .prod-image {
        width: 200px;
        height: 200px;
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
        .cur-image {
          width: 100%;
        }
        .prod-uploader-icon {
          font-size: 45px;
          color: #8c939d;
          width: 200px;
          height: 200px;
          line-height: 200px;
          text-align: center;
        }
      }
    }
  }
</style>
