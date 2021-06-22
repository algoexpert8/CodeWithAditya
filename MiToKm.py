#this is a calculator that will convert mile to km or km to mile
#for that we have to ask the user whether they want to convert from mi to km or from km to mi
print('KM-MI Converter')
select = input('Enter KM to convert from kilometre to mile or enter MI to convert from mile to kilometre:\n')
mileone = 1.60934 
kmone = 0.621371
number = input('OK, now enter the length value to convert:\n')
number = float(number)
if select=='KM':
    print(f'{number} KM in MI is = ',number*kmone,' MI')
elif select=='MI':
    print(f'{number} MI in KM is = ',number*mileone , ' KM')