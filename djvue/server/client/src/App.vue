<template>
  <div id="app">
    <navBar></navBar>
    <div class="main-section">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import navBar from '@/components/nav-bar';
//import container from '@/views/manage-books';
import 'bootstrap/dist/js/bootstrap.bundle';
import 'awesome-notifications/dist/style.css';
export default {
  name: 'app',
  components: {
    navBar
  }
};
</script>

<style lang="scss">
@import '@/styles/index.scss';
</style>