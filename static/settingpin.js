document.getElementById('setPinForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission

    const newPin = document.getElementById('newPin').value;
    const confirmPin = document.getElementById('confirmPin').value;

    // Validate that both PINs match
    if (newPin === confirmPin) {
        localStorage.setItem('userPin', newPin); // Store the PIN in localStorage
        alert('PIN has been set successfully!'); // Handle successful setting of PIN
        window.location.href = 'login.html'; // Redirect to the login page
    } else {
        document.getElementById('set-error-message').textContent = 'PINs do not match. Please try again.';
    }
});