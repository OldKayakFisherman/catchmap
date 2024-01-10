

export default class LocationService
{
    getCurrentLocation(location) {
        
        if(navigator.geolocation){
            navigator.geolocation.getCurrentPosition((position) => {
                location(position);
            });
        }

    }
}