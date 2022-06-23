import re

def mark():
    my_pattern = "[\w\d\s\$\&\+\,\:\;\=\?\@\#\|\<\>\.\^\*\(\)\%\!\-\\\/]"
    content = ''
    output = ''
    comment_opened = False
    with open('exemple.py', 'r') as f:
        content = f.read()
    for line in content.split('\n'):
        if not line.strip().startswith('#'):
            matches = re.findall(f'\"[^\"][^\"]{my_pattern}+\"|\'[^\'][^\']{my_pattern}+\'|\(\".+\"+\)', line)
            for word in matches:
                line = line.replace(word, f"_({word})")
            output += line + "\n"
        else:
            output += line + "\n"
    with open('result.py', 'w') as f:
        f.write(output )
       




if __name__ == '__main__':
    mark()