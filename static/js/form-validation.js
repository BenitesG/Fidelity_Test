document.addEventListener('DOMContentLoaded', function() {

    const passwordInput = document.getElementById('id_password1');
    const confirmPasswordInput = document.getElementById('id_password2');
    
    const lengthRule = document.getElementById('length');
    const uppercaseRule = document.getElementById('uppercase');
    const numberRule = document.getElementById('number');
    const specialRule = document.getElementById('special');
    const confirmFeedback = document.getElementById('confirm-password-feedback');

    function validateRule(element, isValid) {
        if (isValid) {
            element.classList.remove('invalid');
            element.classList.add('valid');
        } else {
            element.classList.remove('valid');
            element.classList.add('invalid');
        }
    }

    passwordInput.addEventListener('input', function() {
        const password = passwordInput.value;

        validateRule(lengthRule, password.length >= 8);

        validateRule(uppercaseRule, /[A-Z]/.test(password));

        validateRule(numberRule, /[0-9]/.test(password));

        validateRule(specialRule, /[\W_]/.test(password));

        validateConfirmPassword();
    });

    function validateConfirmPassword() {
        const password = passwordInput.value;
        const confirmPassword = confirmPasswordInput.value;

        if (confirmPassword.length === 0) {
            confirmFeedback.textContent = ''; 
            return;
        }

        if (password === confirmPassword) {
            confirmFeedback.textContent = 'As senhas conferem!';
            confirmFeedback.className = 'valid';
        } else {
            confirmFeedback.textContent = 'As senhas não conferem.';
            confirmFeedback.className = 'invalid';
        }
    }

    confirmPasswordInput.addEventListener('input', validateConfirmPassword);
});