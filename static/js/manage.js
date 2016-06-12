/**
 * Created by Johnny on 6/11/16.
 */

$( "#dialog" ).dialog({
    autoOpen: false,
    buttons: [{text: "Cancel","class": 'btn btn-success',click: function() {$( "#dialog" ).dialog( "close" );}},
        {text: "Delete","class":'btn btn-danger',click: function() { postData(); $( "#dialog" ).dialog( "close" );}}, ]
});



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

$( "#opener" ).click(function() {
  $( "#dialog" ).dialog( "open" );
});