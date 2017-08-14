<template>
  <div id="container">
    <img class="logo" src="../assets/logo.png" id="logo">
    <h1>观一塔湖图 · 知燕园万事</h1>
    <Button style="position: relative; top: -36px; width: 120px; background-color: darkred; font-size: 20px; color: white; opacity: 0">刷脸登录</Button>
    <form id="form1" action="" style="position: relative; left: 0px; top: -80px;" v-on:submit.prevent="alert('submit')" method="post" action="/">
      <input name="img" type="file" accept="image/*;" id="upload" style="width: 220px; height: 80px; opacity: 0" @change="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: 'hello',
  mounted () {
    const height = document.documentElement.clientHeight;
    document.getElementById('container').style.height = (height - 0) + 'px';
  },
  methods: {
    upload() {
      console.log('click upload');
      document.getElementById('upload').click();
    },
    submit() {
//      console.log(12);
      window.open('www.baidu.com', '_self')
      document.getElementById('form1').submit();
    },
  },
  data () {
    return {
    }
  }
}
//


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    text-align: center;
    /*margin: 10px;*/
    /*border: 1px solid #eee;*/
    position: relative;
  }
  #container:after {
    content: '';
    display: block;
    width: 100%;
    height: 100%;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background: url('../assets/bg1.jpg');
    background-size: cover;
    opacity: 0.5;
    z-index: -1;
  }
  #logo {
    width: 200px;
    margin-top: 30%;
  }
  h1 {
    margin-top: 100px;
    color: darkred;
    animation: 3s disappear forwards;
  }

  Button {
    animation:  3s 2s showup forwards;
    opacity: 0;
  }

  @keyframes disappear
  {
    0%   {opacity: 1;}
    100% {opacity: 0;}
  }

  @keyframes showup
  {
    0%   {opacity: 0;}
    100% {opacity: 1;}
  }

</style>
