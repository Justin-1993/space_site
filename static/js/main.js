mapboxgl.accessToken = 'pk.eyJ1IjoianVzdGluLXdoaXRlIiwiYSI6ImNrbGl0djNxaDRyN3MycG5yMTVhZm1zM3EifQ.DdQv6EbrmH_aplDPUkVMUw';
var map = new mapboxgl.Map({
container: 'map',
style: 'mapbox://styles/mapbox/satellite-streets-v10',
zoom: 5,
});


function update() {

    const url='http://api.open-notify.org/iss-now.json';
    fetch(url, { 
    method: 'GET'
    })
    .then(function(response) { return response.json(); })
    .then(function(json) {
        var obj = json
        var lat = obj.iss_position.latitude
        var lon = obj.iss_position.longitude
    
        map.flyTo({
            center: [lon, lat],
            speed: 0.5
            });

    var marker = new mapboxgl.Marker()
        .setLngLat([lon, lat])
        .addTo(map);


    });
}

update()
window.setInterval( function() {update() }, 10000);
