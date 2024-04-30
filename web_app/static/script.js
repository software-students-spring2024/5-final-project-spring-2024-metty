
$(document).ready(function(){
    $('#activityBtn').click(function(){
        $.ajax({
            url: '/activity-data',
            type: 'GET',
            success: function(response){
                $('#hoursWorked').text(response.hours_week);
                $('#daysWorked').text(response.days);
                // Draw chart for day_hours
                //drawChart('dayHoursChart', response.day_hours);
                // Draw chart for activity_data
                //drawChart('activityDataChart', response.activity_data);
                $('#popup').show();
            }
        });
    });

    $('.close').click(function(){
        $('#popup').hide();
    });
});

/*
function drawChart(canvasId, data) {
    var labels = Object.keys(data);
    var values = Object.values(data);

    var ctx = document.getElementById(canvasId).getContext('2d');
    var chart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Data',
                data: values,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
}
*/