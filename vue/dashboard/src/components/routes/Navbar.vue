<template>
    <div class="Navbar">
        <header>
      <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
        <router-link class="navbar-brand" to="/">Dashboard</router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link class="nav-link" to="AddWidget">Add Widget</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="ManageWidgets">Manage Widgets</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="Account">Account</router-link>
            </li>
            <li class="nav-item">
              <span @click="logout" class="nav-link">Logout</span>
            </li>
          </ul>
          <form class="form-inline mt-2 mt-md-0">
            <li class="nav-item">
              <router-link class="nav-link" to="Admin">Admin</router-link>
            </li>
          </form>
        </div>
      </nav>
    </header>
    </div>
</template>

<script>
export default {
    name: "Navbar",
    data () {
        return {
            
        }
    },
    methods: {
      logout: function() {
        localStorage.removeItem('access_token');
        this.$router.push({name: "Login"});
      }
    }
}
</script>
<style scoped>
</style>