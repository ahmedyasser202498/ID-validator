import json
from datetime import datetime


class NIDValidtor(object):

    def __init__(self) -> None:
        with open('provinces.json', 'r') as f:
            provinces= json.load(f)
        
        self.provinces= provinces

    def validate_national_id(self,national_id):
        # Check if the National ID is exactly 14 digits long
        if len(national_id) != 14 or not national_id.isdigit():
            return False, "Invalid National ID format"

        # Extract the century (2 is from 1900 to 1999, 3 is from 2000 to 2099)
        century_code = int(national_id[0])

        if century_code not in [2, 3]:
            return False, "Invalid century code"

        # Extract the birth date: YYMMDD
        birth_year = int(national_id[1:3])
        birth_month = int(national_id[3:5])
        birth_day = int(national_id[5:7])

        # Validate the birth date
        try:
            birth_date = datetime.strptime(f'{birth_year:02d}-{birth_month:02d}-{birth_day:02d}', '%y-%m-%d')
        except ValueError:
            return False, "Invalid birth date"

        # Extract the province number and check if valid
        province_no= national_id[7:9]
        province=None
        for prov in self.provinces:
            if province_no == prov['code']:
                province=prov['name']

        if not province:
            return False, "Invalid province"

        # Extract the serial number and gender 
        serial_number = national_id[9:13]
        gender_code= 1 if int(national_id[12])%2 ==0 else 2


        # Return extracted data
        return True, {
            'gender': 'Male' if gender_code == 2 else 'Female',
            'birth_date': birth_date.strftime('%Y-%m-%d'),
            'serial_number': serial_number,
            'birth_province':province
        }