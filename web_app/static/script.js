
$(document).ready(function(){
    $('#activityBtn').click(function(){
        $.ajax({
            url: '/activity-data',
            type: 'GET',
            success: function(response){
                $('#hoursWorked').text(response.hours_week);
                $('#daysWorked').text(response.days);
                $('#popup').show();

                // Close popup when clicking outside
                $(document).mouseup(function(e) {
                    var popupContent = $(".popup-content");
                    if (!popupContent.is(e.target) && popupContent.has(e.target).length === 0) {
                        $('#popup').hide();
                    }
                });
    
                // Render charts asynchronously after showing the popup
                setTimeout(function() {
                    drawChart('dayHoursChart', response.day_hours);
                }, 0);
            }
        });
    });

    $('.close-activity').click(function(){
        $('#popup').hide();
    });
});

function drawChart(canvasId, data) {
    var labels = Object.keys(data);
    var values = Object.values(data);

    var ctx = document.getElementById(canvasId).getContext('2d');
    var chart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Data',
                data: values,
                backgroundColor: 'rgba(191, 176, 173, 1)',
                pointBackgroundColor: 'rgba(250, 250, 250, 1)',
            }]
        },
        options: {
            scales: {
                x: {
                    grid: {
                        color: 'rgba(70, 51, 49, 0.2)', // X-axis gridline color
                        borderColor: 'rgba(70, 51, 49, 1)', // X-axis border color
                        borderWidth: 20 // X-axis border width
                    }
                },
                y: {
                    grid: {
                        beginAtZero: true,
                        color: 'rgba(70, 51, 49, 0.2)', // Y-axis gridline color
                        borderColor: 'rgba(70, 51, 49, 1)', // Y-axis border color
                        borderWidth: 20 // Y-axis border width
                    }
                }
            }
        }
    });
}
