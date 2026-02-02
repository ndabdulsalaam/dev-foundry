import requests

def get_address(lat, lon, api_key):
    url = "http://api.positionstack.com/v1/reverse"
    params = {
        'access_key': api_key,
        'query': f"{lat},{lon}"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        if 'data' in data and len(data['data']) > 0:
            # Extract the first address
            result = data['data'][0]
            # Use 'label' as it usually contains the full address, fallback to constructing it if needed
            full_address = result.get('label') or result.get('name')
            return full_address
        else:
            return "No address found for these coordinates."
            
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    LAT = 6.6778
    LON = 3.1654
    API_KEY = "9b7930bd7040d627df9b66103e147f64"
    
    address = get_address(LAT, LON, API_KEY)
    print(f"Full Address: {address}")
