from django.shortcuts import render

# Create your views here.


def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=77AA9E6C-1F93-4D75-BE86-02C5B2019D61")

        try:
            api = json.loads(api_request.content)
        except:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risks."
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = "(51-100) Air Quality is acceptable; however, for some pollutants there may be a moderate heath concern for a very small number of people who are unusually sensitive to air pollution"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description = '(101-150) Air Quality is unhealthy for children, old people and people with diseases'
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = '(151-200) Unhealthy for people with lung diseases'
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "(201-250) Air Quality is considered unhealthy, and air pollution poses risks"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description = "(251-300) Air Quality is considered hazardous stay at home"
        else:
            pass
        return render(request, 'weather/home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})

    else:
        api_request = requests.get(
            "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=77AA9E6C-1F93-4D75-BE86-02C5B2019D61")

        try:
            api = json.loads(api_request.content)
        except:
            api = "Error..."

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "(0-50) Air Quality is considered satisfactory, and air pollution poses little or no risks."
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = "(51-100) Air Quality is acceptable; however, for some pollutants there may be a moderate heath concern for a very small number of people who are unusually sensitive to air pollution"
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description = '(101-150) Air Quality is unhealthy for children, old people and people with diseases'
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = '(151-200) Unhealthy for people with lung diseases'
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "(201-250) Air Quality is considered unhealthy, and air pollution poses risks"
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description = "(251-300) Air Quality is considered hazardous stay at home"
        else:
            pass
        return render(request, 'weather/home.html', {'api': api, 'category_description': category_description, 'category_color': category_color})
