<script setup>
   import {onMounted, ref} from 'vue'
   import LocationService from '../services/LocationService'
   import { useLocationStore } from '@/stores/location'
   import { storeToRefs } from 'pinia'

   const store = useLocationStore()

   const {latitude, longitude, locationAvailable, updateCoordinates} = store

   function syncCoordinates(){
      console.log("Hello")
   }

   onMounted(() => {

      if (!locationAvailable) {
         new LocationService().getCurrentLocation((position) => {
            //latitude.value = position.coords.latitude;
            //longitude.value = position.coords.longitude;
            //locationAvailable.value = true;
            updateCoordinates(position.coords.latitude, position.coords.longitude)
         })
      }

      window.setInterval(() => {
            console.log("Executing Poll")
      }, (60000 + 15))

      
   })

 

</script>

<template></template>