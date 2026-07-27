#!/bin/bash
# publish-blog.sh — Validate and publish a blog post to furdbase.com
# Usage: ./publish-blog.sh src/content/blog/your-post.md

set -e

POST_FILE="$1"

if [ -z "$POST_FILE" ]; then
  echo "Usage: ./publish-blog.sh src/content/blog/your-post.md"
  exit 1
fi

if [ ! -f "$POST_FILE" ]; then
  echo "Error: File not found: $POST_FILE"
  exit 1
fi

# Extract frontmatter
FRONTMATTER=$(sed -n '/^---$/,/^---$/p' "$POST_FILE" | sed '1d;$d')

# Validate required fields
for field in title description pubDate image; do
  VALUE=$(echo "$FRONTMATTER" | grep "^$field:" | head -1 | sed "s/^$field: *//;s/^\"//;s/\"$//")
  if [ -z "$VALUE" ]; then
    echo "Error: Missing required field: $field"
    exit 1
  fi
done

# Check image exists
IMAGE=$(echo "$FRONTMATTER" | grep "^image:" | head -1 | sed 's/^image: *//;s/^"//;s/"$//')
if [ ! -f "public$IMAGE" ]; then
  echo "Error: Image not found: public$IMAGE"
  exit 1
fi

# Get slug from filename
SLUG=$(basename "$POST_FILE" .md)
TITLE=$(echo "$FRONTMATTER" | grep "^title:" | head -1 | sed 's/^title: *//;s/^"//;s/"$//')

echo "Publishing: $TITLE"
echo "Slug: $SLUG"
echo "Image: $IMAGE"

# Build to verify no errors
echo "Building..."
npm run build --silent

# Commit and push
git add "$POST_FILE"
git add "public$IMAGE" 2>/dev/null || true
git commit -m "blog: $TITLE"
git push origin main

echo ""
echo "Done! Post will be live at https://furdbase.com/blog/$SLUG in ~60 seconds."
