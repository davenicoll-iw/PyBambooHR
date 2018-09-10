from PyBambooHR import PyBambooHR

bamboo = PyBambooHR.PyBambooHR(subdomain='', api_key='')

# Use the ID to request json information
# result = bamboo.request_company_report(1, format='json', filter_duplicates=True)
result = bamboo.request_company_report(1, filter_duplicates=True)

# Now do stuff with your results (Will vary by report.)
for employee in result['employees']:
   print(employee)