<template lang="pug">
  div(v-if="block")
    h1 Block {{ block.hash }}

    h3 Transactions in this Block
    table.ui.celled.table
      thead
        tr
          th Tx ID
      tbody
        tr(v-for="tx in block.tx")
          td
            router-link(
              v-bind:to="{name: 'txDetail', params: {txId: tx}}"
            ) {{ tx }}

    h3 Raw
    pre
      code {{ block | json }}
</template>

<script>
export default {
  data(){
    return {
      block: null,
    }
  },
  beforeCreate() {
    const blockId = this.$route.params.blockId

    this.$http.get(`block/${blockId}/`).then(
      r => r.json(),
      r => {
        console.error(r)
        return null
      }
    ).then(
      data => {
        if (data === null)
          return

        this.block = data
      }
    )
  },
  filters: {
    json(val) {
      return JSON.stringify(val, null, 2)
    },
  },
}
</script>

<style scoped>
</style>
