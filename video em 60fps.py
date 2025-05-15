import subprocess

input_video = "D:\\Nova pasta\\video_sharpen\\60fps.mp4"
output_interpolated = "D:\\Nova pasta\\video_sharpen\\video em 60 fps.mp4"

ffmpeg_path = r"C:\\Users\\micdc\\Downloads\\ffmpeg-6.0-full_build\\bin\\ffmpeg.exe"  # ajuste para o caminho correto do seu ffmpeg.exe

command = [
    ffmpeg_path,
    "-i", input_video,
    "-filter_complex", "minterpolate=fps=60",
    output_interpolated
]

subprocess.run(command, check=True)
print("Vídeo com quadros melhorados gerado com sucesso!")
