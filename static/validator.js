function validate(event) {
    // alert("Connected");
    const name = document.getElementById("name").value
    const mobile = document.getElementById("mobile").value
    const email = document.getElementById("email").value
    const password = document.getElementById("password").value
    const gender = document.getElementsByName("gender")
    const dob = document.getElementById("dob").value
    const address = document.getElementById("address").value

    const name_error = document.getElementById("name_error")
    const mobile_error = document.getElementById("mobile_error")
    const email_error = document.getElementById("email_error")
    const password_error = document.getElementById("password_error")
    const gender_error = document.getElementById("gender_error")
    const date_error = document.getElementById("date_error")
    const address_error = document.getElementById("address_error")

    var error = false

    

    // name check


    
    const ifNum = name.match(/[0-9]/)
    function hasWhiteSpace() {
        return name.includes(' ');
    }

    if (name == "") {
        name_error.innerHTML = "Name is required"
        error = true
    } else if (!hasWhiteSpace()) {
        name_error.innerHTML = "Enter proper Full Name"
        error = true
    } else if (ifNum) {
        name_error.innerHTML = "Name can't contain Numbers"
        error = true
    } else {
        name_error.innerHTML = ""
    }



    if (mobile === "") {
        mobile_error.innerHTML = "Mobile number is required"
        error = true
    } else if (isNaN(mobile) || mobile.length != 10) {
        mobile_error.innerHTML = "Mobile number should contain 10 digit"
        error = true
    } else {
        mobile_error.innerHTML = ""
    }


    let atPos = email.indexOf("@")
    let dotPos = email.lastIndexOf(".")
    if (email === "") {
        email_error.innerHTML = "Email is required"
        error = true
    } else if (atPos < 4 || dotPos - atPos < 4 || dotPos == email.length - 1) {
        email_error.innerHTML = "Please enter a valid Email Id."
        error = true
    } else {
        email_error.innerHTML = ""
    }

    if (password === "") {
        password_error.innerHTML = "Password required"
        error = true
    } else if (!password.match(/[a-z]/)) {
        password_error.innerHTML = "Password must contain one Lower case."
        error = true
    } else if (!password.match(/[A-Z]/)) {
        password_error.innerHTML = "Password must contain One Upper Case."
        error = true
    } else if (!password.match(/[0-9]/)) {
        password_error.innerHTML = "Password must contain one Digit."
        error = true
    } else if (!password.match(/[@#$%&!]/)) {
        password_error.innerHTML = "Password must contain one special character."
        error = true
    } else if (password.length < 6 || password.length > 15) {
        password_error.innerHTML = "Password length must be between 6 to 15."
        error = true
    } else {
        password_error.innerHTML = ""
    }

    if (dob == "") {
        date_error.innerHTML = "Enter your Date of Birth"
        error = true
    } else {
        date_error.innerHTML = ""
    }

    if (address == "") {
        address_error.innerHTML = "Enter your curent address"
        error = true
    } else {
        address_error.innerHTML = ""
    }

    if (!gender[0].checked && !gender[1].checked) {
        gender_error.innerHTML = "Enter your gender"
        error = true
    } else {
        gender_error.innerHTML = ""
    }


    if (error) {
        event.preventDefault();
    }
}