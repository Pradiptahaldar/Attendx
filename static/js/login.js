// ======================================
// Password Show / Hide
// ======================================

const password = document.getElementById("password");
const togglePassword = document.getElementById("togglePassword");

if (togglePassword && password) {

    togglePassword.addEventListener("click", () => {

        if (password.type === "password") {

            password.type = "text";

            togglePassword.innerHTML =
                '<i class="bi bi-eye-slash-fill"></i>';

        }

        else {

            password.type = "password";

            togglePassword.innerHTML =
                '<i class="bi bi-eye-fill"></i>';

        }

    });

}


// ======================================
// Input Focus Animation
// ======================================

const inputs = document.querySelectorAll(".form-control");

inputs.forEach(input => {

    input.addEventListener("focus", () => {

        input.parentElement.style.boxShadow =
            "0 0 0 4px rgba(37,99,235,.15)";

    });

    input.addEventListener("blur", () => {

        input.parentElement.style.boxShadow = "none";

    });

});


// ======================================
// Login Button Animation
// ======================================

const form = document.querySelector("form");
const loginButton = document.querySelector(".login-btn");

form.addEventListener("submit", function (e) {

    e.preventDefault();

    loginButton.disabled = true;

    loginButton.innerHTML = `
        <span class="spinner-border spinner-border-sm me-2"></span>
        Signing In...
    `;

    setTimeout(() => {

        loginButton.disabled = false;

        loginButton.innerHTML =
            '<i class="bi bi-box-arrow-in-right me-2"></i>Login';

        // Temporary redirect
        window.location.href = "/dashboard";

    }, 1500);

});


// ======================================
// Press Enter
// ======================================

document.addEventListener("keydown", function(e){

    if(e.key==="Enter"){

        form.requestSubmit();

    }

});


// ======================================
// Fade In
// ======================================

window.addEventListener("load",()=>{

    document.body.style.opacity="1";

});