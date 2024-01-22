import subprocess

def try_code(code):
    command = ["./testBrute"]  # Replace './testBrute' with the actual path
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    process.stdin.write(f"{code}\n")
    process.stdin.flush()

    result, _ = process.communicate()

    return result.strip()

def main():
    wordlist_path = '/usr/share/wordlists/rockyou.txt'  # Adjust the path to the wordlist

    with open(wordlist_path, 'r', errors='replace') as f:
        wordlist = [line.strip() for line in f]

    for word in wordlist:
        result = try_code(word)

        if "Access denied" not in result: #change "Acess denied" to the actual error output your program gives
            print(f"Flag found for code {word}: {result}")
            break
        else:
            print(f"Access denied for code {word}")

if __name__ == "__main__":
    main()
