import Vue from 'vue';
import Router from 'vue-router';
import Ping from './components/Ping.vue';
import Tasks from './components/Tasks.vue';

Vue.use(Router);

export default new Router({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: [
        {
            path: '/',
            name: 'Tasks',
            component: Tasks,
        },
        {
            path: '/ping',
            name: 'Ping',
            component: Ping,
        }
    ],
});