document.addEventListener('DOMContentLoaded', function() {
    // Управление правой панелью профиля
    const profileButton = document.getElementById('profileButton');
    const closeProfile = document.getElementById('closeProfile');
    const profileSidebar = document.getElementById('profileSidebar');

    if (profileButton && profileSidebar) {
        profileButton.addEventListener('click', function() {
            profileSidebar.classList.add('show');
        });
    }

    if (closeProfile && profileSidebar) {
        closeProfile.addEventListener('click', function() {
            profileSidebar.classList.remove('show');
        });
    }

    // Закрытие профиля при клике вне панели
    document.addEventListener('click', function(e) {
        if (profileSidebar && !profileSidebar.contains(e.target) && e.target.id !== 'profileButton') {
            profileSidebar.classList.remove('show');
        }
    });
});