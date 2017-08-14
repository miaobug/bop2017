import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Message from '@/components/Message'
import Map from '@/components/Map'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Login',
      component: Login
    },
    {
      path: '/message/:id',
      name: 'Message',
      component: Message
    },
    {
      path: '/map/:id/:from/:to',
      name: 'Map',
      component: Map
    },
  ]
})
