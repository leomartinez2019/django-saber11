var ctx = document.getElementById("myChart").getContext('2d');
var myChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ["Inglés", "Ciencias", "Matemáticas", "Sociales y Ciudadanas", "Lectura"],
        datasets: [{
            label: 'Promedio',
            data: [datta.promingles, datta.promcienciasnaturales, datta.prommatematica, datta.promsocialesyciudadanas, datta.promlecturacritica],
            backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(54, 162, 235, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    //beginAtZero:true
                    suggestedMin: 30
                }
            }]
        }
    }
});
