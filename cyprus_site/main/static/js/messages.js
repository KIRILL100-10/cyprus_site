document.addEventListener("DOMContentLoaded", () => {
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.animation = "fadeout 0.5s forwards";
            setTimeout(() => alert.remove(), 500);
        }, 5000);
    });
});
