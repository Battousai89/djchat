import { createRouter, createWebHistory } from "vue-router";
import MainLayout from "@/components/MainLayout.vue";

const routes = [
  {
    path: "/",
    name: "Main",
    component: MainLayout, // Основная страница с чатом
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
