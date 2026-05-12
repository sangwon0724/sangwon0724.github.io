import os
import re

def fix_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {path}: {e}")
        return False
        
    original_content = content
    
    # 1. Add alt="" to <img> tags missing alt attribute
    # Handle both <img ... > and <img ... />
    def img_replace(match):
        tag = match.group(0)
        # Check if 'alt=' (case-insensitive) is present
        if not re.search(r'alt\s*=', tag, re.IGNORECASE):
            if tag.endswith('/>'):
                return tag[:-2] + ' alt="" />'
            else:
                return tag[:-1] + ' alt="" >'
        return tag

    content = re.sub(r'<img[^>]+>', img_replace, content)
    
    # 2. Upgrade HTTP to HTTPS for specific domains
    domains = [
        'redisgate.kr', 
        'regexr.com', 
        'jekyllthemes.org', 
        'tomcat.apache.org', 
        'hibernate.org', 
        'gskinner.com'
    ]
    for d in domains:
        content = content.replace(f'http://{d}', f'https://{d}')
        content = content.replace(f'http://www.{d}', f'https://www.{d}')
    
    if content != original_content:
        try:
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error writing {path}: {e}")
            return False
    return False

def main():
    posts_dir = '_posts'
    fixed_count = 0
    for root, dirs, files in os.walk(posts_dir):
        for file in files:
            if file.endswith(('.md', '.markdown')):
                full_path = os.path.join(root, file)
                if fix_file(full_path):
                    print(f"Fixed: {full_path}")
                    fixed_count += 1
    print(f"Total fixed files: {fixed_count}")

if __name__ == "__main__":
    main()
