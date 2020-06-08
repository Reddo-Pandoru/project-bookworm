import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue'
import PageNotFound from './views/page-not-found.vue'

Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/managebooks',
            name: 'manageBooks',
            component: () => import( './views/manage-books.vue')
        },
        {
            path: '/loanbook',
            name: 'loanBook',
            component: () => import( './views/loan-book.vue')
        },
        {
            path: '/returnbook',
            name: 'returnBook',
            component: () => import( './views/return-book.vue')
        },
        {
            path: '/createbook',
            name: 'createbook',
            component: () => import( './views/create-book.vue')
        },
        {
            path: '/createuser',
            name: 'createuser',
            component: () => import( './views/create-user.vue')
        },
        {
            path: '/manageusers',
            name: 'manageUsers',
            component: () => import( './views/manage-users.vue')
        },
        {
            path: '*',
            component: PageNotFound

        }
    ]
});