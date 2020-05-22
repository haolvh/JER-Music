<template>
    <div id="marTop" >
        <el-table
          :data="bookInfo"
          style="width: 100%"
          @cell-click="cellClick">

          <el-table-column type="index">
          </el-table-column>

          <el-table-column
            prop="book_name"
            label="书名"
            width="180">
          </el-table-column>

          <el-table-column
            prop="house_name"
            label="作者"
            width="180">
          </el-table-column>

          <el-table-column
            prop="house_telephone"
            label="出版社">
          </el-table-column>

          <el-table-column
            prop="book_score"
            label="简介"   @click="dialogVisible = true">
          </el-table-column>


          <el-table-column label="操作" width="180" align=center>
            <template slot-scope="scope">
              <el-button @click="addToBasket(scope.row)" type="primary" icon="el-icon-plus" circle></el-button>
            </template>
          </el-table-column>

        </el-table>

      <el-button type="checkbox" class="btn btn-default">确认</el-button>


      <div v-if="this.shopCar.length>0">
        <h3>所选书籍</h3>
        <el-table :data="shopCar" stripe style="width:100%">
          <el-table-column prop="book_name" label="名字" width="180" align=center></el-table-column>

          <!--          <el-table-column label="操作" width="180" align=center>-->
<!--            <template scope="scope">-->
<!--              <el-button type="warning" @click="subQuantity(scope)" icon="el-icon-minus" circle size="mini"></el-button>-->
<!--              <span>{{scope.row.}}</span>-->
<!--            </template>-->
<!--          </el-table-column>-->

                    <el-table-column label="操作" align="right">
                      <template slot-scope="scope">
                        <el-button size="mini" type="danger" icon="el-icon-delete" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
                      </template>
                    </el-table-column>

        </el-table>



        <el-button-group>
          <el-button type="success" @click="submitBookList">提交</el-button>
        </el-button-group>

      </div>



      <el-dialog
        title="简介"
        :visible.sync="dialogVisible"
        width="30%">
        <span>{{book_introduction}}</span>
        <span slot="footer" class="dialog-footer">
              <el-button @click="dialogVisible = false ">取 消</el-button>
        </span>
      </el-dialog>

      <el-dialog title="确定清空？" :visible.sync="basketdialogVisible" width="30%" :before-close="handleClose">
        <span align=center>即将清空</span>
        <span slot="footer" class="dialog-footer">
	    				<el-button @click="basketdialogVisible = false">取 消</el-button>
	    				<el-button type="danger" @click="emptyBaskets">确 定</el-button>
  					</span>
      </el-dialog>

  </div>
  </template>





<script>
import {GetBooksInfo,postBookList} from "../api/finalApi";
import QS from 'qs'
export default {
  data() {
    return {
      bookInfo: [],
      book_introduction: '',
      dialogVisible: false,
      basketdialogVisible: false,
      baskets: [],
      shopCar: [],
      isable: "false"

    }
  },
  created() {
    let self = this;
    GetBooksInfo().then(res => {
      let bookInfo = res.data.bookInfo;
      console.log(res)
      self.bookInfo = bookInfo;
    }).catch(err => {
      console.log(err)
    })
  },
  methods: {
    //添加到购物车带参数book
    // row赋值会赋完  即使不可见
    addToBasket(sRow) {
      let oneBook = {
        book_name: sRow.book_name
      }
      this.shopCar.push(oneBook)
      localStorage.setItem('bookRecord', JSON.stringify(this.shopCar))
      let bookRecord = localStorage.getItem('bookRecord')
    },
    // let basket = {
    //   bookName: sRow.name,
    //   quantity:1
    //
    // }
    // if(this.baskets.length>0){
    //   let result =this.baskets.filter((basket) => {
    //     return basket.bookName === sRow.bookName
    //   })
    //   if(result != null && result.length>0){
    //     result[0].quantity ++
    //   }else{
    //     this.baskets.push(basket)
    //   //   }
    //   // }else{
    //   //   this.baskets.push(basket)
    //   // }
    //   // this.basketdialogVisible = false //不加这一行的时候 清空购物车后再添加会出来模态框，原因未知
    // },
    // subQuantity(scope){
    //   scope.row.quantity --;
    //   if(scope.row.quantity<=0){
    //     this.baskets.splice(this.baskets.indexOf(scope.row),1)
    //   }
    subBasket(sRow) {
      let aBook = {
        book_name: sRow.book_name
      }
      this.shopCar.pop()
      this.btnBoolean = false

    },
    handleDelete(index, row) {
      // console.log(this.record)
      let aBook = {
        book_name: row.book_name
      }
      this.shopCar.splice(index, 1);
      // console.log(that)
      // console.log(this.record)
    },

    handleClose() {
      this.dialogVisible = false
    },
    emptyBaskets() {
      this.baskets = []
    },
    cellClick(row, column, cell, event) {
      if (column.label == "简介") {
        this.dialogVisible = true;
        this.book_introduction = row.book_introduction;
      }
    },

    submitBookList() {
      let email = localStorage.getItem('email')

      let data = {
        email: email,
        shopCar: this.shopCar
      }
      // let _data=QS.stringify(data)
    console.log(data)
      postBookList(data).then(res => {
        this.$message({
          type: 'success',
          message: '借阅成功'
        })

      }).catch(err => {
        console.log(err)
      })
      this.$router.push('/userpage')
    }
  }
}
      // let username=JSON.parse(user)
      // let data = {
      //   userName:username.username,
      //   totalBook:this.shopCar
      // }
      // console.log(data)
      // postBookList(data).then(res => {
      //   // console.log(res)
      // })





    // handleEdit(index, row) {
    //   let  that=this
    //   let user = sessionStorage.getItem('user')
    //   let data = {
    //
    //     user: JSON.parse(user),
    //     bookName:this.row.bookName
    //
    //   }


    //     this.res.data[index] = {bookName: 'meile', press: 'meile', pressTele: 'meile', comment: 'meili'};
    //     console.log()
    //     this.getInfo();
    //   }







        //   handleEdit(index, row)
        //   {
        //     console.log(index);
        //     this.res.data[index] = {bookName: 'meile', press: 'meile', pressTele: 'meile', comment: 'meili'};
        //     console.log()
        //     this.getInfo();
        //   }


      // getInfo()
      // {
      //   this.bookInfo = []
      //   let self = this;
      //   this.res.data.forEach(item => {
      //     self.bookInfo.push(item)
      //   })
        // GetBooksInfo().then(res => {
        //   console.log('habo')
        //   console.log("hello"+res.data)
        //
        //   this.bookInfo=res.data
        //   this.bookName = res.data.bookName
        //   this.press = res.data.press;
        //   this.pressTele = res.data.pressTele
        //   this.comment = res.data.comment
        // })
      // }
    // ,
    //   handleEdit(index, row)
    //   {
    //     console.log(index);
    //     this.res.data[index] = {bookName: 'meile', press: 'meile', pressTele: 'meile', comment: 'meili'};
    //     console.log()
    //     this.getInfo();
    //   }
    // ,

    // }



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

