document.getElementById("back").addEventListener('click', () => {
    window.electronAPI.loadHTML('home')
})

setTimeout(() => {
    ipcData = window.electronAPI.loadUserData()
    chartList1 = ipcData['ipcData1']
    chartList2 = ipcData['ipcData2']
    
    chart1 = anychart.area()
    chart2 = anychart.area()

    dict1 = []
    for (let i = 0; i < 5; i++) {
      dict1.push({x: chartList1[i][0], value: chartList1[i][1]})
    } 
    data1 = anychart.data.set(dict1)

    dict2 = []
    for (let i = 0; i < 5; i++) {
      dict2.push({x: chartList2[i][0], value: chartList2[i][1]})
    } 
    data2 = anychart.data.set(dict2)

    chart1.animation(true);
    chart2.animation(true);
      
        chart1.title("C02 Emissions per Year");
        chart2.title("Total C02 Emissions");

        // chart1.height = "500px"
        // chart2.height = "500px"
      
        // configure the main y-scale
        var yScale = anychart.scales.linear();
        yScale.maximum(1000);
        yScale.minimum(-1000);

        // configure the main y-axis
        chart1.yAxis(0);
        chart2.yAxis(0);

        // set data
        chart1.splineArea(data1);
        chart2.splineArea(data2);

        // chart1.yScale(yScale);
        // chart2.yScale(yScale);

        // set container and draw chart
        chart1.container("chart1").draw();
        chart2.container("chart2").draw();

      newIndex = 5

        function addPoint() {
          if (newIndex < 60) {
            // if (newIndex > 10) {
            //   data1.remove(0)
            //   data2.remove(0)
            // }

            data1.append({x: chartList1[newIndex][0], value: chartList1[newIndex][1]})
            data2.append({x: chartList2[newIndex][0], value: chartList2[newIndex][1]})

            newIndex++
          }
        }

        setInterval(addPoint, 100)
}, 1500)
  
  // setTimeout(() => {
  //   anychart.onDocumentReady(function () {
  //       // data
  //       data = anychart.data.set([
  //         {x: 1, value: 10},
  //         {x: 2, value: 2},
  //         {x: 3, value: 15},
  //         {x: 4, value: 10},
  //         {x: 5, value: 15}
  //       ]);

  //       data3 = anychart.data.set([
  //           {x: 1, value: 30},
  //           {x: 2, value: 20},
  //           {x: 3, value: 10},
  //           {x: 4, value: 80},
  //           {x: 5, value: 43}
  //         ]);
      
  //       // set chart type
  //       var chart = anychart.area();

  //       chart.animation(true);
      
  //       chart.title("Append Point Demo");
      
  //       // configure the main y-scale
  //       var yScale1 = anychart.scales.linear();
  //       yScale1.maximum(1000);
  //       yScale1.minimum(-1000);

  //       // configure the main y-axis
  //       chart.yAxis(0);

  //       // set data
  //       chart.splineArea(data);

  //       chart.splineArea(data3);

  //       chart.yScale(yScale1);
    

  //       // set container and draw chart
  //       chart.container("chart").draw();
  //     });

  //     newIndex = 6
  //     start = 50;
  //     start3 = 50;
      
  //     // function, if listener triggers
  //     function addPoint() {
  //       // first index for new point
      
  //       if (newIndex > 50) {
  //           data.remove(0)
  //           data3.remove(0)
  //       }

  //       if (Math.floor((Math.random() * 4) + 1) < 4) {
  //           start += Math.floor((Math.random() * 15) + 1)
  //       } else{
  //           start -= Math.floor((Math.random() * 15) + 1)
  //       }

        // // append data
        // data.append({
      
        //   // x value
        //   x: newIndex,
      
        //   // random value from 1 to 100
        //   value : start
        // })

  //       if (Math.floor((Math.random() * 4) + 1) < 4) {
  //           start3 -= Math.floor((Math.random() * 15) + 1)
  //       } else{
  //           start3 += Math.floor((Math.random() * 15) + 1)
  //       }

  //       data3.append({
      
  //           // x value
  //           x: newIndex,
        
  //           // random value from 1 to 100
  //           value : start3
  //         })

  //       newIndex++
  //     };

  //   // Update the chart every second (example)
  //   setInterval(addPoint, 100);
  // }, 1500)
