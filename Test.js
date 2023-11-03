
function btnOnClick() {
    let btn = document.getElementById('btn');
    let btnClick = document.getElementById('btnClick');

    if (btnClick.display == 'none') {
        btnClick.display = 'block';
        btnClick.style.display = "none";
    } else {
        btnClick.display = 'none';
        btnClick.style.display = "block";
    }

}