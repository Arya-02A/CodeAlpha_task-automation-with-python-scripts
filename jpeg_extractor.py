import os, shutil

def move_jpgs(source_dir, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)
    moved = 0
    for name in os.listdir(source_dir):
        if name.lower().endswith(('.jpg', '.jpeg')):
            src = os.path.join(source_dir, name)
            dst = os.path.join(dest_dir, name)
            try:
                shutil.move(src, dst)
                moved += 1
            except Exception as e:
                print(f"Failed to move {name}: {e}")
    print(f"Moved {moved} files.")


s = input("Source folder: ").strip()
d = input("Destination folder: ").strip()
move_jpgs(s, d)
