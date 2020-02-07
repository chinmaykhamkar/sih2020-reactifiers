function login() {
    console.log('inside function');
    var username = document.getElementById('login').value;
    var password = document.getElementById('password').value;
    axios.post('http://127.0.0.1:8000/user/farmer_login/', {
            username: username,
            password: password
        })
        .then(function(data) {
            console.log(data.data.valid);
            window.sessionStorage.setItem('check', data.data.name);
            if (data.data.valid === 'true') {

                window.location.href = 'dashboard.html';
            } else {
                alert('wrong passsword');
                window.location.href = 'login.html';

            }
        })

}