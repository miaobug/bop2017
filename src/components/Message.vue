<template>
  <div id="container">
    <iframe
      id="bot"
      src='https://webchat.botframework.com/embed/headachePKU?s=GGxpMuU8D6M.cwA.K0E.o7u1TfdccY0LIc9Gc_lz8gqQUvbnORywUt9J3WkTc_g'
      style="width: 100%"
    >
    </iframe>
  </div>
</template>

<script>
export default {
  name: 'hello',
  mounted () {
    const height = document.documentElement.clientHeight;
    document.getElementById('bot').style.height = (height - 0) + 'px';
  },
  methods: {
  },
  data () {
    return {
    }
  }
}



</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    text-align: center;
  }
</style>
