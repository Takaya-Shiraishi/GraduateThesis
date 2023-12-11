import sys

def markdown_to_html(markdown_text):
    lines = markdown_text.split('\n')
    html_list = ['<ul>']
    for line in lines:
        if '- [ ]' in line:
            content = line.replace('- [ ]', '').strip()
            html_list.append(f'<li><input type="checkbox"> {content}</li>')
    html_list.append('</ul>')
    return '\n'.join(html_list)

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        markdown_text = file.read()

    html_output = markdown_to_html(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_output)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_md.py input.md output.md")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
