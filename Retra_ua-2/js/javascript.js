function openbox(id){
      display = document.getElementById(id).style.display;
      if(display=='none'){
         document.getElementById(id).style.display='block';
      }else{
         document.getElementById(id).style.display='none';
      }
  }
  


$(document).ready(function () {
    $('#content img').click(function () {
       var img = $(this);
       var src = img.attr('src');
       $("body").append("<div id='popup'>"+
         "<div id='popup_bg'></div>"+ 
         "<img src='"+src+"' id='popup_img' />"+"</div>");
       $("#popup").fadeIn(800);
       $("#popup_bg").click(function() {
         $("#popup").fadeOut(800);
         setTimeout(function() {
           $("#popup").remove(); 
         }, 800);
       }); 
         
    });

});


