# 1. Import dependencies
from TM1py.Services import TM1Service

# 2. Main function
def main(params):
    # 3. Get credentials
    creds = {
        'user':params['pauser'],
        'password':params['papassword'], 
        'port':params['paport'],
        'ssl':'False',
        'address':params['paaddress']
    }

    # 4. Get cellset
    cellset = {
        (
            params['Month'], 
            params['Version'], 
            params['Currency'], 
            params['CostCentre'], 
            params['Account'], 
            params['Project'], 
            params['GeneralLedgerSource'], 
            params['GeneralLedgerMeasure'],
        ):params['Value']
    }

    # 5. Write to cube
    with TM1Service(**creds) as tm1:
        tm1.cubes.cells.write_values('General Ledger', cellset, dimensions=['Time Month', 'Version', 'Currency', 'Cost Centre', 'Account', 'Project', 'General Ledger Source', 'General Ledger Measure'])

    # 6. Return result
    print('Data loaded.')
    return {
        'headers':{'Content-Type':'application/json'}, 
        'body':{'message':'Commentary loaded.'}
    }

# 7. Make call
if __name__ == '__main__':
    params = {'pauser':'TM1 USER', 'papassword':'TM1 PASSWORD', 'paport':TM1 HTTP PORT, 'paaddress':'TM1 SERVER', 'Month':'FY2019', 'Version':'Budget', 'Currency':'Local', 'CostCentre':'All Cost Centres', 'Account':'All Accounts', 'Project':'BAU', 'GeneralLedgerSource':'Base', 'GeneralLedgerMeasure':'Commentary', 'Value':'Hotline Bling.'}
    main(params)