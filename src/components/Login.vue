<template>
  <div id="container">
    <img class="logo" src="../assets/logo.png" id="logo">
    <h1>观一塔湖图 · 知燕园万事</h1>
    <Button style="position: relative; top: -36px; width: 120px; background-color: darkred; font-size: 20px; color: white; opacity: 0">刷脸登录</Button>
    <form enctype="multipart/form-data" id="form1" action="/api/faceRecog" style="position: relative; left: 0px; top: -80px;" method="post">
      <input name="img" type="file" accept="image/*;" id="upload" style="width: 220px; height: 80px; opacity: 0">
    </form>

    <!--<input name="img" type="file" accept="image/*;" id="upload" style="width: 220px; height: 80px; opacity: 0" @change="submitt">-->

  </div>
</template>

<script>



  function uploadFile(file){
    var url = '/apii/faceRecog';
    var xhr = new XMLHttpRequest();
    var fd = new FormData();
    xhr.open("POST", url, true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState == 4 && xhr.status == 200) {
        // Every thing ok, file uploaded
        const name = xhr.responseText; // handle response.
        window.open('/message/' + name, '_self');
      }
    };
    fd.append("img", file);
    xhr.send(fd);
  }

export default {
  name: 'hello',
  mounted () {
    const height = document.documentElement.clientHeight;
    document.getElementById('container').style.height = (height - 0) + 'px';

    document.getElementById('upload').addEventListener('change', function(){
      var file = this.files[0];
      // This code is only for demo ...
      uploadFile(file);
      console.log("name : " + file.name);
      console.log("size : " + file.size);
      console.log("type : " + file.type);
      console.log("date : " + file.lastModified);
    }, false);
  },
  methods: {
    upload() {
      console.log('click upload');
      document.getElementById('upload').click();
    },
    submitt() {
//      console.log(12);
//      window.open('www.baidu.com', '_self')
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
