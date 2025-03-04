import os
import ctypes
import cv2
from pyzbar.pyzbar import decode


# Manually set the ZBar library path
zbar_lib_path = "/opt/homebrew/opt/zbar/lib/libzbar.dylib"
os.environ["DYLD_LIBRARY_PATH"] = os.path.dirname(zbar_lib_path)
ctypes.cdll.LoadLibrary(zbar_lib_path)

print("✅ ZBar library loaded successfully!")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect barcodes/QR codes
    barcodes = decode(gray)

    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')  # Extract barcode text
        barcode_type = barcode.type  # Get barcode type (QR Code, EAN, etc.)

        # Draw a rectangle around the barcode
        rect = barcode.rect
        cv2.rectangle(frame, (rect.left, rect.top),
                      (rect.left + rect.width, rect.top + rect.height),
                      (0, 255, 0), 2)

        # Display barcode text on the frame
        cv2.putText(frame, f"{barcode_data} ({barcode_type})",
                    (rect.left, rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 2)

    # Show webcam feed
    cv2.imshow("Barcode Scanner Test", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()

