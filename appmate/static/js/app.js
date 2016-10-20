import Vue from 'vue'
import VueResource from 'vue-resource'
import VueRouter from 'vue-router'

import App from './vue/App.vue'
import Detail from './vue/Detail.vue'
import List from './vue/List.vue'
import TxDetail from './vue/TxDetail.vue'

Vue.use(VueResource)
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: List,
    name: 'index'
  },
  {
    path: '/detail/tx/:txId',
    component: TxDetail,
    name: 'txDetail',
  },
  {
    path: '/detail/:blockId',
    component: Detail,
    name: 'detail',
  },
]

const router = new VueRouter({
  routes
})

const app = new Vue({
  el: 'body',
  render: h => h(App),
  router,
})
