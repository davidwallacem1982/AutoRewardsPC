import os
import sys
import zipfile


def extract_images_from_docx(docx_path, output_dir):
    if not os.path.exists(docx_path):
        print(f"Error: File not found: {docx_path}")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Extracting images from {docx_path} to {output_dir}...")

    try:
        with zipfile.ZipFile(docx_path, "r") as zip_ref:
            # Images are in word/media/
            for file_info in zip_ref.infolist():
                if (
                    file_info.filename.startswith("word/media/")
                    and file_info.file_size > 0
                ):
                    filename = os.path.basename(file_info.filename)
                    target_path = os.path.join(output_dir, filename)

                    with (
                        zip_ref.open(file_info) as source,
                        open(target_path, "wb") as target,
                    ):
                        target.write(source.read())

                    print(f"  Extracted: {filename} ({file_info.file_size} bytes)")
    except zipfile.BadZipFile:
        print(
            "Error: The file is not a valid zip archive (docx files are zip archives)."
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Default paths
    docx_file = os.path.join("docs", "Manual_Usuario_AutoRewardsPC.docx")
    output_folder = os.path.join("assets", "extracted_from_manual")

    extract_images_from_docx(docx_file, output_folder)
