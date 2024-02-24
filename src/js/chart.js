document.getElementById("back").addEventListener('click', () => {
    window.electronAPI.loadHTML('index')
})

setTimeout(() => {
    chartList = window.electronAPI.loadUserData()['ipcData']
    
    var chart = anychart.column()

    // Set chart data
    chart.column(chartList)

    chart.title("Projected Carbon Emissions")

    // Set chart axes titles
    chart.xAxis().title("Non-Renewable Energy Emitted")
    chart.yAxis().title("Months")

    // Draw the chart
    chart.container("chart")
    chart.draw();
}, 1500)

