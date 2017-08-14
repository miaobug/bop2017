<template>
  <div id="container">
    <!--<iframe-->
      <!--id="bot"-->
      <!--src='https://webchat.botframework.com/embed/headachePKU?s=GGxpMuU8D6M.cwA.K0E.o7u1TfdccY0LIc9Gc_lz8gqQUvbnORywUt9J3WkTc_g'-->
      <!--style="width: 100%"-->
    <!--&gt;-->
    <!--</iframe>-->
    <div id="messageBody">
      <div class="header">聊天</div>
      <div id="messageContainer">
        <div id="messageWrapper">
          <div v-for="item in messages">
            <div class="msg bot-msg" v-if="item.from === 'bot'">
              <div v-if="item.type === 'msg'">{{item.content}}</div>
              <div v-else @click="startNav(item)">{{item.content}}</div>
            </div>
            <div class="msg user-msg" v-if="item.from === 'user'">{{item.content}}</div>
            <div style="clear: both;"></div>
          </div>
        </div>
      </div>
    </div>
    <div id="messageBar">
      <div id="sendPhoto" @click="sendPhoto"><img src="../assets/img.png" alt=""><input name="img" type="file" accept="image/*;" id="upload" style="width: 50px; height: 50px; left: 0; top: 0; opacity: 0; position: absolute;"></div>
      <input v-model="message" type="text" @keyup.enter="sendMsg">
      <div id="sendBtn" @click="sendMsg"><img width="40" height="40" src="../assets/send.png" alt=""></div>
      <div class="" style="clear: both;"></div>
    </div>
  </div>
</template>

<script>

  import Vue from 'vue'
  import axios from 'axios'
  import localStorage from 'vue-localstorage'
  Vue.use(localStorage)

//  function uploadFile(file){
//    var url = '/api/sceneRecog';
//    var xhr = new XMLHttpRequest();
//    var fd = new FormData();
//    xhr.open("POST", url, true);
//    xhr.onreadystatechange = function() {
//      if (xhr.readyState == 4 && xhr.status == 200) {
//        // Every thing ok, file uploaded
//        const name = xhr.responseText; // handle response.
////        window.open('/message/' + name, '_self');
//
//      }
//    };
//    fd.append("img", file);
//    xhr.send(fd);
//  }

export default {
  name: 'hello',
  mounted () {
    this.id = this.$route.params.id;
    this.loadMsg();
    const height = document.documentElement.clientHeight;
    document.getElementById('messageContainer').style.height = (height - 102) + 'px';
    document.getElementById('messageWrapper').style.height = (height - 102) + 'px';
    this.containerHeight = height - 100;
    this.$nextTick(() => {
      document.getElementById('messageContainer').scrollTop = document.getElementById('messageWrapper').scrollHeight - this.containerHeight
    });
    const that = this;
    document.getElementById('upload').addEventListener('change', function(){
      let file = this.files[0];
      // This code is only for demo ...
      that.uploadFile(file);
      console.log("name : " + file.name);
      console.log("size : " + file.size);
      console.log("type : " + file.type);
      console.log("date : " + file.lastModified);
    }, false);

    const id = this.$route.params.id;
    if(id != -1) {
      this.messages.push({
        content: '你好,' + id,
        from: 'bot',
        type: 'msg'
      });

      this.$localStorage.set('msg' + this.id, JSON.stringify(this.messages));
    }
  },
  methods: {
    uploadFile(file){
      var url = '/api/sceneRecog';
      var xhr = new XMLHttpRequest();
      var fd = new FormData();
      xhr.open("POST", url, true);
      const that = this;
      xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
          // Every thing ok, file uploaded
          const name = xhr.responseText; // handle response.
//        window.open('/message/' + name, '_self');
          console.log(name);
          that.messages.push({
            content: name,
            from: 'bot',
            type: 'msg'
          });

          that.$localStorage.set('msg' + this.id, JSON.stringify(this.messages));
        }
      };
      fd.append("img", file);
      xhr.send(fd);
    },
    sendPhoto: function () {

    },
    sendMsg: function () {
//      console.log(this.messages);
      if (this.message.length > 0) {
        this.messages.push({
          content: this.message,
          from: 'user',
          type: 'msg'
        });
//        console.log(document.getElementById('messageContainer').scrollTop);
//        console.log(document.getElementById('messageWrapper').scrollHeight);
//        console.log(this.containerHeight);
        this.$localStorage.set('msg' + this.id, JSON.stringify(this.messages));
        axios.get('/api/query/' + this.message).then((response) => {
          console.log(response.data);
          if (response.data.direction === 'answer') {
            this.messages.push({
              content: response.data.param,
              from: 'bot',
              type: 'msg'
            });
            this.$localStorage.set('msg' + this.id, JSON.stringify(this.messages));
          } else if (response.data.direction === 'navigate') {
            this.messages.push({
              content: '点击前往' + response.data.param,
              from: 'bot',
              type: 'nav',
              param: response.data.param
            });
          }
          this.message = '';
          this.$nextTick(() => {
            document.getElementById('messageContainer').scrollTop = document.getElementById('messageWrapper').scrollHeight - this.containerHeight
          });
        });
      }
    },
    loadMsg: function () {
      let tmp = this.$localStorage.get('msg' + this.id);
      if (tmp) {
        this.messages = JSON.parse(tmp)
        console.log(this.messages)
      }
    },
    startNav: function (item) {
//      勺园 博雅塔 未名湖 百周年纪念讲堂 北京大学图书馆 邱德拔体育馆 燕南园-38号楼
      this.$router.push({path: `/map/${this.id}/北京大学图书馆/${item.param}`})
    }
  },
  data () {
    return {
      messages: [],
      message: '',
      containerHeight: 0,
      id: ''
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #container {
    /*text-align: center;*/
    padding: 0;
  }
  .header {
    font-size: 1.5rem;
    color: #ffffff;
    width: 100%;
    height: 50px;
    padding: 0.3rem 0.8rem;
    background: #36baec;
  }
  #messageContainer {
    overflow: auto;
    font-size: 1rem;
    padding: 0 1rem;
  }
  #messageBar {
    border-top: 1px solid #a3a3a3;
    border-bottom: 1px solid #a3a3a3;
    width: 100%;
    height: 50px;
    padding: 0;
  }
  #messageBar {

  }
  #sendPhoto {
    position: relative;
    float: left;
    width: 15%;
    padding: 7px 11px;
  }
  #messageBar input {
    float: left;
    height: 49px;
    font-size: 1.5rem;
    padding: 0 0.5rem;
    border: none;
    border-left: 1px solid #a3a3a3;
    border-right: 1px solid #a3a3a3;
    border-bottom: 1px solid #a3a3a3;
    margin: 0;
    width: 70%;
  }
  #sendBtn {
    padding: 5px;
    float: left;
    width: 15%;
    height: 48px;
  }
  .user-msg {
    max-width: 70%;
    float: right;
    background: #36baec;
    color: #ffffff;
  }
  .bot-msg {
    max-width: 70%;
    float: left;
    background: #cbcbcb;
    color: #000;
  }
  .msg {
    padding: 0.2rem 0.5rem;
    margin: 0.5rem 0;
  }
</style>
