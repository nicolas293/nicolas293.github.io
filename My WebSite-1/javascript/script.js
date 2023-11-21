var modal = document.getElementById('myModal');
var btn = document.getElementById("onclickBtn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var modalM = document.getElementById('myModal-clok');
var btnC = document.getElementById("onOcnoClick");
var spanK = document.getElementsByClassName("close-4")[0];

btnC.onclick = function() {
    modalM.style.display = "block";
}

spanK.onclick = function() {
    modalM.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modalM) {
        modalM.style.display = "none";
    }
}

var modDocument = document.getElementById('myModDocument');
var btnDocument = document.getElementById("icor");
var spanDocument = document.getElementsByClassName("closeHeader-ur")[0];

btnDocument.onclick = function() {
    modDocument.style.display = "block";
}

spanDocument.onclick = function() {
    modDocument.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modDocument) {
        modDocument.style.display = "none";
    }
}

var modPeople = document.getElementById('myModPeople');
var btnPeople = document.getElementById("icor2");
var spanPeople = document.getElementsByClassName("closePeople-ur")[0];

btnPeople.onclick = function() {
    modPeople.style.display = "block";
}

spanPeople.onclick = function() {
    modPeople.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modPeople) {
        modPeople.style.display = "none";
    }
}


function btnOnclick() {
    {if(!document.getElementById('img')){var image=document.createElement('img');
    image.id="img";
    image.src="img/Test.jpg";
    document.body.appendChild(image)}}
}

function clearOnclick() {
    var elem = document.getElementById('img');
    elem.style.display = "none";
}

function nScresr() {
    var tag = document.createElement("p");
    var text = document.createTextNode("Nicolas");
    tag.id = 'poraGraw';
    text.id = 'itamScroll1';
    tag.appendChild(text);
    document.getElementById('itamScroll').appendChild(tag);

    var poraGraw = document.getElementById("poraGraw");
    var img = new Image();
    img.src = 'img/Nicolas.jpg';
    img.id = 'imgFoter';
    poraGraw = document.body.appendChild(img);

    var imgFoter = document.getElementById("imgFoter");
    imgFoter.style.display = "none";
}

function nScresrR() {
    var poraGraw = document.getElementById("poraGraw");
    poraGraw.remove();

    var imgFoter = document.getElementById("imgFoter");
    imgFoter.remove();
}

function igesClik() {
   var elem = document.createElement("img");
   elem.id = 'imgFego';
   elem.setAttribute("src", "img/2.jpg");
   document.getElementById("futerImg").appendChild(elem);
}

function igesRemuve() {
   var imgFego = document.getElementById("imgFego");
   imgFego.remove();
}

function telefonText() {
    var testTelefon = document.getElementById("teLefon");
}

function wrapUpdate() {
    window.location.reload()
}

  
