import os
import cv2

def convert_folder_videos_to_mp4(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]

    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)

        # Generate the corresponding output MP4 file path
        output_file = os.path.splitext(video_file)[0] + '.mp4'
        output_path = os.path.join(output_folder, output_file)

        # Convert the video file to MP4
        try:
            convert_video_to_mp4(input_path, output_path)
        except Exception as e:
            print(f"Error converting {video_file}: {e}")

def convert_video_to_mp4(input_file, output_file):
    # Read the input video file
    cap = cv2.VideoCapture(input_file)

    # Get the video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Create a VideoWriter object to save the output as MP4
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        # Write the frame to the output file
        out.write(frame)

    # Release the resources
    cap.release()
    out.release()

# Example usage
input_folder = 'C:/Users/weble/Desktop/jai_vid/input_folder'
output_folder = 'C:/Users/weble/Desktop/jai_vid/output_folder'
convert_folder_videos_to_mp4(input_folder, output_folder)
