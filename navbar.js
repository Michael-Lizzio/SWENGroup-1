
const navbarContainer = document.getElementById('navbar-container');
fetch('navbar.html')
    .then(response => response.text())
    .then(data => {
        navbarContainer.innerHTML = data;
    })
    .catch(error => console.error('Error fetching navbar HTML:', error));

    