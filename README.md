# Egyptian National ID Validator and Data Extractor API

This project is an API designed to validate and extract data from Egyptian National IDs (NID). It verifies the authenticity of a National ID number and provides relevant details, such as gender, birth date, and province, based on the ID provided. 

## Features

- **Validation of National ID format**: Verifies if the National ID consists of 14 digits.
- **Birth Date Validation**: Validates the birth date encoded within the National ID.
- **Province Verification**: Ensures that the province code in the ID corresponds to a valid province.
- **Gender Determination**: Extracts gender based on the National ID's structure.
- **API Key Authentication**: Secure access to the API through an API key.

## Technologies Used

- **Django**: A high-level Python web framework.
- **Django Rest Framework (DRF)**: A powerful toolkit for building Web APIs.
- **JSON**: For storing and loading provinces data.
- **Python**: For implementing the core logic.

## Project Structure

/project│├── /nid\_validator│ ├── **init**.py│ ├── /migrations│ ├── models.py # Defines the API Key model│ ├── serializers.py # Defines the National ID Serializer│ ├── services.py # Contains the core logic for validating National IDs│ ├── utils.py # Helper functions, including API Key validation│ ├── views.py # API Views to handle requests│ └── /templates│├── /manage.py # Django management script└── /provinces.json # JSON file containing Egyptian provinces and their codes



## Installation

### Prerequisites

1. Python 3.x
2. Django
3. Django Rest Framework

### Steps to Setup

1. **Clone the repository**:

   git clone [<repository-url>](https://github.com/ahmedyasser202498/ID-validator#)
   cd national_id_validator

2. **Docker Build**:
    docker-compose up --build



API Documentation
-----------------

### Endpoint: POST /validate\_nid/

**Description**: This endpoint validates the provided Egyptian National ID and extracts relevant data.

#### Request

`   {    "national_id": "29501068800164"  }   `

*   national\_id (required): A 14-digit string representing the Egyptian National ID.
    

#### Response

If the National ID is valid, the response will contain:

`   {    "gender": "Female",    "birth_date": "1995-01-06",    "serial_number": "0016",    "birth_province": "Outside the republic"  }   `

If the National ID is invalid, the response will contain an error message:

`   {    "error": "Invalid National ID format"  }   `

#### Example of Invalid ID:

1.  Invalid length (not 14 digits)
    
2.  Invalid birth date (e.g., 31st February)
    
3.  Invalid province code
    

#### Authentication

The API requires an API key to access it. To authenticate, include your API key in the X-API-Key header. [ key: 1111 ]

### Sample Request with API Key:

`  curl --location 'http://0.0.0.0:8000/app/validate_nid/' \--header 'X-API-Key: 1111' \--header 'Content-Type: application/json' \--data '{    "national_id":"29501068800164"}' `

#### Example Responses

**Valid Request**:

`   {    "gender": "Female",    "birth_date": "1985-05-21",    "serial_number": "6789",    "birth_province": "Cairo"  }   `

**Invalid Request**:

1. `   {    "error": "Invalid National ID format"  }   `
2. `   {    "error": "Invalid century code"  }   `
3. `   {    "error": "Invalid birth date"  }   `
4. `   {    "error": "Invalid province"  }   `

#### Rate limiting
The API has rate limit if exceeded.

#### Example Responses

` "detail": "Request was throttled. Expected available in 56 seconds." `

Models
------

### APIKey

This model is used for storing API keys in the system. API keys are used for authenticating requests to the API.

`   class APIKey(models.Model):      key = models.CharField(max_length=256, unique=True)      description = models.TextField(null=True, blank=True)      created_at = models.DateTimeField(auto_now_add=True)      is_active = models.BooleanField(default=True)      def __str__(self):          return self.key   `

Services
--------

### NIDValidator

The NIDValidator class contains the core logic for validating a National ID. It checks the format, validates the birth date, province, and gender..

### validate\_national\_id(national\_id)

This method validates the structure of the provided National ID and returns a tuple with:

*   True if the ID is valid, along with the extracted data.
    
*   False if the ID is invalid, along with an error message.
    

#### Example Output for Valid ID:

`   {    "gender": "Female",    "birth_date": "1985-05-21",    "serial_number": "6789",    "birth_province": "Cairo"  }   `

Utils
-----

### validate\_api\_key

This function validates the API key provided in the request headers. It checks the X-API-Key header for a valid key and ensures it is active in the database.

If the API key is missing or invalid, a JsonResponse with an appropriate error message is returned.



BONUS PART
-----

As an additional enhancement, I implemented the ELK (Elasticsearch, Logstash, Kibana) stack to help track and monitor API calls. The ELK stack provides powerful logging and analytics capabilities, allowing for real-time insights into the API's usage.

### ELK Stack Setup

I utilized Docker images to set up the ELK stack, ensuring a smooth and isolated environment for the components to function:

*   **Elasticsearch**: Used for storing and searching logs.
    
*   **Logstash**: Configured to collect, parse, and forward logs to Elasticsearch.
    
*   **Kibana**: Used for visualizing and analyzing the logs stored in Elasticsearch.
    

The goal of this integration was to create a robust logging mechanism that would provide detailed insights into API calls, helping with debugging, monitoring, and overall API performance tracking.

### Issue Encountered

Unfortunately, due to the current workload, I encountered a challenge that I was unable to resolve within the given timeframe. Specifically, I faced issues where **Logstash was not successfully forwarding logs to Elasticsearch** as expected. This prevented the logs from being indexed, and as a result, Kibana was unable to visualize the data.

The issue appears to be related to the configuration between Logstash and Elasticsearch, possibly due to:

*   Misconfiguration in the Logstash output settings.
    
*   Potential version compatibility issues between Logstash and Elasticsearch.
    

While that the core functionality of the API remains intact.
