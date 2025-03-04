import requests


def lookup_barcode(barcode):
    api_key = 'YOUR_API_KEY'  # Replace with your Barcode Lookup API key
    url = f'https://api.barcodelookup.com/v3/products?barcode={barcode}&key={api_key}'
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'products' in data and len(data['products']) > 0:
            product = data['products'][0]
            print(f"Product Name: {product.get('product_name', 'N/A')}")
            print(f"Brand: {product.get('brand', 'N/A')}")
            print(f"Category: {product.get('category', 'N/A')}")
            print(f"Description: {product.get('description', 'N/A')}")
            print(f"Images: {product.get('images', [])}")
        else:
            print("Product not found.")
    else:
        print(f"Error: {response.status_code}")


# Example usage
barcode = '5060947547162'
lookup_barcode(barcode)
