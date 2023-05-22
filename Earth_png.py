import requests

# Make a GET request to the endpoint to retrieve the list of available images
response = requests.get('https://epic.gsfc.nasa.gov/api/natural')

# Check if the request was successful
if response.status_code == 200:
    # Extract the JSON data from the response
    data = response.json()

    # Process the data to get the necessary information
    for image in data:
        image_id = image['image']
        date = image['date']

        # Use the image ID to construct the URL for downloading the image
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{date[:4]}/{date[5:7]}/{date[8:10]}/png/{image_id}.png"

        # Download the image
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            with open(f"{image_id}.png", "wb") as f:
                f.write(image_response.content)

            print(f"Image {image_id} downloaded successfully.")

else:
    print('Error occurred while accessing the API.')