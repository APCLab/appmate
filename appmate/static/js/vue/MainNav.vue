<template lang="pug">
  .ui.top.huge.olive.inverted.attached.menu
    .ui.container
      .item Blockchain Browser
      router-link.item(v-bind:to="{name: 'index'}")
        i.home.icon
        | Home
</template>

<script>
export default {
}
</script>

<style scoped>
.ui.menu {
  margin-bottom: 20px;
}
</style>
