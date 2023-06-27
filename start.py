import os
import wave

def calculate_total_duration(folder_path, include_subfolders=True):
    total_duration = 0

    for root, dirs, files in os.walk(folder_path):
        if not include_subfolders and root != folder_path:
            break

        for file in files:
            if file.endswith(".wav"):  # 假设只处理.wav格式的音频文件，可以根据需要修改
                file_path = os.path.join(root, file)
                with wave.open(file_path, 'rb') as audio_file:
                    frames = audio_file.getnframes()
                    frame_rate = audio_file.getframerate()
                    duration = frames / float(frame_rate)
                    total_duration += duration

    return total_duration

# 示例用法
folder_path = input("请输入音频文件所在的文件夹路径: ")
include_subfolders = input("是否遍历子文件夹？(y/n)").lower() == "y"
total_duration = calculate_total_duration(folder_path, include_subfolders)
print(f"总时长：{total_duration} 秒, 约为 {total_duration / 60} 分钟, 约为 {total_duration / 3600} 小时")
