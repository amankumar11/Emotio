const dashboardbtn = document.getElementById('dashboardbtn');
const aboutusbtn = document.getElementById('aboutusbtn');
const logoutbtn = document.getElementById('logoutbtn');

dashboardbtn.addEventListener('click', (e) => {
    e.preventDefault();
    dashboardbtn.style.backgroundColor="#19052D";
    aboutusbtn.style.backgroundColor="#3B304C";
    logoutbtn.style.backgroundColor="#3B304C";
});

aboutusbtn.addEventListener('click', (e) => {
    e.preventDefault();
    aboutusbtn.style.backgroundColor="#19052D";
    dashboardbtn.style.backgroundColor="#3B304C";
    logoutbtn.style.backgroundColor="#3B304C";
});