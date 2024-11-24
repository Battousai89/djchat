/* eslint-disable */
<template>
    <div class="chat-window">

      <ChatHeader />
      
      <div class="chat-messages">
        <div
          v-for="message in messages"
          :key="message.id"
          class="chat-message"
          :class="{ 'is-user': message.isUser }"
        >
          <div class="message-header">
            <span class="message-author">{{ message.author }}</span>
            <span class="message-time">{{ message.time }}</span>
          </div>
          <p class="message-content">{{ message.content }}</p>
          <img
            v-if="message.image"
            :src="message.image"
            alt="Attached"
            class="message-image"
          />
        </div>
      </div>
      <footer class="chat-footer">
        <input
          v-model="newMessage"
          placeholder="Type a message..."
          @keypress.enter="sendMessage"
        />
        <button @click="sendMessage">Send</button>
      </footer>
    </div>
  </template>
  
  <script>
  import ChatHeader from "./ChatHeader.vue";
  export default {
    name: "ChatWindow",
    components: {
        ChatHeader,
    },
    data() {
      return {
        activeChannel: "#general",
        messages: [
          {
            id: 1,
            author: "Jeshua Stout",
            time: "6:38 PM",
            content: "I did for 6 days in Iceland",
            isUser: false,
          },
          {
            id: 2,
            author: "Harold Adams",
            time: "5:02 PM",
            content: "Which country to visit next?",
            image: "my-top-places.jpg",
            isUser: false,
          },
          {
            id: 3,
            author: "You",
            time: "11:54 AM",
            content: "Wow, it's amazing! I want to buy a van and travel.",
            isUser: true,
          },
        ],
        newMessage: "",
      };
    },
    methods: {
      sendMessage() {
        if (this.newMessage.trim() !== "") {
          this.messages.push({
            id: Date.now(),
            author: "You",
            time: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
            content: this.newMessage,
            isUser: true,
          });
          this.newMessage = "";
        }
      },
      toggleStar() {
        console.log("Star toggled");
      },
      toggleSettings() {
        console.log("Settings toggled");
      },
    },
  };
  </script>
  
  <style scoped>
  .chat-window {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    background-color: #f9f9f9;
    padding: 20px;
  }
  .chat-actions button {
    background: none;
    border: none;
    font-size: 20px;
    cursor: pointer;
  }
  .chat-messages {
    flex-grow: 1;
    overflow-y: auto;
    margin-bottom: 10px;
  }
  .chat-message {
    margin-bottom: 15px;
  }
  .chat-message.is-user {
    text-align: right;
  }
  .message-header {
    font-size: 12px;
    color: #555;
  }
  .message-content {
    margin: 5px 0;
  }
  .message-image {
    max-width: 100%;
    border-radius: 5px;
  }
  .chat-footer {
    display: flex;
    gap: 10px;
  }
  .chat-footer input {
    flex-grow: 1;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
  }
  .chat-footer button {
    padding: 10px 15px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  </style>
  