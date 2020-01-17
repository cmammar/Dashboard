import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/routes/Login'
import Register from '@/components/routes/Register'
import Dashboard from '@/components/routes/Dashboard'
import AddWidget from '@/components/routes/AddWidget'
import ManageWidgets from '@/components/routes/ManageWidgets'
import Account from '@/components/routes/Account'
import Admin from '@/components/routes/Admin'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Dashboard',
      component: Dashboard,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next() : next({name: 'Login'})
      }
    },
    {
      path: '/Login',
      name: 'Login',
      component: Login,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next({name: 'Dashboard'}) : next()
      }
    },
    {
      path: '/Register',
      name: 'Register',
      component: Register,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next({name: 'Dashboard'}) : next()
      }
    },
    {
      path: '/Account',
      name: 'Account',
      component: Account,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next() : next({name: 'Login'})
      }
    },
    {
      path: '/AddWidget',
      name: 'AddWidget',
      component: AddWidget,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next() : next({name: 'Login'})
      }
    },
    {
      path: '/ManageWidgets',
      name: 'ManageWidgets',
      component: ManageWidgets,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next() : next({name: 'Login'})
      }
    },
    {
      path: '/Admin',
      name: 'Admin',
      component: Admin,
      beforeEnter: (to, from, next) => {
        localStorage.access_token ? next() : next({name: 'Login'})
      }
    },
  ]
})