<template lang="pug">
  div
    main-nav
    .ui.container
      <router-view></router-view>
</template>

<script>
import MainNav from './MainNav.vue'

export default {
  components: {
    MainNav,
  },
}
</script>

<style>
</style>
