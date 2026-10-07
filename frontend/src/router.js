import { createRouter, createWebHistory } from "vue-router";

import FeedbackView from "./views/FeedbackView.vue";
import OverviewView from "./views/OverviewView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", redirect: "/tagasiside" },
    { path: "/tagasiside", component: FeedbackView },
    { path: "/ulevaade", component: OverviewView },
  ],
});

export default router;
