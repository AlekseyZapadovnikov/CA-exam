#!/usr/bin/python3
import os
import argparse

# Constants
IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg', '.gif', '.svg')
MARKDOWN_EXTENSIONS = ('.md', '.markdown')


def find_files_in_directory(path, extensions):
    return [
        os.path.join(root, file)
        for root, _, files in os.walk(path)
        for file in files if file.lower().endswith(extensions)
    ]


def check_image_usage(image_path, markdown_path, verbose, usage_filter):
    image_files = set(find_files_in_directory(image_path, IMAGE_EXTENSIONS))
    markdown_files = find_files_in_directory(markdown_path, MARKDOWN_EXTENSIONS)

    image_usage = {img_file: [] for img_file in image_files}
    for md_file in markdown_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                for img_file in image_files:
                    if os.path.basename(img_file) in line:
                        image_usage[img_file].append((md_file, line_num))

    for img_file, usage in image_usage.items():
        used = bool(usage)
        if usage_filter == 'used' and not used or usage_filter == 'not-used' and used:
            continue

        print(f"{img_file}: {'used' if used else 'not used'}", end="")
        if verbose and used:
            for md_file, line_num in usage:
                print(f" in {md_file}:{line_num}")
        else:
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Find used or not used images in Markdown files.')
    parser.add_argument('image_path', type=str, help='Path to the directory containing images.')
    parser.add_argument('markdown_path', type=str, help='Path to the directory containing Markdown files.')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output.')
    parser.add_argument('--usage', choices=['used', 'not-used'], default='not-used',
                        help='Filter for used or not used images.')

    args = parser.parse_args()
    check_image_usage(args.image_path, args.markdown_path, args.verbose, args.usage)
