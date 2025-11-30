import os

print("Name of website:")
NOW = input("> ")

base_path = "/home/zackdcat/Everything/Applications/Projects/Websites"
folder_name = NOW
folder_path = os.path.join(base_path, folder_name)

os.makedirs(folder_path, exist_ok=True)

# HTML content
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{NOW}</title>
    <link href="https://fonts.googleapis.com/css2?family=Momo+Trust+Display&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <h3>{NOW}</h3>
</body>
</html>
"""

# CSS content
css_content = """body {
    background-color: #f0f0f0;
    font-family: "Momo Trust Display", sans-serif;
}

h3 {
    position: absolute;
    font-family: "Momo Trust Display", sans-serif;
    left: 2.5%;
    color: #000000;
    font-size: 10vw;
    margin: 0%;
}
"""

js_content = ""

# Full paths to files
html_file_path = os.path.join(folder_path, "index.html")
css_file_path = os.path.join(folder_path, "index.css")
js_file_path = os.path.join(folder_path, "index.js")

# Write HTML file
with open(html_file_path, "w") as f:
    f.write(html_content)

# Write CSS file
with open(css_file_path, "w") as f:
    f.write(css_content)

# Write CSS file
with open(js_file_path, "w") as f:
    f.write(js_content)

print(f"Website folder and files created at: {folder_path}")
