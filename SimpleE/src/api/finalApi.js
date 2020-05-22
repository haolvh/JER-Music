import axios from'axios'
import base from "./base";
//administer login
export const AdminLogin=params=>{
  return axios.post(`${base}/admin/login`,{params:params})
}

export const UserLogin = params => {
  // console.log("params" + params)
  return axios.post(`${base}/userlogin`, params)
}


export const UserRegister = params => {
  console.log("params" + params)
  return axios.post(`${base}/register`, params)
}

export const postBookList = params => {
  console.log("params" + params)
  return axios.post(`${base}/postBooklist`, params)
}

export const returnPost = params => {
  return axios.post(`${base}/returnbook`, params)
}

export const GetBooksInfo = params => {
  return axios.post(`${base}/listBook`, params)
}
export const GetMusicInfo=params=>{
  return axios.post(`${base}/music`,params)}

export const GetRes= params => {
  return axios.get(`${base}/api/show_books`, {params: params})
}
export const GetMusic = params =>{
  return axios.get(`${base}/api/get_music`, {params: params})
}
export const FirstMusic = params =>{
  return axios.get(`${base}/api/firstPage`, {params: params})
}








