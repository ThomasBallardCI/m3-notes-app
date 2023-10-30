document.addEventListener('DOMContentLoaded', function () {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    // flash messages functionality
    var cardButtons = document.querySelectorAll('.card-alert > button');
    for (var i = 0; i < cardButtons.length; i++) {
        cardButtons[i].addEventListener('click', function () {
            // Hide the flash message card
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

    // Collapsibles initialization
    let collapsibles = document.querySelectorAll('.collapsible');
    M.Collapsible.init(collapsibles);

    // Modals for note deletion;
    let modals = document.querySelectorAll('.modal');
    M.Modal.init(modals);

    // Delete specific notes based on note.id
    // Select all elements with the class 'delete-button'
    let deleteButtons = document.querySelectorAll('.delete-button');

    // Iterate through each delete button
    deleteButtons.forEach(button => {
        // Add a click event listener to each delete button
        button.addEventListener('click', function () {
            // Get the specific note ID associated with the delete button
            let noteId = this.getAttribute('data-note-id');

            // Access the modal associated with the specific note ID
            let modal = M.Modal.getInstance(document.querySelector(`#modal${noteId}`));
            modal.open(); // Open the modal for confirmation

            // Locate the confirmation button within the modal
            let confirmButton = document.querySelector(`#confirm-delete-${noteId}`);

            // Add a click event listener to the confirmation button
            confirmButton.addEventListener('click', function () {
                // Send a GET request to the server to delete the note with the given noteId
                fetch(`/delete_note/${noteId}`, {
                    method: 'GET'
                }).then(response => {
                    // Check if the deletion request was successful
                    if (response.ok) {
                        window.location.href = 'notes.html'; // Redirect to the notes page after successful deletion
                    } else {
                        console.error('Failed to delete the note.');
                    }
                }).catch(error => {
                    console.error('Error:', error); // Log any errors encountered during the deletion process
                });
            });
        });
    });
});