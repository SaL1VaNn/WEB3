import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def sort_files_by_extension(source_folder, destination_folder):
    def process_file(file_path):
        try:
            file_extension = os.path.splitext(file_path)[-1].lower()
            if file_extension:
                destination_path = os.path.join(destination_folder, file_extension[1:])
                os.makedirs(destination_path, exist_ok=True)
                shutil.move(file_path, os.path.join(destination_path, os.path.basename(file_path)))
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

    with ThreadPoolExecutor(max_workers=5) as executor:
        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(process_file, file_path)

if __name__ == "__main__":
    source_folder = "Мотлох"  # Замініть на шлях до вашої папки "Мотлох"
    destination_folder = "сортовані файли"  # Замініть на шлях до папки, де ви хочете зберегти сортовані файли
    os.makedirs(destination_folder, exist_ok=True)
    sort_files_by_extension(source_folder, destination_folder)

import multiprocessing

def factorize(*numbers):
    def worker(number):
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        return factors

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(worker, numbers)

    return results

if __name__ == "__main__":
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)
