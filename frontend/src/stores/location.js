import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useLocationStore = defineStore('location', () => {
  const latitude = ref(null)
  const longitude = ref(null)
  const locationAvailable = computed(() => ((latitude !== null) && (longitude !== null)))
  function updateCoordinates(lat, lng) {
    latitude.value = lat,
    longitude.value = lng
  }

  return { latitude, longitude, locationAvailable, updateCoordinates }
})
