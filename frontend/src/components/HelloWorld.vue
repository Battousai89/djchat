<template>
  <div class="hello">

  </div>
</template>

<script>
import axiosInstance from "../axios";

export default {

  name: 'HelloWorld',
  data() {
    return {
      servers: []
    };
  },
  mounted() {
    axiosInstance.get("servers/").then(response => console.log(response.data)).catch(error => console.error(error));
  }
}
</script>

<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
