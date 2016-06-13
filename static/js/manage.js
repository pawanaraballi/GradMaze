/**
 * Created by Johnny on 6/11/16.
 */


/**
 *
 * General Settings
 *
 * */

// Set up dialog
$( "#dialog-acc-delete" ).dialog({
    autoOpen: false,
    buttons: [{text: "Cancel","class": 'btn btn-success',click: function() {$( "#dialog-acc-delete" ).dialog( "close" );}},
        {text: "Delete","class":'btn btn-danger',click: function() { postDeleteAcc(); $( "#dialog-acc-delete" ).dialog( "close" );}}, ]
});

// Post Delete Account
function postDeleteAcc(){
    $.ajax({
      type: "POST",
      url: "/GradMaze/accounts/delete/",
      data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
      success: function(resultData){

      }
});
}

// On Click for Dialog
$( "#opener" ).click(function() {
  $( "#dialog-acc-delete" ).dialog( "open" );
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


// On Click to show application form
$('.remove-app').click(function(e) {
    $( "#dialog-app-delete").data('row_id',$(e.target).parent().parent()[0].id)
    $( "#dialog-app-delete" ).dialog( "open" );
});

// Post Delete Application
function postDeleteApplication(row_id){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/apps/delete/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN,
                "row_id":row_id},
          success: function(resultData){

          }
    });
}

$( "#dialog-app-delete" ).dialog({
    autoOpen: false,
    buttons: [
        {text: "Cancel",
        "class": 'btn btn-success',
        click: function() {
            $( "#dialog-app-delete" ).dialog( "close" );
        }},
        {text: "Delete",
         "class":'btn btn-danger',
         click: function(e) {
             postDeleteApplication($( "#dialog-app-delete").data('row_id'));
             $( "#dialog-app-delete" ).dialog( "close" );
             $('#'+$( "#dialog-app-delete").data('row_id')).remove();}
        }]
});



$(".modify-app").change(function(e){
    row_id = $(e.target).parent().parent()[0].id
    status = e.target.value
    postModifyApplication(row_id,status)
})


// Post Delete Application
function postModifyApplication(row_id,status){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/apps/modify/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN,
                "row_id":row_id,
                "status":status},
          success: function(resultData){

          }
    });
}