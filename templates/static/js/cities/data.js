 

var url = window.location.href;
var cidadeId = url.match(/\/(\d+)\/?$/)[1];

const url_python = `http://127.0.0.1:8000/api/cities/${cidadeId}`
    fetch(url_python)
    .then(res => res.json())
    .then(e => {
       e.routes.forEach(element => {
        my_function(element)
       });
    })
