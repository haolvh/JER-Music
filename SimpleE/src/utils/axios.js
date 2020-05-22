import axios from 'axios'

export function request(config) {
    const instance = axios.create({
        baseURL: 'http://192.168.3.86:8081',
        timeout: 5000
    })
    instance.interceptors.request.use(config => {
        return config
    },(err) => {
        return Promise.reject(err)
    })
    instance.interceptors.response.use(res => {
        return res
    })

    return instance(config)
}
/*拦截器（Interceptor）使用

interceptor 的执行顺序大致为：

请求到达 DispatcherServlet
DispatcherServlet 发送至 Interceptor ，执行 preHandle
请求达到 Controller
请求结束后，postHandle 执行*/
