$(document).ready(function() {
    $('#uploadForm').on('submit', function(event){
        event.preventDefault();
        var form_data = new FormData(this);
        $.ajax({
            url: '/upload',
            method: 'POST',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                $('#uploadedFiles').html(data);
            }
        });
    });

    $(document).on('click', '.delete', function(){
        var docId = $(this).attr('id');
        $.ajax({
            url: '/delete/' + docId,
            method: 'POST',
            success: function(data) {
                $('#uploadedFiles').html(data);
            }
        });
    });

    $(document).on('click', '.view', function(){
        var docId = $(this).attr('id');
        $.ajax({
            url: '/view/' + docId,
            method: 'GET',
            success: function(data) {
                $('#viewModal .modal-body').html(data);
                $('#viewModal').modal('show');
            }
        });
    });
});