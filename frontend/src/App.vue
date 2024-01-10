<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import LocationResolver from './components/LocationResolver.vue';
</script>

<template>
  <LocationResolver />
  <RouterView />
</template>

