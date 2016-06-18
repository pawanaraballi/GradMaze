/**
 * Created by Johnny on 6/18/16.
 */






// Post Delete Current Program
function postDeleteCurrProg(){
    $.ajax({
          type: "POST",
          url: "/GradMaze/search/",
          data:{'field': $('#search_field').val(),
                'query_string':$('#search_bar').val() },
          success: function(resultData){
                window.location.href = 'http://127.0.0.1:8000/GradMaze/accounts/manage/';
          }
    });
}