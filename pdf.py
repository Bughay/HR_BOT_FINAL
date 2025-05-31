from PyPDF2 import PdfReader

reader = PdfReader("/home/lordmark1/Desktop/aziza_resume.pdf")


def pdf_extractor(reader):
    reader = reader
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    return text


text = pdf_extractor(reader)

job_reqs = """


Holding company is a private equity fund and in-house incubator that is investing and cultivating startup companies to bring them into the global markets (headcount up to 80 people).

We are seeking a highly analytical and detail-oriented Market Analyst to lead the market research efforts and competitive analysis for our organization. The candidate will be responsible for comprehensive market studies, competitor evaluation, and generating actionable insights to support strategic decision-making. This role involves working closely with internal stakeholders to highlight our competitive positioning, in various technologies mainly in oil and gas, medical gases, renewable energy, automotive, wast-to-energy. This role requires a proactive individual with a keen eye for detail, the ability to interpret and complex data and to translate findings into actionable strategies.

Office work 3-5 days a week (метро Проспект Мира - 5 minutes walk from the metro)

Key Responsibilities:

    Market Research & Competitor Analysis:
        Conduct detailed analysis of primary competitors with significant market share, identifying their competitive advantages, customer preferences, sales volume and market share among competitors.
        Analyze market data to identify key insights and industry trends.
        Evaluate and compare our technology with competitor technologies, outlining strengths, weaknesses, and competitive edges.
        Prepare presentations on market analysis in well organized and systematic manner.
    Presentation Development:
        Compile findings and analysis and create clear, visually compelling, and data-driven presentations that support strateguc business decisions.
        Present findings and recommendations to stakeholders, including leadership teams.

Position Requirements:

    Proven experience in market analysis, competitive intelligence, or a similar analytical role.
    Strong analytical skills and communication skills.
    Strong proficiency in research tools, data visualization software, and Microsoft Office Suite (Excel, PowerPoint).
    Bachlor degree in Business management/MBA or economic or or marketing or statistic or data analytics or industrial engineering.
    Excellent English writing and good speaking - MUST.


"""