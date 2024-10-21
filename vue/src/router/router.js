import { createRouter, createWebHistory } from 'vue-router';
import App from '../app.vue';
import Signup from '../signup.vue';
import Signin from '../signin.vue';

const routes = [
  { path: '/', component: App },
  { path: '/signup', component: Signup },
  { path: '/signin', component: Signin },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
