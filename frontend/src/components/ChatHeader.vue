<template>
    <div class="header">
      <div class="header-left">
        <h3>#general</h3>
        <p>{{ memberCount }} members</p>
      </div>
      <div class="header-right">
        <input type="text" placeholder="Search" class="search-input" />
        <button class="icon-button">🔔</button>
        <button class="icon-button">⚙️</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ChatHeader",
    data() {
      return {
        memberCount: 1093,
      };
    },
  };
  </script>
  
  <style scoped>
  .header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: rgb(249, 249, 249);
    padding: 10px;
    color: white;
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  
  .header-left h3 {
    margin: 0;
  }
  
  .search-input {
    padding: 5px;
    border-radius: 5px;
    margin-right: 10px;
  }
  
  .icon-button {
    background: none;
    border: none;
    font-size: 20px;
    color: white;
    margin-left: 10px;
    cursor: pointer;
  }
  
  .icon-button:hover {
    color: #7289da;
  }
  </style>
  