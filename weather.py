from pyowm import OWM

owm=OWM("54da52a59ecdca96be90226eb2841719")
results=[]
def get_forecast(lat,lon):
    observation=owm.three_hours_forecast_at_coords(lat,lon)
    forecasts=observation.get_forecast()

    location=forecasts.get_location()
    loc_name=location.get_name()
    loc_lat=location.get_lat()
    loc_lon=location.get_lon()

    for forecast in forecasts:
        time=forecast.get_reference_time('iso')
        status=forecast.get_status()
        detailed=forecast.get_detailed_status()
        temperature=forecast.get_temperature('celsius')
        temp=temperature.get("temp")
        temp_min=temperature.get("temp_min")
        temp_max=temperature.get("temp_max")

        results.append("""
        location : {} Lat : {} Lon : {}
        Time: {}
        Status: {}
        Detailed: {}
        Temperature: {}
        Min Temperature: {}
        Max Temperature: {}
        """.format(loc_name,loc_lat, loc_lon,time,status,detailed,temp,temp_min, temp_max))
    return "".join(results[:10])

if __name__=="__main__":
    print(get_forecast(-1.2,36))

#get_forecast()