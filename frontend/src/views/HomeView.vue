<script setup>

import { onMounted, ref } from 'vue'
import L from 'leaflet'
import "leaflet/dist/leaflet.css"

const catchMap = ref(null)
const templateMap = ref(null)
const selectedFishery = ref(null)
const showCatchMap = ref(true) 
const showAddNewCatch = ref(false)


function getFishery(id){
    const map = new Map([
        [1, {"latitude":38.763250, "longitude": -77.298793, "name":"Burke Lake"}],
        [2, {"latitude":38.742047, "longitude": -77.387657, "name":"Bull Run"}]
    ])

    return map.get(id)
}

function addNewFishery(){
  console.log("Adding new Fishery")
}

function updateMapFishery(){

  if(selectedFishery !== "")
  {
    let fishery = getFishery(Number(selectedFishery.value))
    catchMap.value.setView([fishery.latitude, fishery.longitude], 15)
  }
  
}

function handleCatchClick(e){
  console.log(e)
  showCatchMap.value = false;
  showAddNewCatch.value = true;
}

function cancelAddNewCatch(e){
  showCatchMap.value = true;
  showAddNewCatch.value = false;
}

function initializeMap(){
  
  catchMap.value = L.map(templateMap.value).setView([38.763250, -77.298793], 15); 

  L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(catchMap.value);

  catchMap.value.on('click', handleCatchClick)

}


onMounted(() =>{
  initializeMap();

})

</script>

<template>
  <main>

    <div v-show ="showCatchMap"> 

        <div class="row ms-3 mt-3">
       <div class="col-4">
          <select v-model="selectedFishery" @change="updateMapFishery" class="form-select" aria-label="Default select example">
            <option selected>Please select a fishery</option>
            <option value="1">Burke Lake</option>
            <option value="2">Bull Run</option>
          </select>
       </div> 
       <div class="col-2">
          <button class="btn btn-outline-primary" @click="addNewFishery">Add New Fishery</button>
       </div>
        </div>     
    
        <div class="row mt-5">
          <div class="col-12 map-wrapper" ref="templateMap"></div>
      </div>  

    </div>
    <div class="row mt-5" v-show ="showAddNewCatch">
      
      <div class="ms-2 col-md-8">

        <h3>Catch Specifics</h3>

        <select class="form-select mt-3" aria-label="Species">
          <option selected>Select Species</option>
          <option value="1">Bass</option>
          <option value="2">Snakehead</option>
          <option value="3">Crappie</option>
          <option value="4">Perch</option>
        </select>

        <select class="form-select mt-3" aria-label="Technique">
          <option selected>Select Technique</option>
          <option value="1">Jig</option>
          <option value="2">Spinnerbait</option>
          <option value="3">Texas Rig</option>
          <option value="4">Squarebill</option>
        </select>

        <select class="form-select mt-3" aria-label="Technique">
          <option selected>Select Weather Conditions</option>
          <option value="1">Sunny</option>
          <option value="2">Partly Cloudy</option>
          <option value="3">Texas Rig</option>
          <option value="4">Squarebill</option>
        </select>

        <button class="btn btn-outline-secondary mt-3" @click="cancelAddNewCatch">Cancel</button>
        <button class="btn btn-outline-primary ms-3 mt-3">Save</button>
      </div>


    </div>   
  </main>



</template>


<style>
.map-wrapper {
  width: 100%;
  height: 400px;
}
</style>
