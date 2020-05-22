import axios from 'axios'
import {HOST} from '../common/js/config'

export function getBanner () {
  const url = HOST + '/index'
  return axios.get(url)
}

export function getRecommendList () {
  const url = HOST + '/index'
  return axios.get(url)
}

export function getRecommendMusic () {
  const url = HOST + '/index'
  return axios.get(url)
}

export function getRecommendListDetail (id) {
  const url = HOST + `/index/slist`
  return axios.get(url)
}
