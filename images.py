import os
import re
import shutil

# Paths
posts_dir = "/home/will/Documents/IT/Blog/"
attachments_dir = "/home/will/Documents/IT/Blog/attachments"
static_images_dir = "/home/will/code/blog/static/images"

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r") as file:
            content = file.read()
        
        # Step 2: Find image references: Obsidian embeds like [[image.png]]
        # and standard Markdown images like ![alt](image.png).
        # Capture common image extensions and allow paths or basenames.
        embeds = re.findall(r'\[\[\s*([^\]]+\.(?:png|jpe?g|gif|svg))\s*\]\]', content, flags=re.IGNORECASE)
        md_imgs = re.findall(r'!\[[^\]]*\]\(([^)]+\.(?:png|jpe?g|gif|svg))\)', content, flags=re.IGNORECASE)
        images = list(dict.fromkeys(embeds + md_imgs))
        
        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image in images:
            # Prepare the Markdown-compatible link with %20 replacing spaces
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, image)
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w") as file:
            file.write(content)

print("Markdown files processed and images copied successfully.")
