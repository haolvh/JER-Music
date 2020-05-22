<template>
  <div id="app">
    <m-header></m-header>
    <keep-alive>
      <router-view></router-view>
    </keep-alive>
    <recommend></recommend>
    <Slist></Slist>
  </div>
</template>

<script>
import Recommend from "./components/recommend";
import Slist from "./components/Slist";
export default {
  name: 'App',
  components: {Slist, Recommend}
}
</script>

<style lang="scss" scoped>
 // @import './common/scss/index.scss';
  #app {
    position: fixed;
    top: 0;
    height: 100%;
    width: 100%;
    overflow: hidden;
  }
</style>
