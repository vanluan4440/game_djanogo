function loading() {
    console.log(window.localStorage.getItem('key'));
    if (window.localStorage.getItem('key') == 'true') {
        document.getElementById('key').style.display = 'block'
    } else {
        document.getElementById('key').style.display = 'none'
    }
}
window.addEventListener('click', () => {
    document.getElementById('key').style.display = 'none'
    window.localStorage.setItem('key', false)

})