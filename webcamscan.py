import cv2
import numpy as np
import pyzxing
import tempfile
import os
import time

# Initialize ZXing Barcode Reader
reader = pyzxing.BarCodeReader()

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print(" Error: Could not open webcam.")
    exit()
else:
    print("Webcam initialized successfully!")

time.sleep(5)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

        # Display the video feed
    cv2.imshow("ZXing Barcode Scanner - Live Feed", frame)

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Save the frame as a temporary image
    temp_file = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    temp_path = temp_file.name
    cv2.imwrite(temp_path, gray)

    # Decode the barcode using ZXing
    results = reader.decode(temp_path)

    if results:
        for result in results:
            barcode_data = result["raw"]
            barcode_type = result["format"]

            # Draw a rectangle around the barcode (Dummy values for now)
            cv2.putText(frame, f"{barcode_data} ({barcode_type})",
                        (50, 50), cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0, 255, 0), 2)

            print(f"✅ Found barcode: {barcode_data} (Type: {barcode_type})")

    # Show webcam feed
    cv2.imshow("ZXing Barcode Scanner", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
os.remove(temp_path)  # Remove temporary file after scanning
