import hashlib
import os
import json

# Function to calculate the hash of a file
def calculate_hash(file_path, algo='sha256'):
    hash_func = hashlib.new(algo)
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        return None

# Function to generate and save hashes for all files in a directory
def generate_hashes(directory, hash_file='hashes.json'):
    hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            hash_value = calculate_hash(path)
            if hash_value:
                relative_path = os.path.relpath(path, directory)
                hashes[relative_path] = hash_value
    
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)
    print(f"Hashes saved to {hash_file}")

# Function to check file integrity by comparing current hashes with stored hashes
def verify_integrity(directory, hash_file='hashes.json'):
    try:
        with open(hash_file, 'r') as f:
            old_hashes = json.load(f)
    except FileNotFoundError:
        print(f"Hash file '{hash_file}' not found. Please generate it first.")
        return

    current_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            relative_path = os.path.relpath(path, directory)
            current_hashes[relative_path] = calculate_hash(path)
    
    print("\nFile Integrity Check Report:")
    for file, old_hash in old_hashes.items():
        current_hash = current_hashes.get(file)
        if current_hash is None:
            print(f"[MISSING] {file}")
        elif current_hash != old_hash:
            print(f"[MODIFIED] {file}")
        else:
            print(f"[OK] {file}")
    
    for file in current_hashes:
        if file not in old_hashes:
            print(f"[NEW] {file}")

# Example usage
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("directory", help="Directory to monitor")
    parser.add_argument("--generate", action="store_true", help="Generate new hashes")
    parser.add_argument("--verify", action="store_true", help="Verify file integrity")
    parser.add_argument("--hashfile", default="hashes.json", help="Path to the hash storage file")

    args = parser.parse_args()

    if args.generate:
        generate_hashes(args.directory, args.hashfile)
    elif args.verify:
        verify_integrity(args.directory, args.hashfile)
    else:
        print("Please specify either --generate or --verify")
