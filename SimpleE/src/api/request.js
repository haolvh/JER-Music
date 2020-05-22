import axios from 'axios'
import { Notification } from 'element-ui'

// 创建axios实例
const service = axios.create({
  baseURL: process.env.BASE_API,
  timeout: 50000 // 请求超时时间
})

// request拦截器
service.interceptors.request.use(
  config => {
    config.headers['Content-Type'] = 'text/plain' // 关键所在
    return config
  },
  error => {
    console.log(error) // for debug
    Promise.reject(error)
  }
)

// response 拦截器
service.interceptors.response.use(
  response => {
    const res = response.data
    if (res.resultCode !== '000') { // 后台返回码，根据自己的业务进行修改
      Notification.error({
        title: '错误',
        message: res.resultDesc, // 错误描述信息
        duration: 0
      })
      return Promise.reject('error')
    } else {
      return response.data
    }
  },
  error => {
    console.log('err' + error) // for debug
    Notification.error({
      title: '错误',
      message: error,
      duration: 0
    })
    return Promise.reject(error)
  }
)

export default service
