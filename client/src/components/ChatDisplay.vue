<template>
  <div>
    <div v-for="(message,index) in messages" v-bind:key="index">
      <span v-bind:title="message.datetime">&lt;{{message.user}}&gt; {{message.content}}</span>
    </div>
  </div>
</template>

<script>
import io from 'socket.io-client';

export default {
  data() {
    return {
      messages: [{
        datetime: new Date().toISOString(),
        user: 'system',
        content: 'app starting',
      }],
      socket: null,
    };
  },
  mounted() {
    // this.socket = io.connect(`http://${document.domain}:${location.port}`);
    this.socket = io();
    this.socket.on('connect', () => {
      this.messages.unshift({
        datetime: new Date().toISOString(),
        user: 'system',
        content: 'connected to server!',
      });
    });
    this.socket.on('message', (data) => {
      this.messages.unshift(data);
    });
  },
  destroyed() {
    this.socket.close();
  },
};
</script>

<style>

</style>
