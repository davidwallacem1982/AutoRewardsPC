import os
import re
import sys
from urllib.parse import unquote


def find_markdown_files(root_dir):
    md_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files


def check_links(root_dir):
    print(f"Checking links in {root_dir}...")
    md_files = find_markdown_files(root_dir)
    broken_links = []

    # Regex for standard markdown links [text](url)
    link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

    for file_path in md_files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            dirname = os.path.dirname(file_path)

            for match in link_pattern.finditer(content):
                link_text = match.group(1)
                link_url = match.group(2)

                # Skip external links
                if link_url.startswith(("http://", "https://", "mailto:", "#")):
                    continue

                # Handle anchors in local files (strip them for file check)
                url_path = link_url.split("#")[0]
                if not url_path:  # Just an anchor
                    continue

                # Decode URL specific encoding
                url_path = unquote(url_path)

                # Resolve absolute path relative to the file
                target_path = os.path.normpath(os.path.join(dirname, url_path))

                if not os.path.exists(target_path):
                    broken_links.append(
                        {
                            "file": file_path,
                            "text": link_text,
                            "url": link_url,
                            "target": target_path,
                        }
                    )
                    print(f"❌ Broken link in {os.path.relpath(file_path)}:")
                    print(f"   [{link_text}]({link_url})")
                    print(f"   Resolved to: {target_path}\n")

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

    with open("broken_links.log", "w", encoding="utf-8") as log:
        if broken_links:
            log.write(f"Found {len(broken_links)} broken links:\n")
            for error in broken_links:
                log.write(f"❌ File: {os.path.relpath(error['file'])}\n")
                log.write(f"   Link: [{error['text']}]({error['url']})\n")
                log.write(f"   Resolved: {error['target']}\n\n")
            print(f"Found {len(broken_links)} broken links. See broken_links.log")
            sys.exit(1)
        else:
            log.write("✅ All relative links are valid!")
            print("✅ All relative links are valid!")
            sys.exit(0)


if __name__ == "__main__":
    # Check docs/ and README.md (via current dir)
    base_dir = os.getcwd()
    check_links(base_dir)
