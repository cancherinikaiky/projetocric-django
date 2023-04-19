const url_python = 'http://127.0.0.1:8000/api/home_cities/'
    fetch(url_python)
    .then(res => res.json())
    .then(e => {
        // console.log(e[0]['coordinates'].lat, e[0]['coordinates'].lng)
        // console.log(e[0].routes)
        let map = new Map();
        map.setMap(e[0]['coordinates'].lat, e[0]['coordinates'].lng)
        addRoutesOnMap(e[0], map.getMap())
    })