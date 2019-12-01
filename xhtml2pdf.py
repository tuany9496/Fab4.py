from wkhtmltopdf import WKHtmlToPdf

wkhtmltopdf = WKHtmlToPdf(
    url='http://google.com',
    output_file='~/example.pdf',
)
wkhtmltopdf.render()


def main():
    wkhtmltopdf
