$(document).ready(function() {
  // Droppable 
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
          let id = ui.draggable.data("id");
          delete_sale(id)
          ui.draggable.remove()
          display_sales_list(sales) 
        }
      });

  // Autocomplete 
  $( "#log_paper" ).autocomplete({
    source: clients
  });

  // Adding New Name to Autocomplete 
  function addName() {
    unknown = $('#log_paper').val()
    if (!(clients.includes(unknown))){
      clients.push(unknown)
    }
  }
  
  // Adding a new row of data 
  sales.forEach(function(item,index){
    // First we make a row 
    let row = $("<div>").addClass("row gx-1 mb-4").data("id", item.id).draggable({ revert:"invalid"}); 

    // Then we append cols 
    row.append($("<div>").addClass("col-lg-3").text(item.salesperson));
    row.append($("<div>").addClass("col-lg-3").text(item.client));
    row.append($("<div>").addClass("col-lg-3").text(item.reams));

    // The "delete" col
    let btn_x_col = $("<div>").addClass("col-lg-3");
    let btn_x = $("<button>").addClass("btn btn-warning").text("X");

    btn_x.on("click",function(){
      let id = item.id
      delete_sale(id) 
      display_sales_list(sales) 
    })

    btn_x_col.append(btn_x);
    row.append(btn_x_col)

    // Now we append this row dynamically 
    $("#dynamic_content").append(row);
  })  
  
  
  const salespersonName = "Heather Mason" // Our hard-coded salesperson name. 

  function delete_sale(id){
    let data_to_delete = { "id": id } 

    $.ajax({
      type: "POST",
      url: "/delete_sale",
      dataType: "json",
      contentType: "application/json; charset=utf-8", 
      data: JSON.stringify(data_to_delete),
      success: function(result){
        let all_sales = result["sales"]
        sales = all_sales
        display_sales_list(sales) 
      },
      error: function(request,status, error){
        console.log("Error!");
        console.log(request);
        console.log(status);
        console.log(error);
      } 
    });

  }

  /* 
  In HW 4 --> addSale 
  In HW 5 --> save_sale(new_sale)
  */ 
  // Adding a new sale 
  function save_sale(new_sale){
  
    let data_to_save = {"new_sale": new_sale}

    $.ajax({
      type: "POST",
      url: "/save_sale",
      dataType: "json",
      contentType: "application/json; charset=utf-8",
      data: JSON.stringify(data_to_save),
      success: function(result){
        let all_sales = result["sales"]
        sales = all_sales
        display_sales_list(sales) // Update/refresh UI with new data.
        clearFields() // Clear fields for next client upload. 
    
        $("#log_paper").autocomplete({
          source: clients
        })
      },
      error: function(request,status, error){
        console.log("Error!");
        console.log(request);
        console.log(status);
        console.log(error);
      } 
    });
  }

  /* 
  In HW 4 --> UpdateUI (Clientside Data Refresh)
  In HW 5 --> Display Sales (Server)
  */
  function display_sales_list(sales){
    $("#dynamic_content").empty()

    sales.forEach(function(item,index){
      let row = $("<div>").addClass("row gx-1 mb-4").data("id", item.id).draggable({ revert:"invalid"}); 
  
      row.append($("<div>").addClass("col-lg-3").text(item.salesperson));
      row.append($("<div>").addClass("col-lg-3").text(item.client));
      row.append($("<div>").addClass("col-lg-3").text(item.reams));

      let btn_x_col = $("<div>").addClass("col-lg-3");
      let btn_x = $("<button>").addClass("btn btn-warning").text("X");

      btn_x.on("click",function(){
        let id = item.id
        delete_sale(id) 
      })
      
      btn_x_col.append(btn_x);
      row.append(btn_x_col)
  
      $("#dynamic_content").append(row);
    })  
  }

  // Clearing input fields 
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
    $("reams").val("");
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
    let new_sale = {
      salesperson: salespersonName,
      client: $("#log_paper").val(),
      reams: $("#reams").val()
    }
    save_sale(new_sale) // Add sale to JSON data. 
  })
})

