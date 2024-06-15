document.addEventListener('DOMContentLoaded', () => {
    const bell = document.querySelector('.notification-bell');
    const dropdown = document.querySelector('.notification-dropdown');

    bell.addEventListener('click', () => {
        dropdown.style.display = dropdown.style.display === 'block' ? 'none' : 'block';
    });

    document.querySelectorAll('.notification-dropdown .close').forEach(closeButton => {
        closeButton.addEventListener('click', (e) => {
            const li = e.target.closest('li');
            li.remove();
            updateNotificationCount();
        });
    });

    function updateNotificationCount() {
        const count = document.querySelectorAll('.notification-dropdown li').length;
        const notificationCountElement = document.querySelector('.notification-count');
        notificationCountElement.textContent = count;
        if (count === 0) {
            notificationCountElement.style.display = 'none';
            dropdown.style.display = 'none';
        } else {
            notificationCountElement.style.display = 'block';
        }
    }

    updateNotificationCount();
});



document.getElementById('openPopUp').addEventListener('click', function() {
    var sidebar = document.getElementById('notificationSidebar');
    sidebar.style.width = this.offsetWidth + 'px';
    sidebar.classList.toggle('open');
});

document.querySelectorAll('.close-btn').forEach(function(btn) {
    btn.addEventListener('click', function() {
        var li = this.parentElement;
        li.parentElement.removeChild(li);
    });
});




