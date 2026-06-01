$( function() {
  $( "#draggable" ).draggable({revert: true, revert: "invalid"});
  $( "#droppable" ).droppable({
    accept: "#draggable",
    classes: {
      "ui-droppable-hover": "ui-state-hover"
    },
    drop: function( event, ui ) {
      $( this )
        .addClass( "ui-state-highlight" )
        .find( "p" )
          .html( "Dropped!" );
    }
  });
} );