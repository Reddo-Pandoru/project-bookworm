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
        <router-link to="/manageusers" class="nav-item nav-link">Utenti</router-link>
        <router-link to="/managebooks" class="nav-item nav-link">Libri</router-link>
        <router-link to="/createuser" class="nav-item nav-link"> new User</router-link>
        <router-link to="/createbook" class="nav-item nav-link">Nuovo libro</router-link>
        <router-link to="/loanbook" class="nav-item nav-link">Prestiti</router-link>
        <router-link to="/returnbook" class="nav-item nav-link">Restituzioni</router-link>
      </div>
    </div>
  </nav>
</template>

<script>
</script>
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