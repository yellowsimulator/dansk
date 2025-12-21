from weasyprint import HTML, CSS

# Read the HTML file
with open('sma_historier.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Create PDF from HTML
HTML(string=html_content).write_pdf('sma_historier.pdf')

print("PDF created successfully: sma_historier.pdf")