import numpy as np
import cv2
def main():
    print("Hello from data-analysis!")

def camera_access():
    import cv2

def open_camera():
    # 0 is usually the default built-in camera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Camera opened. Press 'q' to exit.")

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Can't receive frame. Exiting...")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Wait for 'q' key to stop the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()