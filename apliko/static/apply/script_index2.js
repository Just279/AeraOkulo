

document.addEventListener('DOMContentLoaded', () => {
    const bell = document.querySelector('.notification-bell');
    const dropdown = document.querySelector('.notification-dropdown');

    bell.addEventListener('click', () => {
        if (dropdown.style.display === 'block') {
        $.ajax({
	    url: '/apliko/',     
	    method: 'get',              
	    data: {text: '!'},     
	    success: function(data){

	    }
	});
	dropdown.style.display ='none'
	} else {
	dropdown.style.display ='block'
	}
    });

    document.querySelectorAll('.notification-dropdown .close').forEach(closeButton => {
        closeButton.addEventListener('click', (e) => {
            const li = e.target.closest('li');
            li.remove();
            updateNotificationCount();
        });
    });

    function updateNotificationCount() {
        const count = document.querySelectorAll('.notification-dropdown-ul li').length;
        const notificationCountElement = document.querySelector('.notification-count');
        notificationCountElement.textContent = count;
        if (count === 0) {
            notificationCountElement.style.display = 'none';
            dropdown.style.display = 'none';
        } else {
            notificationCountElement.style.display = 'block';
            
        }
    }

    // Initialize the notification count on page load
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

