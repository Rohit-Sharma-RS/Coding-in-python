from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Your Name', 0, 1, 'C')
    
    def add_section_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(5)
    
    def add_text(self, text):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 10, text)
        self.ln(5)
    
    
    def add_hyperlink(self, title, link):
        self.set_text_color(0, 0, 255)  # Blue color for hyperlinks
        self.set_font('Arial', 'U', 11)  
        self.cell(0, 10, title, 0, 1, 'L', link=link)
        self.set_text_color(0, 0, 0)  
        self.ln(5)


pdf = PDF()


pdf.add_page()


pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Your Name', 0, 1, 'C')


pdf.add_section_title('Contact Information')
pdf.add_text('Email: your.email@example.com\nPhone: +91 12345 67890\nLinkedIn: linkedin.com/in/yourprofile')


pdf.add_section_title('Projects')
pdf.add_hyperlink('Carbon Emission Project (Smart India Hackathon)', 'http://yourprojectlink.com')
pdf.add_hyperlink('WBJEE Study Materials', 'http://yoursecondprojectlink.com')


pdf.add_section_title('Education')
pdf.add_text('B.Tech in Computer Science, XYZ University\nYear: 2020-2024')


pdf.add_section_title('Skills')
pdf.add_text('Python, Machine Learning, Web Development, Data Analysis')


pdf.output("resume_with_links.pdf")
