document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // flash messages functionality
    var cardButtons = document.querySelectorAll('.card-alert > button');
    for (var i = 0; i < cardButtons.length; i++) {
        cardButtons[i].addEventListener('click', function () {
            var cardAlert = this.closest('div.card-alert');
            if (cardAlert) {
                cardAlert.style.transition = 'opacity 0.5s';
                cardAlert.style.opacity = '0';
                setTimeout(function () {
                    cardAlert.style.display = 'none';
                }, 500); // 0.5s transition duration
            }
        });
    }

    // datepicker initialization
    let datepicker = document.querySelectorAll('.datepicker');
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        i18n: {done: "Select"}
    });

    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // Modals for note deletion
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);
});