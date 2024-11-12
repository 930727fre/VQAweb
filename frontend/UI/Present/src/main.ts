import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import App from "./App.vue";

import TapPic from "./pages/TapPic.vue";
import TapQuest from "./pages/TapQuest.vue";
import Result from "./pages/Result.vue";
import Normal from "./pages/Normal.vue";
import "./global.css";

interface Route {
  path: string;
  name: string;
  component: any;
}

const routes: Route[] = [
  {
    path: "/",
    name: "TapPic",
    component: TapPic,
  },
  {
    path: "/tap-quest",
    name: "TapQuest",
    component: TapQuest,
  },
  {
    path: "/result",
    name: "Result",
    component: Result,
  },
  {
    path: "/normal",
    name: "Normal",
    component: Normal,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((toRoute, _, next) => {
  const metaTitle = toRoute?.meta?.title as string;
  const metaDesc = toRoute?.meta?.description as string;

  window.document.title = metaTitle || "Present";
  if (metaDesc) {
    addMetaTag(metaDesc);
  }
  next();
});

const addMetaTag = (value: string) => {
  const element = document.querySelector(`meta[name='description']`);
  if (element) {
    element.setAttribute("content", value);
  }
};

createApp(App).use(router).mount("#app");

export default router;
