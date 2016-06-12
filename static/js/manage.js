/**
 * Created by Johnny on 6/11/16.
 */

$( "#dialog" ).dialog({
    autoOpen: false,
    buttons: [{text: "Cancel","class": 'btn btn-success',click: function() {$( "#dialog" ).dialog( "close" );}},
        {text: "Delete","class":'btn btn-danger',click: function() {$( "#dialog" ).dialog( "close" );}}, ]
});


$( "#opener" ).click(function() {
  $( "#dialog" ).dialog( "open" );
});