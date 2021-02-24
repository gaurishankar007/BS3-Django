//selecting HTML elements
//actions/events
//set or get content, attribute, style
document.getElementsByClassName("test")[0].innerHTML = "<i>Hello<i> Everyone!";
document.getElementsByClassName("test")[0].align = "center";
document.getElementsByClassName("test")[0].setAttribute("class", "my_class");
document.getElementsByClassName("my_class")[0].getAttribute("class");
document.getElementsByClassName("my_class")[0].style.color = "red";

var a = 10;
b = 20;
let c = 30;

myFun = () => // Different way to call a function
  {
    let z = 100;
    if (z == 100);
    {
      let x = 555;
      var y = 111;
    }
  }

  // JQuery selector;
  $(window).scroll(function() {
    var height = $(window).scrollTop();

    if(height  > some_number) {
        // do something
    }
  });
  $(document).ready(function(){

    $('.my_class').click(function(){
      $(this).html('From JQuery');
      $(this).attr('align', 'right');
      $(this).css('color', 'blue');
    });

    $('#my_btn').click(function(){
      alert($('input[name=username]').val())
    })

    var list=[];
    $('input[type="checkbox"]').click(function() {
      if (this.checked) {
        list.push($(this).val())
      }
      else{
        list.splice(list.indexOf($(this).val()), 1)
      }  
      console.log(list);     
    });
  
    $('input[name=show_result]').hide();
    $('input[name=remove_result]').hide();
    $('#result').hide();
    $('input[name=submit]').click(() => {
      $('input[name=show_result]').show();
      var Hobbies='';
      var Hobby=$('input[name=hob]');
      for(i=0; i<Hobby.length; i++)
      {
          if(Hobby[i].checked)
          {
              Hobbies+=Hobby[i].value+",";
          }
      }
      console.log(Hobbies)
      $('#name').html("<b>Name:</b> "+$('input[name=name]').val());
      $('#gender').html("<b>Gender:</b> "+$('input[name=gender]:checked').val());
      $('#hobbies').html("<b>Hobbies:</b> "+Hobbies);
      $('#dob').html("<b>DOB:</b> "+$('input[name=dob]').val());
      $('#contact').html("<b>Contact:</b> "+$('input[name=contact]').val());
      $('#country').html("<b>Country:</b> "+$('select.country').children("option:selected").val());
      $('#email').html("<b>Email:</b> "+$('input[name=email]').val());
    }) 

    $('input[name=show_result]').click(() => {
      $('input[name=show_result]').hide();
      $('#result').show();
      $('input[name=remove_result]').show();
    })

    $('input[name=remove_result]').click(() => {
      $('input[name=remove_result]').hide();
      $('#result').hide();
    });
  });