// Injects a recieved JSON element from a GET to the app
function fetchDataElement(destinationContainerId, uri) {
    fetch(uri)
        .then(response => response.json())
        .then(data => {
            document.getElementById(destinationContainerId).innerHTML = data.html;
        })
        .catch(error => {
            console.error('Error fetching additional content:', error);
            document.getElementById(destinationContainerId).innerHTML = '<p>Could not fetch.</p>'
        });
}