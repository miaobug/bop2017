<template>
  <div id="container">
    <div id="allmap"></div>
  </div>
</template>



<script>
export default {
  name: 'hello',
  mounted () {
    const height = document.documentElement.clientHeight;
    document.getElementById('container').style.height = (height - 0) + 'px';
    this.search(this.from, this.to);
  },
  methods: {
      search(from, to) {
//        var from = myform.from.value;
//        var to = myform.to.value;
        console.log(from, to);
        var map = new BMap.Map("allmap");
        map.enableScrollWheelZoom();
        map.centerAndZoom(new BMap.Point(116.404, 39.915), 11);
        var walking = new BMap.WalkingRoute(map, {renderOptions:{map: map, autoViewport: true}});
        walking.search(from, to);
      }
  },
  data () {
    return {
      id: this.$route.params.id,
      from: this.$route.params.from,
      to: this.$route.params.to,
    }
  }
}



</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    text-align: center;
  }
  #allmap {
    width: 100%;
    height: 100%;
    overflow: hidden;
    margin:0;
    font-family:"微软雅黑";
  }
</style>
