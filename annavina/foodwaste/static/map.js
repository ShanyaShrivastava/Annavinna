const map = L.map("map").setView([0,0],10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution : "Annavinna"
}).addTo(map)

if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition((position) => {
        const {latitude,longitude} = position.coords;
        map.setView([latitude,longitude],25);
        L.marker([latitude,longitude]).addTo(map).bindPopup(
            L.popup({
              maxWidth: 200,
              minWidth: 100,
              autoClose: false,
              closeOnClick: true,
              closeButton: true
            }).setContent(
              "Hello"
            )
          )
          .openPopup();
    },(error) => {
        console.log(error)
    },{
        enableHighAccuracy : true,
        timeout : 10000,
        maximumAge : 0,
    })
}