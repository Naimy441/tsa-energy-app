window.electronAPI.getPythonData('testRunner', 'chartList', jsonData)
setTimeout(() => {
    chartList = window.electronAPI.loadChartData()['chartList']
}, 750)