document.getElementById("back").addEventListener('click', () => {
    window.electronAPI.loadHTML('index')
})

// setTimeout(() => {
//     chartList = window.electronAPI.loadUserData()['ipcData']
    
//     var chart = anychart.column()

//     // Set chart data
//     chart.column(chartList)

//     chart.title("Projected Carbon Emissions")

//     // Set chart axes titles
//     chart.xAxis().title("Non-Renewable Energy Emitted")
//     chart.yAxis().title("Months")

//     // Draw the chart
//     chart.container("chart")
//     chart.draw();
// }, 1500)
  
  setTimeout(() => {
    anychart.onDocumentReady(function () {
        // data
        data = anychart.data.set([
          {x: 1, value: 10},
          {x: 2, value: 2},
          {x: 3, value: 15},
          {x: 4, value: 10},
          {x: 5, value: 15}
        ]);

        data3 = anychart.data.set([
            {x: 1, value: 30},
            {x: 2, value: 20},
            {x: 3, value: 10},
            {x: 4, value: 80},
            {x: 5, value: 43}
          ]);
      
        // set chart type
        var chart = anychart.area();

        chart.animation(true);
      
        chart.title("Append Point Demo");
      
        // configure the main y-scale
        var yScale1 = anychart.scales.linear();
        yScale1.maximum(1000);
        yScale1.minimum(-1000);

        // configure the main y-axis
        chart.yAxis(0);

        // set data
        chart.splineArea(data);

        chart.splineArea(data3);

        chart.yScale(yScale1);
    

        // set container and draw chart
        chart.container("chart").draw();
      });

      newIndex = 6
      start = 50;
      start3 = 50;
      
      // function, if listener triggers
      function addPoint() {
        // first index for new point
      
        if (newIndex > 50) {
            data.remove(0)
            data3.remove(0)
        }

        if (Math.floor((Math.random() * 4) + 1) < 4) {
            start += Math.floor((Math.random() * 15) + 1)
        } else{
            start -= Math.floor((Math.random() * 15) + 1)
        }

        // append data
        data.append({
      
          // x value
          x: newIndex,
      
          // random value from 1 to 100
          value : start
        })

        if (Math.floor((Math.random() * 4) + 1) < 4) {
            start3 -= Math.floor((Math.random() * 15) + 1)
        } else{
            start3 += Math.floor((Math.random() * 15) + 1)
        }

        data3.append({
      
            // x value
            x: newIndex,
        
            // random value from 1 to 100
            value : start3
          })

        newIndex++
      };

    // Update the chart every second (example)
    setInterval(addPoint, 100);
  }, 1500)
