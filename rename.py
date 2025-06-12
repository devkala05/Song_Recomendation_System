import os

# Path to your folder with songs
folder_path = "./oufile"

# List all mp3 files
mp3_files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]

# Sort files for consistency
mp3_files.sort()

# Rename with ID
for idx, filename in enumerate(mp3_files):
    song_id = str(idx + 1).zfill(4)
    name_part = os.path.splitext(filename)[0]
    new_name = f"{song_id}_{name_part}.mp3"
    
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    
    os.rename(old_path, new_path)

print("✅ Renaming complete.")
