const map = L.map("map").setView([0,0],10);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution : "Annavinna"
}).addTo(map)

if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition((position) => {
        const {latitude,longitude} = position.coords;
        map.setView([latitude,longitude],12);
    },(error) => {
        console.log(error)
    },{
        enableHighAccuracy : true,
        timeout : 10000,
        maximumAge : 0,
    })
}

latlonarr.forEach(elem => {
    L.marker([elem.lat,elem.lon]).addTo(map).bindPopup(
        L.popup({
          maxWidth: 200,
          minWidth: 100,
          autoClose: false,
          closeOnClick: true,
          closeButton: true
        }).setContent(
           `<h1 class="font-semibold">${elem.name}</h1><a href="tel:${elem.phone}">${elem.phone}</a>`
        )
      )
      .openPopup();
})
