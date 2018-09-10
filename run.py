from PyBambooHR import PyBambooHR

bamboo = PyBambooHR.PyBambooHR(subdomain='infinityworks', api_key='OTY0NTAzNjZjYmIyNmFlNTJkNzJlZDRmNjM0ODgxZGE3NDg5ZDg3ZDp4')

# Use the ID to request json information
# result = bamboo.request_company_report(1, format='json', filter_duplicates=True)
result = bamboo.request_company_report(1, filter_duplicates=True)

# Now do stuff with your results (Will vary by report.)
for employee in result['employees']:
   print(employee)