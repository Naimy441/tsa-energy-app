document.getElementById('begin').addEventListener('click', function(event) {
    userData = window.electronAPI.loadUserData()

    username = document.getElementById('name').value
    email = document.getElementById('email').value

    if (username != "" && email.includes("@") && email.includes(".")) {
        userData['startComplete'] = true
        userData['userData']['name'] = username
        userData['userData']['email'] = email 
    }

    window.electronAPI.saveUserData(JSON.stringify(userData))
    window.electronAPI.loadHTML('home')
})