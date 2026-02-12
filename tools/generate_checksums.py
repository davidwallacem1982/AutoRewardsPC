import hashlib
import os


def generate_checksums(directory="dist"):
    """Generates SHA256 checksums for all files in the given directory."""
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        return

    checksums = {}
    print(f"Generating checksums for files in '{directory}'...")

    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            # Calculate SHA256
            sha256_hash = hashlib.sha256()
            with open(filepath, "rb") as f:
                # Read and update hash string value in blocks of 4K
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)

            relative_path = os.path.relpath(filepath, directory)
            checksums[relative_path] = sha256_hash.hexdigest()
            print(f"  {relative_path}: {checksums[relative_path]}")

    # Write to file
    output_file = os.path.join(directory, "CHECKSUMS.txt")
    with open(output_file, "w") as f:
        for filename, hash_val in checksums.items():
            f.write(f"{hash_val}  {filename}\n")

    print(f"\nChecksums saved to {output_file}")


if __name__ == "__main__":
    generate_checksums()
