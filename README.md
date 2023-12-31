# Health System provider for Faker

[//]: # ([![Tests]&#40;https://github.com/matthttam8411/faker_education/actions/workflows/python-app.yml/badge.svg&#41;]&#40;https://github.com/matthttam8411/faker_education/actions/workflows/python-app.yml&#41;)

[//]: # ([![Maintainability]&#40;https://api.codeclimate.com/v1/badges/180ddde29f8aa4e8c869/maintainability&#41;]&#40;https://codeclimate.com/github/matthttam8411/faker_education/maintainability&#41;)

[//]: # ([![Test Coverage]&#40;https://api.codeclimate.com/v1/badges/180ddde29f8aa4e8c869/test_coverage&#41;]&#40;https://codeclimate.com/github/matthttam8411/faker_education/test_coverage&#41;)


`faker_healthcare_system` is a provider for the `Faker` Python package.

## Description

`faker_healthcare_system` provides fake data related to healthcare system for testing purposes.

## Installation

Install with pip:

``` bash
pip install faker-healthcare-system
```

Add as a provider to your Faker instance:

``` bash
from faker import Faker
from provider_individual import IndividualProvider

fake = Faker()
fake.add_provider(IndividualProvider)
```

### NPI

``` python
>>> fake.npi()
513653999
```

### TIN

``` python
>>> fake.tin()
156224985
```

### Gender

``` python
>>> fake.gender()
M
```

### Enumeration date

``` python
>>> fake.enumeration_date()
2019-04-25
```

### Taxonomy

``` python
>>> fake.taxonomy()
{
    'code': '2279H0200X', 
    'classification': 'Respiratory Therapist, Registered', 
    'specialization': 'Home Health', 
    'section': 'Individual', 
    'grouping': 'Respiratory, Developmental, Rehabilitative and Restorative Service Providers', 
    'display_name': 'Home Health Registered Respiratory Therapist'
}
```

### Taxonomies of individuals
#### Generate the number of taxonomies specified.
Standard version [23.1, 7/1/23](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40/csv-mainmenu-57), created by NUCC, is being used.
``` python
>>> fake.fake.individual_taxonomies(2)
[
        {
            'code': '163WX0200X',
            'classification': 'Registered Nurse',
            'specialization': 'Oncology',
            'section': 'Individual',
            'grouping': 'Nursing Service Providers', 'display_name': 'Oncology Registered Nurse'
        },
        {
            'code': '202K00000X',
            'classification': 'Phlebology',
            'specialization': '',
            'section': 'Individual',
            'grouping': 'Allopathic & Osteopathic Physicians', 
            'display_name': 'Phlebology Physician'
        }
]
```

### Unique Taxonomies of individuals
#### Generate the number of taxonomies specified.
``` python
>>> fake.individual_unique_taxonomies(2)
[
    {
        'code': '207RH0002X',
        'classification': 'Internal Medicine',
        'specialization': 'Hospice and Palliative Medicine',
        'section': 'Individual', 
        'grouping': 'Allopathic & Osteopathic Physicians',
        'display_name': 'Hospice and Palliative Medicine (Internal Medicine) Physician'
    },
    {
        'code': '246ZB0301X', 
        'classification': 'Specialist/Technologist, Other',
        'specialization': 'Biomedical Engineering',
        'section': 'Individual', 
        'grouping': 'Technologists, Technicians & Other Technical Service Providers',
        'display_name': 'Biomedical Engineer'
    }
]
```

### Married name

``` python
>> female_person = fake.person_name_by_gender('F')
{
    'first_name': 'Amy', 
    'last_name': 'Miller', 
    'name_prefix': 'Mrs.', 
    'name_suffix': 'MD', 
    'type_name': 'Personal Name'
}
>> fake.person_married_name(female_person)
{
    'first_name': 'Amy',
    'last_name': 'Santana', 
    'name_prefix': 'Mrs.', 
    'name_suffix': 'MD', 
    'type_name': 'Married'
}
```

### Address
#### Generate a random address; by default, the purpose is 'Mailing', but if you need to change it, put the desired purpose in the function.
``` python
>> female_person = fake.address_with_purpose()
{
    'country_code': 'US', 
    'country_name': 'United States', 
    'purpose': 'Mailing', 
    'address_type': 'FGN', 
    'address_1': '4106 Peterson Center\nEast Matthew, MA 92472', 
    'address_2': '1961 Leslie Mission\nNorth Christopherberg, DC 03284', 
    'city': 'Rhondashire', 
    'state': 'Nevada', 
    'postal_code': '63012', 
    'telephone_number': '270-845-8739x895', 
    'fax_number': '001-686-489-7865x80217'
}

>> female_person = fake.address_with_purpose('Main Office')
{
    'country_code': 'US', 
    'country_name': 'United States', 
    'purpose': 'Main Office', 
    'address_type': 'Physical', 
    'address_1': '4106 Peterson Center\nEast Matthew, MA 92472', 
    'address_2': '1961 Leslie Mission\nNorth Christopherberg, DC 03284', 
    'city': 'Rhondashire', 
    'state': 'Nuevo Hampshire', 
    'postal_code': '63012', 
    'telephone_number': '270-845-8739x895', 
    'fax_number': '001-686-489-7865x80217'
}
```

### DEA
``` python
>> fake.dea()
{
    'number': 'M5490877',
    'allow_prescribe': True, 
    'start_date': datetime.date(2020, 3, 22), 
    'expiration_date': datetime.date(2024, 3, 21), 
    'supervising_number': 'Y5472030', 
    'supervising_license': 2806910
}
```

### Professional degree school
``` python
>> fake.professional_degree_school()
Johns Hopkins University - Johns Hopkins School of Medicine
```

### Language
``` python
>> fake.practitioner_language()
{
    'code': 'TR', 
    'description': 'Turkish', 
    'language_type': 'Practitioner'
}
```

### Languages
#### Generates the specified number of languages, plus English
``` python
>> fake.practitioner_languages_plus_english(2)
[
    {
        'code': 'SM', 
        'description': 'Samoan', 
        'language_type': 'Practitioner'
    },
    {
        'code': 'FI', 
        'description': 'Finnish', 
        'language_type': 'Practitioner'
    }, 
    {
        'code': 'en', 
        'description': 'English', 
        'language_type': 'Practitioner'
    }
]
```

### Ethnicity
``` python
>> fake.practitioner_ethnicity_code()
{   
    'code': 'J', 
    'description': 'JAPANESE'
}
```

### Gender restriccion
``` python
>> fake.gender_restriction()
F
```

### Malpractice
``` python
>> fake.malpractice()
{
    'insurance': 'Fairway Physicians Ins. Co.', 
    'insurance_policy_number': 5, 
    'covered_amount': ' 1-6'
}
```

### License
``` python
>> fake.license()
{
    'license': 'I93615979', 
    'state': 'Dakota del Sur', 
    'is_primary': False, 
    'start_date': datetime.date(2020, 3, 22), 
    'end_date': datetime.date(2024, 3, 21)
}
```
### Identifier
``` python
>> fake.identifier()
{
    'code': 6950, 
    'desc': 'Medicare', 
    'issuer': 'pZGG', 
    'identifier': '59333', 
    'state': 'Misuri'
}
```

### Board
``` python
>> fake.board()
{
    'status': 2, 
    'start_date': datetime.date(2022, 1, 31), 
    'expiration_date': datetime.date(2023, 1, 31)
}
```

### Working hours
``` python
>> fake.working_hours()
10:00-13:00
```
### Weekly working hours
``` python
>> fake.weekly_working_hours()
{
    'Monday': '10:00-13:00', 
    'Tuesday': '7:00-13:00', 
    'Wednesday': '10:00-20:00', 
    'Thursday': '9:00-17:00', 
    'Friday': '8:00-18:00', 
    'Saturday': 'CLOSED', 
    'Sunday': 'CLOSED'
}
```

### Taxonomy qualification
``` python
>> fake.taxonomy_qualification()
{
    'board': {
                'status': 5, 
                'start_date': datetime.date(2023, 8, 18), 
                'expiration_date': datetime.date(2024, 8, 17)
             }, 
    'intership_start_date': datetime.date(2021, 10, 16), 
    'intership_expiration_date': datetime.date(2024, 10, 15), 
    'residency_start_date': datetime.date(2021, 10, 16), 
    'residency_expiration_date': datetime.date(2023, 10, 16), 
    'fellowship_start_date': datetime.date(2021, 10, 16), 
    'fellowship_expiration_date': datetime.date(2024, 10, 15), 
    'taxonomy': 
                {
                    'code': '103T00000X', 
                    'classification': 'Psychologist', 
                    'specialization': '', 
                    'section': 'Individual', 
                    'grouping': 'Behavioral Health & Social Service Providers', 
                    'display_name': 'Psychologist'
                }, 
    'facility_type': 10
}
```

### Endpoint
``` python
>> fake.endpoint()
{
    'endpointType': 'CONNECT', 
    'endpointTypeDescription': 'CONNECT URL', 
    'endpoint': 'http://thompson-young.com/blog/appregister.htm', 
    'endpointDescription': '', 
    'affiliation': 'N', 
    'use': 'DIRECT', 
    'useDescription': 'Direct', 
    'contentType': 'OTHER', 
    'contentTypeDescription': 'Communication', 
    'contentOtherDescription': 'Communication', 
    'country_code': 'US', 
    'country_name': 'United States', 
    'address_1': '628 Banks Stravenue\nCarolynfort, DC 08813', 
    'city': 'Kylemouth', 
    'state': 'Vermont', 
    'postal_code': '71465'
}
```



### Individual
``` python
>> fake.individual_object()
{
    'npi': 465929309,
    'tin': 155728978, 
    'last_updated_epoch': datetime.date(2022, 5, 23), 
    'created_epoch': datetime.date(2019, 5, 24), 
    'enumeration_date': datetime.date(2020, 3, 24), 
    'status': 'Active', 
    'email': 'matthewcook@example.org', 
    'enumeration_type': 'NPI-1', 
    'mailing_address': {
                            'country_code': 'US', 
                            'country_name': 'United States', 
                            'purpose': 'Mailing', 
                            'address_type': 'DOM', 
                            'address_1': '96105 Garcia Cape Apt. 220\nRhondashire, NJ 35277', 
                            'address_2': '5873 Smith Trafficway\nCohenfort, NC 88118', 
                            'city': 'Brookston', 
                            'state': 'Ohio', 
                            'postal_code': '99351', 
                            'telephone_number': '+1-721-274-2558x6176', 
                            'fax_number': '291.650.5368'
                        }, 
    'location_address': {
                            'country_code': 'US', 
                            'country_name': 'United States', 
                            'purpose': 'LOCATION', 
                            'address_type': 'FGN', 
                            'address_1': 'Unit 3872 Box 2876\nDPO AA 06285', 
                            'address_2': '04546 Smith River Apt. 851\nSouth Priscillaside, MS 10132', 
                            'city': 'Johnsonmouth', 
                            'state': 'Alaska', 
                            'postal_code': '34912', 
                            'telephone_number': '308.256.5026x1253', 
                            'fax_number': '001-486-884-2465x28581'
                         }, 
    'main_office_address': {
                                'country_code': 'US', 
                                'country_name': 'United States', 
                                'purpose': 'Main Office', 
                                'address_type': 'Physical', 
                                'address_1': '0577 Patterson Trail\nEast Aimeehaven, NY 73452', 
                                'address_2': '539 Davis Parkways\nEast Olivia, KS 52689', 
                                'city': 'New Christopherborough', 
                                'state': 'Maine', 
                                'postal_code': '66709', 
                                'telephone_number': '303.749.3195', 
                                'fax_number': '+1-682-982-7760'
                            }, 
    'taxonomies': [
                    {
                        'code': '2084E0001X', 
                        'classification': 'Psychiatry & Neurology', 
                        'specialization': 'Epilepsy', 
                        'section': 'Individual', 
                        'grouping': 'Allopathic & Osteopathic Physicians', 
                        'display_name': 'Epilepsy Physician'
                    }, 
                    {
                        'code': '146L00000X', 
                        'classification': 'Emergency Medical Technician, Paramedic', 
                        'specialization': '', 
                        'section': 'Individual', 
                        'grouping': 'Emergency Medical Service Providers', 
                        'display_name': 'Paramedic'
                    }, 
                    {
                        'code': '163WX0003X', 
                        'classification': 'Registered Nurse', 
                        'specialization': 'Obstetric, Inpatient', 
                        'section': 'Individual', 
                        'grouping': 'Nursing Service Providers', 
                        'display_name': 'Inpatient Obstetric Registered Nurse'
                    }, 
                    {
                        'code': '364SP0812X', 
                        'classification': 'Clinical Nurse Specialist', 
                        'specialization': 'Psychiatric/Mental Health, Community', 
                        'section': 'Individual', 
                        'grouping': 'Physician Assistants & Advanced Practice Nursing Providers', 
                        'display_name': 'Community Psychiatric/Mental Health Clinical Nurse Specialist'
                    }
                 ], 
    'licenses': [
                    {
                        'license': 'M981935046', 
                        'state': 'Alaska', 
                        'is_primary': True, 
                        'start_date': datetime.date(2021, 6, 12), 
                        'end_date': datetime.date(2023, 6, 12)
                    }, 
                    {
                        'license': 'U6400179',
                        'state': 'Utah', 
                        'is_primary': False, 
                        'start_date': datetime.date(2022, 8, 5), 
                        'end_date': datetime.date(2026, 8, 4)
                    }, 
                    {   
                        'license': 'W627735057', 
                        'state': 'Maine', 
                        'is_primary': True, 
                        'start_date': datetime.date(2021, 6, 17), 
                        'end_date': datetime.date(2022, 6, 17)
                    }, 
                    {
                        'license': 'O388523895', 
                        'state': 'Wisconsin', 
                        'is_primary': False, 
                        'start_date': datetime.date(2021, 7, 14), 
                        'end_date': datetime.date(2025, 7, 13)
                    }
                 ], 
    'identifiers': '',
    'taxonomy_qualification': '',
    'taxonomy_endpoints': '', 
    'schedule': '',
    'credential': 'MD', 
    'sole_proprietor': 'NO', 
    'gender': 'F', 
    'personal_name': {
                        'first_name': 'Deborah',
                        'last_name': 'Roberson', 
                        'name_prefix': 'Dr.', 
                        'name_suffix': 'MD', 
                        'type_name': 'Personal Name'
                     }, 
    'other_names': {
                        'first_name': 'Deborah', 
                        'last_name': 'Stewart', 
                        'name_prefix': 'Dr.', 
                        'name_suffix': 'MD', 
                        'type_name': 'Married'
                    }, 
    'dea': {
                'number': 'C8533755',
                'allow_prescribe': True, 
                'start_date': datetime.date(2020, 12, 2), 
                'expiration_date': datetime.date(2022, 12, 2), 
                'supervising_number': 'Y4031241', 
                'supervising_license': 7415179
            }, 
    'ethnicity_code': 'T', 
    'date_of_birth': datetime.date(2017, 7, 30), 
    'languages': [
                    {'code': 'BG', 'description': 'Bulgarian', 'language_type': 'Practitioner'},
                    {'code': 'RU', 'description': 'Russian', 'language_type': 'Practitioner'}, 
                    {'code': 'CO', 'description': 'Corsican', 'language_type': 'Practitioner'}, 
                    {'code': 'BR', 'description': 'Breton', 'language_type': 'Practitioner'}, 
                    {'code': 'SL', 'description': 'Slovene', 'language_type': 'Practitioner'}, 
                    {'code': 'MG', 'description': 'Malagasy', 'language_type': 'Practitioner'}, 
                    {'code': 'en', 'description': 'English', 'language_type': 'Practitioner'}], 
    'gender_restriction': 'F', 
    'malpractice': {
                        insurance': 'MUTUAL PROTECTION TRUST', 
                        'insurance_policy_number': 7297077, 
                        'covered_amount': ' 8-4'
                    }, 
    'professional_degree_school': 'University of Washington - UW School of Medicine'
    }
```

