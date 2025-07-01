#!/usr/bin/env python3
"""
Convert newsletter HTML files to Jekyll markdown posts
"""

import os
import re
import shutil
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import html2text
from urllib.parse import unquote

def clean_title(filename):
    """Extract and clean title from filename"""
    # Remove ID and .html extension
    title = re.sub(r'^\d+_', '', filename)
    title = title.replace('.html', '')
    
    # Clean up special characters
    title = title.replace('_', ' ')
    title = unquote(title)  # Handle URL encoding
    
    return title.strip()

def extract_content_from_html(html_content):
    """Extract main content from HTML, removing newsletter elements"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the main content area (after the header table)
    content_elements = []
    
    # Look for paragraphs and blockquotes in the main content area
    main_div = soup.find('div', class_='page')
    if main_div:
        # Skip the web link, title, and author table
        skip_title = True  # Skip the first h1 element (title)
        for element in main_div.find_all(['p', 'blockquote', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            # Skip elements that contain newsletter-specific content
            text = element.get_text().strip()
            if ('不想再收到来自' in text or 
                '竹白' in text or 
                '点击在浏览器中访问' in text or
                element.find('img', alt='logo')):
                continue
            
            # Skip the first h1 element (which is the title)
            if element.name == 'h1' and skip_title:
                skip_title = False
                continue
            
            content_elements.append(element)
    
    # Convert to markdown
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.body_width = 0  # Don't wrap lines
    
    markdown_content = ""
    for element in content_elements:
        element_html = str(element)
        # Fix image paths
        element_html = re.sub(r'src="images/', r'src="/images/', element_html)
        # Remove newsletter URL placeholders
        element_html = re.sub(r'%recipient\.zhubai_url_\d+%', '#', element_html)
        element_html = re.sub(r'%recipient\.unsubscribe_url%', '#', element_html)
        markdown_content += h.handle(element_html) + "\n"
    
    return markdown_content.strip()

def generate_description(content, title):
    """Generate a description from the content"""
    # Take first paragraph or first 150 characters
    lines = content.split('\n')
    first_para = ""
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            first_para = line
            break
    
    if len(first_para) > 150:
        first_para = first_para[:147] + "..."
    
    return first_para or f"A newsletter post about {title}"

def create_jekyll_post(html_file, output_dir, post_date):
    """Convert single HTML file to Jekyll markdown post"""
    
    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Extract title from filename
    filename = os.path.basename(html_file)
    title = clean_title(filename)
    
    # Extract content
    content = extract_content_from_html(html_content)
    
    # Generate description
    description = generate_description(content, title)
    
    # Create Jekyll frontmatter
    frontmatter = f"""---
date: {post_date.strftime('%Y-%m-%d')}
layout: post
title: "{title}"
description: "{description}"
categories: [Newsletter]
---

"""
    
    # Create output filename
    clean_title_for_filename = title.replace(' ', '-').replace('/', '-').replace(':', '-').replace('?', '').replace('!', '').replace('"', '').replace(''', '').replace(''', '').replace('—', '-').replace('–', '-').lower()
    post_filename = f"{post_date.strftime('%Y-%m-%d')}-{clean_title_for_filename}.md"
    post_path = os.path.join(output_dir, post_filename)
    
    # Write Jekyll post
    with open(post_path, 'w', encoding='utf-8') as f:
        f.write(frontmatter + content)
    
    print(f"Created: {post_filename}")
    return post_path

def copy_images(content_dir, images_dir):
    """Copy images from content/images to main images directory"""
    source_images = os.path.join(content_dir, 'images')
    if os.path.exists(source_images):
        for img_file in os.listdir(source_images):
            src_path = os.path.join(source_images, img_file)
            dst_path = os.path.join(images_dir, img_file)
            if not os.path.exists(dst_path):
                shutil.copy2(src_path, dst_path)
                print(f"Copied image: {img_file}")

def main():
    # Directories
    content_dir = "/Users/zhengchen/GitHub/liamchzh.github.com/content"
    posts_dir = "/Users/zhengchen/GitHub/liamchzh.github.com/_posts"
    images_dir = "/Users/zhengchen/GitHub/liamchzh.github.com/images"
    
    # Get all HTML files and sort them
    html_files = []
    for filename in os.listdir(content_dir):
        if filename.endswith('.html'):
            html_files.append(filename)
    
    # Sort by the ID at the beginning of filename
    html_files.sort(key=lambda x: int(x.split('_')[0]))
    
    # Start date
    start_date = datetime(2023, 1, 1)
    
    # Convert each file
    for i, filename in enumerate(html_files):
        html_path = os.path.join(content_dir, filename)
        post_date = start_date + timedelta(days=i)
        
        create_jekyll_post(html_path, posts_dir, post_date)
    
    # Copy images
    copy_images(content_dir, images_dir)
    
    print(f"\nConverted {len(html_files)} newsletter posts!")
    print(f"Posts created from {start_date.strftime('%Y-%m-%d')} to {(start_date + timedelta(days=len(html_files)-1)).strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()