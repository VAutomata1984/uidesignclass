$(document).ready(function(){

// Search Bar Function 
$("#navbar-search-bar" ).on("submit", function(event) {
  if ($("#search-text").val() == ""){
    event.preventDefault();
    $("#search-text").focus();
    $("#search-text").select();
  }  // Else, it will submit normally. 
});


// Homepage Link
let popular_cafes = [
  {id: 1, title: "Georgie's Cafe & Bar",},
  {id: 3, title: "Kona Coffee Roasters | Midtown",},
  {id: 10, title: "Joe's Coffee | Columbia University - Journalism School",},
];

function homepageDisplay(){
  popular_cafes.forEach(cafe =>{
    $("#homepage_display").append(
      $("<p></p>").append(
        $("<a></a>").attr("href", `/view/${cafe.id}`).text(cafe.title)
      )
    )
  })
};

homepageDisplay()




});
