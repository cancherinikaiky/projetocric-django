
var url = window.location.href;
var cityId = url.match(/\/(\d+)\/?$/)[1];

const url_python = `http://127.0.0.1:8000/api/cities/${cityId}`
    fetch(url_python)
    .then(res => res.json())
    .then(e => {
      // console.log(e)
      let map = new Map();
      map.setMap(e['coordinates'].lat, e['coordinates'].lng)
      addRoutesOnMap(e, map.getMap())
    })
