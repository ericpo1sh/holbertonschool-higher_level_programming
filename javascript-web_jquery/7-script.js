#!/usr/bin/node
// Write a JavaScript script that fetches the character name from this URL:
// https://swapi-api.hbtn.io/api/people/5/?format=json
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
    success: function (data) {
      $('#character').text(data.name);
    },
    error: function () {
      $('#character').text('Error: Name not found!');
    }
  });
}
);
