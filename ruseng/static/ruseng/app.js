console.log("Hello");
var count = 5;
console.log("0");
var state = 'show';

function get_data (){
    console.log('get_data')
    $('#answer').hide();
    $.get({url: 'get_data/',
           data: {'count': count},
           success: function (data){
              console.log('get_data - success');
              $('#answer').hide();
              $('#question').text(data.data.one);
              $('#answer').text(data.data.two);
              $('#answer-button').text('Show');
            }
    });
}

function clickHandler (num) {
    console.log('show_answer');
    if (state == 'show') {
      $('#answer').show();
      $('#answer-button').text('Next');
      state = 'next';
    }else{
      state = 'show';
      get_data();
   }
}


console.log("1");
$('#answer-button').click(clickHandler);
get_data()
