<script setup>
const props = defineProps({
    text: {
        type: String,
        default: "Фамилия",
    },
    type: {
        type: String,
        default: "text",
    }
})
</script>

<template>
    <input class="input" :type="props.type" :placeholder="props.text">
</template>

<style src="./Input.scss" lang="scss" scoped />