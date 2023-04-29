export class Map {
  constructor() {
    this.map = null;
  }

  setMap(lat, lng) {
    this.map = L.map('map', {scrollWheelZoom: false}).setView([lat, lng], 12);
  }

  getMap() {
    return this.map;
  }

  addRoutes(e) {
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
                  attribution:
                    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> <strong>ROTACRIC</strong>',
    }).addTo(this.map);

    e.routes.forEach(e => {
      var coordinates = L.Polyline.fromEncoded(
      e.polyline
    ).getLatLngs();
        
    L.polyline(coordinates, {
      color: "red",
      weight: 4,
      opacity: 1,
      lineJoin: "round",
    }).addTo(this.map);
    })

    
    e.points.forEach(element => {
    const newIcon = new L.Icon({
                        iconUrl: element.category.photo,
                        iconSize: [30, 40],
                        iconAnchor: [5, 30],
                        popupAnchor: [10, -20]
                    })

    L.marker([element.coordinates['lat'], element.coordinates['lng']],{icon: newIcon})
            .bindPopup(`
            ${bindPopupName(element.name)} 
            ${bindPopupImage(element.image)}
            ${bindPopupAddress(element.address)}
            ${bindPopupOpeningHours(element.business_hours)}
            ${bindPopupPhone(element.phone)}
            `,{
            maxWidth: 150,
            keepInView: true,
            className: "markerPopup"
            })
            .addTo(this.map)
    })
  }
}

const bindPopupName = (name) => {
    return `<h1>${name}</h1>`;
}

const bindPopupImage = (image) => {
    if(image == null) {
        return `<p>Foto não informada</p>`
    }
    return `<img src=${image}>`;
}

const bindPopupAddress = (address) => {
    return `<p>Endereço: ${address.street_name}, ${address.number}, ${address.neighborhood}</p>`;
}

const bindPopupOpeningHours = (hours) => {
    return `<p>Horário de atendimento: ${hours}</p>`;
}

const bindPopupPhone = (phone) => {
    return `<p>Contato: ${phone}</p>`;
}
