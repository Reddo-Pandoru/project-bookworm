<template>
  <nav class="navbar navbar-dark bg-dark navbar-expand-lg">
    <router-link to="/" class="navbar-brand">Home</router-link>
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarNavAltMarkup"
      aria-controls="navbarNavAltMarkup"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <router-link to="/manageusers" class="nav-item nav-link">Utente</router-link>
        <router-link to="/managebooks" class="nav-item nav-link">Libri</router-link>
      </div>
    </div>
  </nav>
</template>


  

<style scoped lang="scss">
.router-link-active {
  color: white !important;
}
.navbar {
  position: fixed;
  z-index: 9999;
  width: 100%;
}
</style>