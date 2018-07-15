<template>
  <div>
    <b-form @submit="sendMessage">
      <b-form-input v-model="message"
        type="text"
        placeholder="Chat!"
        />
    </b-form>
    <small><span class="clickable" @click="changeName">Change your name ({{nick}})</span></small>
    <b-modal id="modal1" ref="nameChangeModal" title="Name change" hide-footer>
      <b-form @submit="changeNameFin">
        <b-form-input v-model="nick"
          type="text"
          placeholder="Your name"/>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      nick: 'Zjeb',
      message: 'Hello!',
    };
  },
  methods: {
    changeName() {
      this.$refs.nameChangeModal.show();
    },
    changeNameFin() {
      this.$refs.nameChangeModal.hide();
    },
    sendMessage() {
      axios.post('/api/send-msg', {
        nick: this.nick,
        message: this.message,
      })
        .then((response) => {
          this.msg = response.data.tiem;
        })
        .catch((e) => {
          // eslint-disable-next-line
          console.log(e);
        });
      this.message = '';
    },
  },
};
</script>

<style>
span.small{
  font-size: 9px;
}
span.clickable:hover {
  text-decoration: underline dotted;
}
</style>
