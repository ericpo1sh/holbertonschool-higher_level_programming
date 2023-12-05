#!/usr/bin/node
// Write a JavaScript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header
$('#toggle_header').click(function () {
  if ($('header').hasClass('red')) {
    $('header').toggleClass('green');
  } else {
    $('header').toggleClass('red');
  }
});
