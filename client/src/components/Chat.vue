<template>
    <div class="grid-container">
        <div class="col-md-12">
            <chat-input/>
        </div>
        <div class="col-md-12">
            <chat-display/>
        </div>
    </div>
</template>

<script>
import ChatInput from './ChatInput';
import ChatDisplay from './ChatDisplay';

export default {
  components: {
    chatInput: ChatInput,
    chatDisplay: ChatDisplay,
  },
};
</script>

<style>
</style>
