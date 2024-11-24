<template>
  <div class="sidebar">
    <div class="server-list">
      <div v-for="server in servers" :key="server.id" class="server">
        <img :src="server.icon" :alt="server.name" class="server-icon" />
      </div>
    </div>
    <div class="channel-list">
      <h3>CHANNELS</h3>
      <ul>
        <li v-for="channel in channels" :key="channel.id">
          <span>#</span>{{ channel.name }}
        </li>
      </ul>
    </div>
    <div class="friend-list">
      <h3>FRIENDS</h3>
      <ul>
        <li v-for="friend in friends" :key="friend.id">
          <img :src="friend.avatar" alt="Avatar" class="friend-avatar" />
          <span>{{ friend.name }}</span>
          <span :class="['status-dot', friend.status]"></span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "AppSidebar",
  data() {
    return {
      servers: [
        { id: 1, name: "Server 1", icon: "/path/to/icon1.png" },
        { id: 2, name: "Server 2", icon: "/path/to/icon2.png" },
        { id: 3, name: "Server 3", icon: "/path/to/icon3.png" },
      ],
      channels: [
        { id: 1, name: "All threads" },
        { id: 2, name: "general" },
        { id: 3, name: "support" },
      ],
      friends: [
        { id: 1, name: "Orlando Diggs", avatar: "/path/to/avatar1.jpg", status: "online" },
        { id: 2, name: "Carmen Velasco", avatar: "/path/to/avatar2.jpg", status: "offline" },
      ],
    };
  },
};
</script>

<style scoped>
.sidebar {
  display: flex;
  flex-direction: column;
  background-color: #2f3136;
  width: 300px;
  padding: 10px;
  color: white;
}

.server-list {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.server {
  margin: 10px 0;
}

.server-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  cursor: pointer;
  transition: 0.3s;
}

.server-icon:hover {
  border: 2px solid #7289da;
}

.channel-list,
.friend-list {
  margin-top: 20px;
}

.friend-avatar {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-right: 10px;
}

.status-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin-left: 10px;
}

.status-dot.online {
  background-color: green;
}

.status-dot.offline {
  background-color: red;
}
</style>
