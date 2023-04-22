import cv2
import tkinter as tk
from tkinter import simpledialog

def capture_image(camera_index, destination_folder):
    # Open the camera
    cap = cv2.VideoCapture(camera_index)
    if not cap.isOpened():
        print("Failed to open camera")
        return

    # Open a window to display the camera feed
    cv2.namedWindow("Camera")
    while True:
        # Capture a frame
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        # Display the frame in the window
        cv2.imshow("Camera", frame)

        # Check for key press or mouse click
        key = cv2.waitKey(1)
        if key == ord('s') or key == ord(' '):  # Press 's' or space key to capture and save the image
            # Prompt the user to set a name for the captured image using a dialog box
            root = tk.Tk()
            root.withdraw()
            image_name = simpledialog.askstring("Image Name", "Enter a name for the captured image:")
            root.destroy()

            if not image_name:  # If user cancels the dialog box or enters an empty name, skip saving the image
                continue

            # Save the image to the destination folder with the user-specified name
            destination_folder= r"C:/Users/risha/OneDrive/Desktop/face attendence system/photos"
            image_path = f"{destination_folder}/{image_name}.jpg"
            cv2.imwrite(image_path, frame)

            # Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()

            print(f"New face profile successfully added to the database.")
            break
        elif key == ord('q'):  # Press 'q' to quit without saving
            # Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()
            break
        elif cv2.getWindowProperty("Camera", cv2.WND_PROP_VISIBLE) == 0:  # Close the window to quit without saving
            # Release the camera and close the window
            cap.release()
            cv2.destroyAllWindows()
            break