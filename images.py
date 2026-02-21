import os
import re
import shutil
import urllib.parse

# Base dir (script location) to make repo-relative paths robust
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths (keep Obsidian source absolute)
obsidian_posts = "/home/will/Documents/IT/Blog/"
attachments_dir = "/home/will/Documents/IT/Blog/attachments"
static_images_dir = os.path.join(BASE_DIR, "static", "images")
post_dir = os.path.join(BASE_DIR, "content", "posts")

# Ensure destination directories exist
os.makedirs(static_images_dir, exist_ok=True)
os.makedirs(post_dir, exist_ok=True)

# Step 1: Copy markdown files from Obsidian vault into repo content/posts
for filename in os.listdir(obsidian_posts):
    if filename.endswith(".md"):
        src = os.path.join(obsidian_posts, filename)
        dst = os.path.join(post_dir, filename)
        shutil.copy2(src, dst)

# Step 2: Process each markdown file in the posts directory
for filename in os.listdir(post_dir):
    if not filename.endswith('.md'):
        continue
    filepath = os.path.join(post_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as fh:
        content = fh.read()

    # Find Obsidian embeds [[image.png]] and Markdown images ![alt](image.png)
    embeds = re.findall(r'\[\[\s*([^\]]+\.(?:png|jpe?g|gif|svg))\s*\]\]', content, flags=re.IGNORECASE)
    md_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+\.(?:png|jpe?g|gif|svg))\)', content, flags=re.IGNORECASE)
    images = list(dict.fromkeys(embeds + md_imgs))

    for image in images:
        image_basename = os.path.basename(image)
        safe_name = urllib.parse.quote(image_basename)
        markdown_image = f"![Image Description](/images/{safe_name})"

        # Replace possible forms: [[path/to/image.png]] or [[image.png]]
        content = re.sub(r'\[\[\s*' + re.escape(image) + r'\s*\]\]', markdown_image, content)
        content = re.sub(r'\[\[\s*' + re.escape(image_basename) + r'\s*\]\]', markdown_image, content)

        # Copy image from attachments folder. Try both the captured path and basename.
        image_source = os.path.join(attachments_dir, image)
        if not os.path.exists(image_source):
            image_source = os.path.join(attachments_dir, image_basename)

        if os.path.exists(image_source):
            dst_path = os.path.join(static_images_dir, image_basename)
            shutil.copy2(image_source, dst_path)

    # Write updated content back to post file
    with open(filepath, 'w', encoding='utf-8') as fh:
        fh.write(content)

print("Markdown files processed and images copied successfully.")
