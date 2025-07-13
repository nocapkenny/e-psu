<script setup>
const props = defineProps({
  text: {
    type: String,
    default: "Фамилия",
  },
  type: {
    type: String,
    default: "button",
  }
})
</script>

<template>
  <button :type="props.type" class="button">{{ props.text }}</button>
</template>

<style src="./Button.scss" lang="scss" scoped />
