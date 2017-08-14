import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/Login'
import Message from '@/components/Message'

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
  ]
})
