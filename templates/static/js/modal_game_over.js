// Get the modal
var modal1 = document.getElementById("game_over");


// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal1) {
        modal1.style.display = "none";
        window.location.reload()
    }
}


//--------------------------------------------------------------