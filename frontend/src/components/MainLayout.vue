/* eslint-disable */
<template>
  <div class="main-layout">
    <!-- Боковая панель -->
    <AppSidebar />

    <!-- Основная область: окно чата -->
    <ChatWindow />

    <!-- Боковая панель профиля -->
    <ProfileSidebar />
  </div>
</template>

<script>
import AppSidebar from "./AppSidebar.vue";
import ChatWindow from "./ChatWindow.vue";
import ProfileSidebar from "./ProfileSidebar.vue";

export default {
  name: "MainLayout",
  components: {
    AppSidebar,
    ChatWindow,
    ProfileSidebar,
  },
};
</script>

<style scoped>
.main-layout {
  display: flex;
  height: 100vh;
  overflow: hidden;
}
</style>
