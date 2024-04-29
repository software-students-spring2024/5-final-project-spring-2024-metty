$(document).ready(function(){
    $('#activityBtn').click(function(){
        // AJAX request to fetch activity data
        $.ajax({
            url: '/activity-data',
            type: 'GET',
            success: function(response){
                $('#activityData').html(response);
                $('#popup').show();
            }
        });
    });

    // Close popup when close button is clicked
    $('.close').click(function(){
        $('#popup').hide();
    });
});
