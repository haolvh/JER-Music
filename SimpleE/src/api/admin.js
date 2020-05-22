import axios from 'axios'
import {request} from "../utils/axios";
import qs from 'qs'
let base='/api'

// 后台登录接口
export const AdminLogin=params=>{
  return axios.get('${base}/admin/login',{params:params})
}

// 判断管理员是否被注册
export const hasReginedAdminer = params => {
  return axios.get(`${base}/admin/hasregined`, {params: params})
}
// 添加管理员接口
export const NewAdminer = params => {
  return axios.post(`${base}/admin/newadminer`, params)
}

// 获取管理员
export const GetAdminer = params => {
  return axios.get(`${base}/admin/getadminer`, {params: params})
}
// 修改管理员
export const EditAdminer = params => {
  return axios.post(`${base}/admin/editadminer`, params)
}


// 获取图书分类
export const GetProducts = params => {
  return axios.get(`${base}/admin/getproducts`, {params: params})
}

// 添加一本书
export const NewProd = params => {
  return axios.post(`${base}/admin/newprod`, params)
}

// 获取书
export const GetProds = params => {
  return axios.get(`${base}/admin/getprods`, {params: params})
}

// 修改书
export const EditProd = params => {
  return axios.post(`${base}/admin/editprod`, params)
}




// 获取用户
// export const GetUsers = params => {
//   return axios.get(`${base}/admin/getusers`, {params: params})
// }
export function GetUsers() {

  return request(params,{
    method:'get',
    url:'/admin/getusers',

  })

}




// 用户注册
export function register(msg) {
  return request({
    method: 'post',
    url: '/user/register',
    data: msg
  })
}

// 用户登录
export function login(msg) {
  return request({
    method: 'post',
    url: '/user/login',
    data: qs.stringfy(data)
  })
}

// // 用户更新信息
// export function update(msg) {
//     return request({
//         method: 'post',
//         url: '/user/update',
//         data: msg
//     })
// }

export function getMsg() {
  return request({
    method: 'get',
    url: '/user/test'
  })
}




/*// 创建网站设置
export const NewOption = params => {
  return axios.post(`${base}/admin/siteoption`, params)
}
// 获取网站设置
export const GetOption = params => {
  return axios.get(`${base}/admin/siteoption`, {params: params})
}
// 更新网站基本设置
export const SiteOption = params => {
  return axios.put(`${base}/admin/siteoption`, params)
}*/



