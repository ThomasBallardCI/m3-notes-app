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

    // Modals for note deletion;
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);

    let deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function () {
            let noteId = this.getAttribute('data-note-id');

            let modal = M.Modal.getInstance(document.querySelector(`#modal${noteId}`));
            modal.open();

            let confirmButton = document.querySelector(`#confirm-delete-${noteId}`);
            confirmButton.addEventListener('click', function () {
                fetch(`/delete_note/${noteId}`, {
                    method: 'GET'
                }).then(response => {
                    if (response.ok) {
                        window.location.href = 'notes.html'; // Redirect to the notes page after successful deletion
                    } else {
                        console.error('Failed to delete the note.');
                    }
                }).catch(error => {
                    console.error('Error:', error);
                });
            });
        });
    });
});