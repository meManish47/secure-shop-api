import os
import sys

def process_files(fix=False):
    ignore_dirs = {'.git', '__pycache__', 'venv', 'env', 'node_modules'}
    count = 0
    files_with_issues = []

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        for file in files:
            if not file.endswith(('.py', '.md', '.txt')):
                continue
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check for literal \n at the end of lines
                lines = content.splitlines(keepends=True)
                new_lines = []
                file_has_issue = False
                file_count = 0
                
                for line in lines:
                    # A line ends with actual newline '\n' (if not last line without it)
                    # We want to find literal '\n' at the very end of the text.
                    # so if line ends with '\\n\n' or '\\n'
                    orig_line = line
                    if line.endswith('\\n\n'):
                        line = line[:-3] + '\n'
                        file_has_issue = True
                        file_count += 1
                    elif line.endswith('\\n'):
                        line = line[:-2]
                        file_has_issue = True
                        file_count += 1
                    
                    # Also handle the case where a line is exactly '\n\n' or just '\n' literally
                    if orig_line.strip() == '\\n':
                        # if the line is literally just \n (with or without actual newline)
                        line = orig_line.replace('\\n', '')
                        file_has_issue = True
                        # If we already counted it above, don't double count
                        if not orig_line.endswith('\\n\n') and not orig_line.endswith('\\n'):
                            file_count += 1

                    new_lines.append(line)
                
                if file_has_issue:
                    files_with_issues.append((path, file_count))
                    count += file_count
                    if fix:
                        with open(path, 'w', encoding='utf-8') as f:
                            f.writelines(new_lines)
                            
            except Exception as e:
                print(f"Error reading {path}: {e}")

    return count, files_with_issues

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'count'
    fix = mode == 'fix'
    count, issues = process_files(fix)
    
    if fix:
        print(f"Fixed {count} unnecessary literal '\\n's in {len(issues)} files.")
    else:
        print(f"Found {count} unnecessary literal '\\n's in {len(issues)} files:")
        for path, c in issues:
            print(f"{path}: {c} occurrences")
