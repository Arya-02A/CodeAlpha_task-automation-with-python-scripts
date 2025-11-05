import re

def extract_emails(input_file, output_file):
    # Read the content of the file
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    # Regular expression to find emails
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Extract all matching email addresses
    emails = re.findall(pattern, text)

    # Remove duplicates (optional)
    emails = list(set(emails))

    # Save to output file
    with open(output_file, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")

    print(f"✅ Extracted {len(emails)} email(s) and saved to {output_file}")


input_txt = input("Enter the path of the .txt file : ").strip()
extract_emails(input_txt, "emails_output.txt")
