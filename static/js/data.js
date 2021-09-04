let myChart = document.getElementById("pie-chart").getContext('2d');


let massPopChart = new Chart(myChart, {
    type: 'doughnut', //bar, horizontal-bar, pie, doughnut, line, radar, polarArea
    data: {
        labels: ['Happy', 'Sad', 'Angry'],
        datasets: [{
            label:'mood index',
            data: [
                70,
                25,
                5
            ],
            //backgroundColor:'green'
            backgroundColor:[
                '#de288f',
                '#f07881',
                '#e3b025'

            ],
            borderWidth:1,
            borderColor:'#623b96',
            hoverBorderColor:'#623b96',
            hoverBorderWidth:4

        }]
    }, 
    options:{}
});