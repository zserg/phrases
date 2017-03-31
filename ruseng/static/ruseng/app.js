console.log("Hello");
var count = 3;
console.log("0");
var state = 'show';

jQuery.fn.visible = function() {
      return this.css('visibility', 'visible');
};

jQuery.fn.invisible = function() {
      return this.css('visibility', 'hidden');
};

function get_data (){
    console.log('get_data')
    $('#answer').invisible();
    $.get({url: 'get_data/',
           data: {'count': count},
           success: new_text
          });
}

function new_text (data) {
    console.log('new_text');
    $('#answer').invisible();
    text = "";
    for (let item of data.data.one) {
      text+=("<p>"+item+"</p>");
    }
    $('#question').html(text);
    text = "";
    for (let item of data.data.two) {
      text+=("<p>"+item+"</p>");
    }
    $('#answer').html(text);
    $('#answer-button').text('Show');
}


function clickHandler (num) {
    console.log('show_answer');
    if (state == 'show') {
      $('#answer').visible();
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
