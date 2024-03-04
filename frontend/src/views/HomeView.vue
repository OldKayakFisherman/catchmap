<script setup>

import { onMounted, ref } from 'vue'
import L from 'leaflet'
import "leaflet/dist/leaflet.css"

const map = ref(null)

function addNewFishery(){
  console.log("Adding new Fishery")
}

function updateMapFishery(src){
  console.log(src)
}

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

    <div class="row ms-3 mt-3">
       <div class="col-4">
          <select @change="updateMapFishery" class="form-select" aria-label="Default select example">
            <option selected>Please select a fishery</option>
            <option data-longitude="38.763250" data-latitude="-77.298793">Burke Lake</option>
            <option data-longitude="38.742047" data-latitude="-77.387657">Bull Run</option>
          </select>
       </div> 
       <div class="col-2">
          <button class="btn btn-outline-primary" @click="addNewFishery">Add New Fishery</button>
       </div>
    </div>     
    
    <div class="row">
      <div class="col-4">
        Side Menu
      </div>
      <div class="col-8 map-wrapper" ref="map"></div>
    </div>  
    

  </main>
</template>


<style>
.map-wrapper {
  width: 100%;
  height: 400px;
}
</style>
