import base from './base'
// import axios from '../utils/getData'

const login = function (params) {
  return axios.post(`${base.sq}/login`, params)
}

export default login
