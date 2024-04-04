function getInfoNum(string) {
    if (string === "Natural gas") {
        return 1
    } else if (string === "Electricity") {
        return 2
    } else if (string === "Fuel oil or kerosene") {
        return 3
    } else if (string === "Propane") {
        return 4
    } else if (string === "Wood") {
        return 5
    }
}

username = window.electronAPI.loadUserData()['userData']['name']
document.getElementById('greeting').innerText = "Welcome back, " + username + "!"

document.getElementById("surveyForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    var formData = new FormData(this);
    var formValues = {};
    for (var pair of formData.entries()) {
        formValues[pair[0]] = pair[1];
    }

    userData = window.electronAPI.loadUserData()
    
    userData['Statistics']['Housing unit type'] = formValues['Housing unit type']
    userData['Statistics']['Year of construction'] = formValues['Year of construction']
    userData['Statistics']['Total square footage'] = formValues['Total square footage']
    userData['Statistics']['Number of household members'] = formValues['Number of household members']
    userData['Statistics']['2020 annual household income'] = formValues['2020 annual household income']
    userData['Statistics']['Payment method for energy bills'] = formValues['Payment method for energy bills']

    userData['Consumption information']['Space heating'] = [
        formValues['Space heating'],
        [formValues['Highest space heating month'], parseInt(formValues['Highest hours for space heating'])], 
        ['February', parseInt(formValues['Lowest hours for space heating'])]
    ]
    userData['Consumption information']['Water heating'] = [
        formValues['Water heating'],
        [formValues['Highest water heating month'], parseInt(formValues['Highest hours for water heating'])], 
        ['February', parseInt(formValues['Lowest hours for water heating'])]
    ]
    userData['Consumption information']['Air conditioning'] = [
        formValues['Air conditioning'],
        [formValues['Highest air conditioning month'], parseInt(formValues['Highest hours for air conditioning'])], 
        ['February', parseInt(formValues['Lowest hours for air conditioning'])]
    ]
    userData['Consumption information']['Refrigerators'] = [formValues['Refrigerators'], getInfoNum(formValues['Refrigerators'])]
    userData['Consumption information']['Other'] = [formValues['Other'], getInfoNum(formValues['Other'])]

    window.electronAPI.saveUserData(JSON.stringify(userData))
    window.electronAPI.getPythonData('testRunner', 'chartLists', JSON.stringify(userData))
    window.electronAPI.loadHTML('chart')
});