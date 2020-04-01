from covid import Covid

covid = Covid()
coron=covid.get_data()
# print(coron)
countries = covid.list_countries()
# print(countries)
india_cases = covid.get_status_by_country_name('India')
# india_cases = covid.get_status_by_country_name(84)
print(india_cases)
netherlands_cases = covid.get_status_by_country_name('Netherlands')
print(netherlands_cases)

spain_cases = covid.get_status_by_country_name('Spain')
print(spain_cases)

greece_cases = covid.get_status_by_country_name('greece')
print(greece_cases)

active = covid.get_total_active_cases()
confirmed = covid.get_total_confirmed_cases()
recovered = covid.get_total_recovered()
deaths = covid.get_total_deaths()
print("\n" + "Total active: "+str(active) + "\n" + "Total confirmed: " +str(confirmed) + "\n" + "Total recovered: " + str(recovered) + "\n" + "Total deaths: " + str(deaths) + "\n")
