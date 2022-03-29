function setCookie(cname, cvalue, exdays) {
    const d = new Date();
    d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
    let expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

if (localStorage.getItem('token') == undefined) {
    //window.location.href = '/login'
    //console.log(location.search());
} else {
    setCookie('token', localStorage.getItem('token'))
    window.location.replace('/game')
}