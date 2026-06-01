$(document).ready(function() {

  $("#trash").droppable({
        accept:".row",

        over: function(){
          $(this).css("background-color","yellow");
        },

        out: function(){
          $(this).css("background-color","gray");
        },

        drop: function (event, ui){
          $(this).css("background-color","gray");
          let index = ui.draggable.data("index");
          sales.splice(index,1)
          updateUI()
          ui.draggable.remove()
        }
      });


  // Data I
  let clients = [
    "Shake Shack",
    "Toast",
    "Computer Science Department",
    "Teacher's College",
    "Starbucks",
    "Subsconsious",
    "Flat Top",
    "Joe's Coffee",
    "Max Caffe",
    "Nussbaum & Wu",
    "Taco Bell",
  ];

  // Data II 
  let sales = [
    {
      "salesperson": "James D. Halpert",
      "client": "Shake Shack",
      "reams": 100
    },
    {
      "salesperson": "Stanley Hudson",
      "client": "Toast",
      "reams": 400
    },
    {
      "salesperson": "Michael G. Scott",
      "client": "Computer Science Department",
      "reams": 1000
    },
  ]
  
  // Autocomplete 
  $( "#log_paper" ).autocomplete({
    source: clients
  });

  function addName() {
    unknown = $('#log_paper').val()
    if (!(unknown in clients)){
      clients.push(unknown)
    }
  }

  

  sales.forEach(function(item,index){
    let row = $("<div>").addClass("row gx-1 mb-4").data("index", index).draggable({ revert:"invalid"}); 

    row.append($("<div>").addClass("col-lg-3").text(item.salesperson));
    row.append($("<div>").addClass("col-lg-3").text(item.client));
    row.append($("<div>").addClass("col-lg-3").text(item.reams));

    let btn_x_col = $("<div>").addClass("col-lg-3");
    let btn_x = $("<button>").addClass("btn btn-warning").text("X");

    btn_x.on("click",function(){
      sales.splice(index,1)
      updateUI()
    })

    btn_x_col.append(btn_x);
    row.append(btn_x_col)

    $("#dynamic_content").append(row);
  })  
  
  const salespersonName = "Durandal" // Our hard-coded salesperson name. 

  function addSale(){
    let newClient = $("#log_paper").val();
    let numReams = $("#reams").val()

    let newSale = {
      salesperson: salespersonName,
      client: newClient,
      reams: numReams,
    };

    sales.unshift(newSale);
  }

  function updateUI(){
    $("#dynamic_content").empty()

    sales.forEach(function(item,index){
      let row = $("<div>").addClass("row gx-1 mb-4").data("index", index).draggable({ revert:"invalid"}); 
  
      row.append($("<div>").addClass("col-lg-3").text(item.salesperson));
      row.append($("<div>").addClass("col-lg-3").text(item.client));
      row.append($("<div>").addClass("col-lg-3").text(item.reams));

      let btn_x_col = $("<div>").addClass("col-lg-3");
      let btn_x = $("<button>").addClass("btn btn-warning").text("X");

      // below is needed for #13.  
      btn_x.on("click",function(){
        sales.splice(index,1)
        updateUI()
      })
      
      btn_x_col.append(btn_x);
      row.append(btn_x_col)
  
      $("#dynamic_content").append(row);
    })  
  }

  function clearFields(){
    $("#log_paper").val("")
    $("#reams").val("")
    $("#log_paper").focus();
    $("#log_paper").select();
  }
  
  // Error Catching 
  $("#log_paper").keydown(function(event){
    if (event.key == "Enter"){
      event.preventDefault()
    }
  })

  $("#reams").keydown(function(event){
    if (event.key == "Enter"){
      let reamVal = $("#reams").val().trim()
      if ( reamVal == "") {
        event.preventDefault()
      }
    }
  })

  $("#the_form").on("submit", function(e){
    if ($("#log_paper").val() == "" && $("#reams").val() == "") {
        e.preventDefault()
        $("#log_paper").attr("placeholder","Client Required")
        $("#log_paper").addClass("error")
        $("#reams").attr("placeholder","# Reams Required")
        $("#reams").addClass("error")
        $("#log_paper").focus();
        $("#log_paper").select();
        return false
    } else if ($("#log_paper").val() == "" && $("#reams").val() != "") {
        e.preventDefault()
        $("#log_paper").attr("placeholder","Client Required")
        $("#log_paper").addClass("error")
        $("#log_paper").focus();
        $("#log_paper").select();
        return false
    } else if ($("#log_paper").val() != "" && $("#reams").val() == ""){
        e.preventDefault()
        $("#reams").attr("placeholder","# Reams Required")
        $("#reams").addClass("error")
        $("#reams").focus();
        $("#reams").select();
        return false
    } else {
      $("#log_paper").attr("placeholder","Client")
      $("#log_paper").removeClass("error")
      $("#reams").attr("placeholder","# Reams")
      $("#reams").removeClass("error")
    }

  let NumReams = Number($("#reams").val())

  if (isNaN(NumReams)){
    e.preventDefault()
    $("#reams").attr("placeholder","Input a # Please")
    $("#reams").addClass("error")
    $("#reams").focus();
    $("#reams").select();

    return false 
  } else{ 
    $("#reams").attr("placeholder","# Reams")
    $("#reams").removeClass("error")
  }

    e.preventDefault();
    addName() // If name not in data, put name in data. 
    addSale() // Add sale to JSON data. 

    updateUI() // Update/refresh UI with new data.
    clearFields() // Clear fields for next client upload. 
  })

  console.log(sales)

})

