$(document).ready(function(){

  $( "#navbar-search-bar" ).on("submit", function(event) {
    if ($("#search-text").val() == ""){
      event.preventDefault();
      $("#search-text").focus();
      $("#search-text").select();
    }  // Else, it will submit normally. 
  });

})



