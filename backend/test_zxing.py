import pyzxing

# Initialize ZXing Reader
reader = pyzxing.BarCodeReader()

# Path to a test barcode image (update with your image path)
image_path = "test_barcode.png"

# Decode the barcode
results = reader.decode(image_path)

if results:
    for result in results:
        print(f"✅ Found barcode: {result['raw']} (Type: {result['format']})")
else:
    print("❌ No barcode found in the image.")
