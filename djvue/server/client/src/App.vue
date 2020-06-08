<template>
  <Navbar/>
 <Container />
</template>

<script>
import Container from './views/manage-books.vue'
import Navbar from './components/nav-bar.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    Container

  }
}
</script>

<style>
</style>
