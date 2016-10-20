<template lang="pug">
  div
    div(v-if="tx")
      h1 Tx {{ tx.txid }}

      table.ui.celled.table
        tbody
          tr
            td Create on:
            td {{ tx.time | timeago}}
          tr
            td Belong to Block:
            td {{ tx.blockhash }}
          tr(v-for="op_ret in op_returns")
            td
              code OP_RETURN:
            td
              pre
                code {{ op_ret | json }}

      h2 Raw
      pre
        code {{ tx | json }}
    div(v-else)
</template>

<script>
import filters from '../filters.js'

export default {
  data() {
    return {
      tx: null,
      op_returns: [],
    }
  },
  beforeCreate() {
    const txId = this.$route.params.txId

    this.$http.get(`tx/${txId}/`).then(
      r => r.json(),
      r => {
        console.error(r)
        return null
      }
    ).then(
      data => {
        if (data === null)
          return

        this.tx = data.tx
        this.op_returns = data.op_returns
      }
    )
  },
  filters,
}
</script>

<style scoped>
</style>
