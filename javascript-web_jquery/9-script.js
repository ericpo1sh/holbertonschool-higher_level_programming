#!/usr/bin/node
// Write a JavaScript script that fetches from
// https://hellosalut.stefanbohacek.dev/?lang=fr and displays the value of hello
$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (data) {
      $('#hello').text(data.hello);
    },
    error: function () {
      $('#hello').text('Error: Name not found!');
    }
  });
}
);
