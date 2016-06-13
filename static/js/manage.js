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
//$( ".datepicker" ).datepicker();

$( ".datepicker").click(function(e){
    $(e.target).datepicker()
})
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


// Post Modify Application
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


/**
 *
 * Education Records
 *
 * */


// Plus Button onClicks

$( "#add-cprog" ).click(function() {
  $( "#form-cprog" ).show();
});

$( "#add-pprog" ).click(function() {
  $( "#form-pprog" ).show();
});

$( "#add-gre" ).click(function() {
  $( "#form-gre" ).show();
});

$( "#add-toefl" ).click(function() {
  $( "#form-toefl" ).show();
});


// Form Controls and Dialogs

// Post Delete GREScore
function postDeleteGREScore(){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/grescore/delete/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
          success: function(resultData){
                window.location.href = 'http://127.0.0.1:8000/GradMaze/accounts/manage/';
          }
    });
}

$( "#dialog-gre-delete" ).dialog({
    autoOpen: false,
    buttons: [
        {text: "Cancel",
        "class": 'btn btn-success',
        click: function() {
            $( "#dialog-gre-delete" ).dialog( "close" );
        }},
        {text: "Delete",
         "class":'btn btn-danger',
         click: function(e) {
             postDeleteGREScore()
         }
        }]
});

$("#delete-gre").click(function(e){
    $( "#dialog-gre-delete" ).dialog( "open" );

})


// Post Delete TOEFLScore
function postDeleteTOEFLScore(){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/toeflscore/delete/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
          success: function(resultData){
                window.location.href = 'http://127.0.0.1:8000/GradMaze/accounts/manage/';
          }
    });
}

$( "#dialog-toefl-delete" ).dialog({
    autoOpen: false,
    buttons: [
        {text: "Cancel",
        "class": 'btn btn-success',
        click: function() {
            $( "#dialog-toefl-delete" ).dialog( "close" );
        }},
        {text: "Delete",
         "class":'btn btn-danger',
         click: function(e) {
             postDeleteTOEFLScore()
         }
        }]
});

$("#delete-toefl").click(function(e){
    $( "#dialog-toefl-delete" ).dialog( "open" );

})


// Post Delete Previous Program
function postDeletePrevProg(){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/prevprogram/delete/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
          success: function(resultData){
                window.location.href = 'http://127.0.0.1:8000/GradMaze/accounts/manage/';
          }
    });
}

$( "#dialog-pprog-delete" ).dialog({
    autoOpen: false,
    buttons: [
        {text: "Cancel",
        "class": 'btn btn-success',
        click: function() {
            $( "#dialog-pprog-delete" ).dialog( "close" );
        }},
        {text: "Delete",
         "class":'btn btn-danger',
         click: function(e) {
             postDeletePrevProg()
         }
        }]
});


$("#delete-pprog").click(function(e){
    $( "#dialog-pprog-delete" ).dialog( "open" );
})






// Post Delete Current Program
function postDeleteCurrProg(){
    $.ajax({
          type: "POST",
          url: "/GradMaze/accounts/currprogram/delete/",
          data:{csrfmiddlewaretoken: window.CSRF_TOKEN},
          success: function(resultData){
                window.location.href = 'http://127.0.0.1:8000/GradMaze/accounts/manage/';
          }
    });
}

$( "#dialog-cprog-delete" ).dialog({
    autoOpen: false,
    buttons: [
        {text: "Cancel",
        "class": 'btn btn-success',
        click: function() {
            $( "#dialog-cprog-delete" ).dialog( "close" );
        }},
        {text: "Delete",
         "class":'btn btn-danger',
         click: function(e) {
             postDeleteCurrProg()
         }
        }]
});


$("#delete-cprog").click(function(e){
    $( "#dialog-cprog-delete" ).dialog( "open" );
})