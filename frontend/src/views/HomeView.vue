<script setup>

import { onMounted, ref } from 'vue'
import L from 'leaflet'
import "leaflet/dist/leaflet.css"

const map = ref(null)

function formatMap(){
  console.log(map);

  let mapref = L.map(map.value).setView([38.763250, -77.298793], 15); 

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(mapref);

}


onMounted(() =>{
  formatMap();
})

</script>

<template>
  <main>

    

    Hello

    <div class="map-wrapper" ref="map"></div>

  </main>
</template>


<style>
.map-wrapper {
  width: 100%;
  height: 400px;
}
</style>
