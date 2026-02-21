#!/bin/bash
set -euo pipefail

##Flags:
# preview: will preview draft blog posts locally
# test: will show the site excluding draft posts
# commit: will sync and commit the posts to git

# Change to the script's directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Set variables for Obsidian to Hugo copy
sourcePath="$HOME/Documents/IT/Blog/"
destinationPath="$HOME/code/blog/content/posts/"
attachmentsFolder="$HOME/Documents/IT/Blog/attachments/"

# Set GitHub Repo
myrepo="blog"

# Check for required commands
for cmd in git rsync python3 hugo; do
    if ! command -v $cmd &> /dev/null; then
        echo "$cmd is not installed or not in PATH."
        exit 1
    fi
done

# Step 3: Process Markdown files with Python script to handle image links. Copies markdown post files.
echo "Processing image links in Markdown files..."
if [ ! -f "images.py" ]; then
    echo "Python script images.py not found."
    exit 1
fi

if ! python3 images.py; then
    echo "Failed to process image links."
    exit 1
fi

if [ "$1" == "preview" ]; then 
    hugo server --buildDrafts --disableFastRender --noHTTPCache
    exit 0
fi

if [ "$1" == "test" ]; then 
    hugo server --disableFastRender --noHTTPCache
    exit 0
fi

# Step 4: Build the Hugo site
echo "Building the Hugo site..."
if ! hugo; then
    echo "Hugo build failed."
    exit 1
fi

if [ "$1" == "commit" ]; then 
    # Step 5: Add changes to Git
    echo "Staging changes for Git..."
    if git diff --quiet && git diff --cached --quiet; then
        echo "No changes to stage."
    else
        git add .
    fi

    # Step 6: Commit changes with a dynamic message
    commit_message="New Blog Post on $(date +'%Y-%m-%d %H:%M:%S')"
    if git diff --cached --quiet; then
        echo "No changes to commit."
    else
        echo "Committing changes..."
        git commit -m "$commit_message"
    fi
    # Step 7: Push all changes to the main branch
    echo "Deploying to GitHub Main..."
    if ! git push origin main; then
        echo "Failed to push to main branch."
        exit 1
    fi

fi

echo "All done! Site synced, processed, committed, built, and deployed."
