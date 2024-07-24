document.getElementById("deleteForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent the form from submitting normally
    
    Swal.fire({
        title: 'Are you sure you want to delete the Task?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: 'red',
        cancelButtonColor: 'rgb(45, 45, 119)',
        confirmButtonText: 'Yes, delete it!',
        cancelButtonText: 'Cancel' // Add cancel button text
    }).then((result) => {
        if (result.isConfirmed) {
            // Submit the form using AJAX
            fetch(document.getElementById("deleteForm").action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value
                }
            })
            .then(response => {
                if (response.ok) {
                    Swal.fire({
                        title: 'Success!',
                        text: 'Task deleted successfully.',
                        icon: 'success'
                    }).then(() => {
                        window.location.href = "{% url 'task_list' %}";
                    });
                } else {
                    throw new Error('Something went wrong!');
                }
            })
            .catch(error => {
                Swal.fire({
                    title: 'Error!',
                    text: error.message,
                    icon: 'error'
                });
            });
        }
    });
});