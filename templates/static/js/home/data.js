const url_python = 'http://127.0.0.1:8000/api/home_routes/'
    fetch(url_python)
    .then(res => res.json())
    .then(rotas => {
        rotas.forEach(e => {
            my_function(e)  /* static/js/map/map.js */
        })
    })