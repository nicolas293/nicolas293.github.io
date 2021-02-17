/*
function onclickOnClick() {
  var onlicks = document.getElementById('onlicks');
  var oncl2 = document.getElementsByClassName('oncl2'); 

  if(onlicks.style.display = "none"){
    onlicks.style.display = "inline";
    oncl2.style.background = "#333";
    onlicks.display = "none";
  } else {
    onlicks.style.display = "none";
    oncl2.style.background = "#ff6";
    onlicks.display = "inline";  
  } 

} 


function onClickButton() {
    var header = document.getElementById("header");
    var pr = document.getElementById("pr");
    var btn = document.getElementById("btn");

        if(header.style.display == "none") {   
            header.style.display = "inline";
            btn.innerHTML = "Меню. ";
            btn.style.color = "#ff6";
            pr.display = "none";  
        } else {
            header.style.display = "none";
            btn.innerHTML = "Главная: ";
            btn.style.color = "#fff";
            pr.display = "inline";         
        }   


    }

 btn.style.color = "#fff";
 btn.style.background = "#330";

function newNavSlca() {
  var newNav = document.getElementById('newNav');
  var silca = document.getElementById('silca');
  
  if(newNav.style.display == "none") {
    newNav.style.display = "inline";
    silca.display = "none";  
  } else {
    newNav.style.display = "none";
    silca.display = "inline";  
  }
}*/
 
function onClickButton() {
  var seltheme = document.getElementById("selcolor").value;
  var elem = document.getElementById("pcit");

            if(seltheme == "Red") {
              elem.style.backgroundColor = "red";
          } else {
            if(seltheme == "Green") {
              elem.style.backgroundColor = "green";
          } else {
            if(seltheme == "Blue") {
              elem.style.backgroundColor = "blue";
          } else {
            if(seltheme == "Black") {
              elem.style.backgroundColor = "black";
          } else {
            if(seltheme == "Antiquewhite") {
              elem.style.color = "antiquewhite";
              elem.style.background = "antiquewhite";
          } else {
            if(seltheme == "Black") {
              elem.style.color = "black"; 
          }     
        }  
      }
    }  
  }
}

}


function onClickBB1() {
    var btn = document.getElementById("btn");
    var pcit = document.getElementById("pcit");

      if(pcit.style.display == "none") {
        btn.display = "none";
        btn.innerHTML = "Скрыть";
        pcit.style.display = "inline";
      } else {
        btn.display = "inline";
        btn.innerHTML = "Паказать";
        pcit.style.display = "none";
      }

} 

function onClickAB2() {
  var pcit = document.getElementById("pcit");

  if(pcit.display == "none") {
    pcit.display = "none";
    pcit.style.color = "antiquewhite"; 
  } else {
    pcit.display = "inline";
    pcit.style.color = "black";
  }

  if(pcit.display == "none") {
    pcit.display = "inline";
    pcit.style.color = "antiquewhite"; 
  } else {
    pcit.display = "none";
    pcit.style.color = "black";
  } 

}
  
function onClickCB3() {
  var pil = document.getElementById("pil");

  if(pcit.display == "none") {
    pcit.display = "inline";
    pil.innerHTML = "Показать Фон";
    pcit.style.background = "#fff";
  } else {
    pcit.display = "none";
    pil.innerHTML = "Скрыть Фон";
    pcit.style.background = "red";
  }   
}

function clickOneClic() {
  var bil = document.getElementById("bil");
  
  if(bil.display == "none") {
      bil.display = "none";
      bil.innerHTML = "Изменениний Цвет Красный";
      bil.style.background = "red";
      bil.style.color = "black"; 
      bil.display = "inline";
    } else {  
      bil.display = "inline";
      bil.innerHTML = "Изменениний Цвет Синий";
      bil.style.background = "blue";
      bil.style.color = "#fff";
      bil.display = "none";
    }
}







