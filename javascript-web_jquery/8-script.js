#!/usr/bin/node
// Write a JavaScript script that fetches and lists the title for all
// movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/films/?format=json',
    success: function (data) {
      for (const info of data.results) {
        $('#list_movies').append(`<li>${info.title}</li>`);
      }
    },
    error: function () {
      $('#list_movies').text('Error: Name not found!');
    }
  });
}
);
