
$(document).ready(function(){
    $('#activityBtn').click(function(){
        $.ajax({
            url: '/activity-data',
            type: 'GET',
            success: function(response){
                $('#hoursWorked').text(response.hours_week);
                $('#daysWorked').text(response.days);
                $('#popup').show();

                // Sort the keys of the data object to match the order of days
                var sortedData = {};
                ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'].forEach(function(day) {
                    sortedData[day] = response.day_hours[day] || 0;
                });
    
                // Render charts asynchronously after showing the popup
                setTimeout(function() {
                    drawChart('dayHoursChart', sortedData);
                }, 0);
            }
        });
    });

    $('.close').click(function(){
        $('#popup').hide();
    });

    // Close the popup when clicking outside of it
    $(window).click(function(event) {
        if (event.target == $('#popup')[0]) {
            $('#popup').hide();
        }
    });
});

function drawChart(canvasId, data) {
    var values = Object.values(data);
    var labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'];

    var ctx = document.getElementById(canvasId).getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Time (hours)',
                data: values,
                backgroundColor: 'rgba(191, 176, 173, 1)',
                pointBackgroundColor: 'rgba(250, 250, 250, 1)',
            }]
        },
        options: {
            scales: {
                // axes styling
                x: {
                    grid: {
                        beginAtZero: true,
                        color: 'rgba(70, 51, 49, 0.2)',
                        borderColor: 'rgba(70, 51, 49, 1)',
                        borderWidth: 20
                    },
                    indexAxis: 'x'
                },
                y: {
                    grid: {
                        beginAtZero: true,
                        color: 'rgba(70, 51, 49, 0.2)',
                        borderColor: 'rgba(70, 51, 49, 1)',
                        borderWidth: 20
                    }
                }
            }
        }
    });
}
