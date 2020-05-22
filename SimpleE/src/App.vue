<template>
  <div id="app">
    <HeaderFirst></HeaderFirst>
    <router-view></router-view>
  </div>
</template>

<script>
  // @import './assets/css/icon.css';
  // @import './assets/css/main.css';
  // @import './assets/css/color-dark.css'; /*深色主题*/
  import HeaderFirst from "./components/HeaderFirst";
  export default {
  name: 'App',
  components:{
    HeaderFirst,

  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
