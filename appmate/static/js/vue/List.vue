<template lang="pug">
  div
    h2 Recent Blocks
    table.ui.celled.table
      thead
        tr
          th Index
          th Block Hash
          th Tx Count
          th Timestamp
      tbody
        tr(v-for="block in blocks")
          td {{ block.height }}
          td
            router-link(
              v-bind:to="{name: 'detail', params: {blockId: block.height}}"
            ) {{ block.hash }}
          td {{ block.tx.length }}
          td {{ moment(block.time * 1000).fromNow() }}
</template>

<script>
import moment from 'moment'

export default {
  data() {
    return {
      blockcount: null,
      blocks: [],
      moment,
    }
  },
  mounted(){
    this.blockinfo()
  },
  methods: {
    blockinfo(){
      this.$http.get('blockinfo/').then(
        res => res.json(),
        res => {
          console.log(res.json())
          return null
        }
      ).then(
        data => {
          if(data === null)
            return

          this.blockcount = data.blockcount
          this.blocks = data.blocks

          setTimeout(this.blockinfo, 800);
        }
      )
    },
  },
}
</script>

<style scoped>
</style>
