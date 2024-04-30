document.addEventListener('DOMContentLoaded', function () {
    var profileIcon = document.getElementById('profile-icon');
    var profileMenu = document.getElementById('profile-menu');

    // Fonction pour basculer l'affichage du menu déroulant
    function toggleProfileMenu() {
        profileMenu.classList.toggle('show');
    }

    // Ajout d'un écouteur d'événements pour le clic sur l'icône de profil
    profileIcon.addEventListener('click', toggleProfileMenu);

    // Ajout d'un écouteur d'événements pour masquer le menu lorsque l'utilisateur clique en dehors de celui-ci
    document.addEventListener('click', function (event) {
        if (!profileIcon.contains(event.target) && !profileMenu.contains(event.target)) {
            profileMenu.classList.remove('show');
        }
    });
});