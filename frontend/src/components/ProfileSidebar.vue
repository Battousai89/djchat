<template>
    <div class="profile">
      <img :src="user.avatar" alt="User avatar" class="profile-avatar" />
      <h2>{{ user.name }}</h2>
      <p>{{ user.role }}</p>
      <div class="social-links">
        <a v-for="link in user.socialLinks" :key="link.name" :href="link.url">
          {{ link.name }}
        </a>
      </div>
      <button class="message-button">Message</button>
      <div class="profile-details">
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <p><strong>Timezone:</strong> {{ user.timezone }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ProfileSidebar",
    data() {
      return {
        user: {
          avatar: "/path/to/avatar.jpg",
          name: "Amilia Luna",
          role: "UI Designer",
          socialLinks: [
            { name: "Twitter", url: "#" },
            { name: "LinkedIn", url: "#" },
          ],
          username: "@amilia_lu",
          email: "a-luna@gmail.com",
          timezone: "2:21 PM Local time",
        },
      };
    },
  };
  </script>
  
  <style scoped>
  .profile {
    text-align: center;
    background-color: #2f3136;
    color: white;
    padding: 20px;
  }
  
  .profile-avatar {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-bottom: 10px;
  }
  
  .message-button {
    background-color: #7289da;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  .message-button:hover {
    background-color: #5b6eae;
  }
  </style>
  