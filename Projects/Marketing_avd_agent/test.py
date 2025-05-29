import markdown
import pdfkit

# Markdown content or file
markdown_text = """
# Sample Markdown

This is a **bold** text and this is *italic*.

- Item 1
- Item 2

[Link to OpenAI](https://openai.com)
"""

# Convert markdown to HTML
html_text = markdown.markdown(markdown_text)

# Save HTML to temporary file (optional)
with open("temp.html", "w") as f:
    f.write(html_text)

# Convert HTML to PDF
pdfkit.from_string(html_text, "output.pdf")

print("PDF saved as output.pdf")
