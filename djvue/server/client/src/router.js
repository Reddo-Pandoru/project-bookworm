import Vue from 'vue';
import Router from 'vue-router';


Vue.use(Router);

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import( './views/Home.vue')
        },
        {
            path: '/managebooks',
            name: 'manageBooks',
            component: () => import( './views/manage-books.vue')
        },
        {
            path: '/manageusers',
            name: 'manageUsers',
            component: () => import( './components/login.vue')
        },
        {
            path: '/lista',
            name: 'lista',
            component: () => import( './views/lista-book.vue')
        },
        {
            path: '/user-loans',
            name: 'user-loans',
            component: () => import( './views/user-loans.vue')
        },
        {
            path: '/books/:isbn',
            name: 'detail',
            component: () => import( './views/bookDetail.vue'),
            props: true
        },
        {
            path: '*',
            component: () => import( './views/page-not-found.vue')

        }
    ]
});