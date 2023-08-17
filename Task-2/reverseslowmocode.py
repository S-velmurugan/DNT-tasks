import cv2

# Open the video file for reading

cap = cv2.VideoCapture("walking.mp4")

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create VideoWriter objects for output videos

output = cv2.VideoWriter("Reverseslowmo.mp4", cv2.VideoWriter_fourcc(*'mp4v'), int(fps / 2), (frame_width, frame_height))

frame_list = []

# Read and store frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_list.append(frame)



# Reverse playback and decreasing the fps for slow motion.

for frame in reversed(frame_list):
    output.write(frame)
    cv2.imshow("SlowMotion and Reverse", frame)
    if cv2.waitKey(int(1000 / (fps / 4))) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
output.release()
cv2.destroyAllWindows()

print("done") #Confirmation.

