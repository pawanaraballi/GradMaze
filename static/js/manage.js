/**
 * Created by Johnny on 6/11/16.
 */


/**
 *
 * General Settings
 *
 * */

// Set up dialog
$( "#dialog" ).dialog({
    autoOpen: false,
    buttons: [{text: "Cancel","class": 'btn btn-success',click: function() {$( "#dialog" ).dialog( "close" );}},
        {text: "Delete","class":'btn btn-danger',click: function() { postData(); $( "#dialog" ).dialog( "close" );}}, ]
});

// Post Delete Account
function postData(){
    $.ajax({
      type: "POST",
      url: "/GradMaze/accounts/delete/",
      data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
      success: function(resultData){
          alert("Save Complete");
      }
});
}

// On Click for Dialog
$( "#opener" ).click(function() {
  $( "#dialog" ).dialog( "open" );
});



/**
 *
 * Applications
 *
 * */

// Add jQuery UI Datepicker to datefields
$( ".datepicker" ).datepicker();


// On Click to show application form
$( "#add-app" ).click(function() {
  $( "#form-app" ).show();
});