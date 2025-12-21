from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# Create the PDF
pdf_filename = "sma_historier.pdf"
doc = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4,
    rightMargin=25*mm,
    leftMargin=25*mm,
    topMargin=25*mm,
    bottomMargin=25*mm
)

# Container for the 'Flowable' objects
elements = []

# Define styles
styles = getSampleStyleSheet()

# Title style
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=48,
    textColor=HexColor('#1a1a1a'),
    spaceAfter=30,
    alignment=TA_CENTER,
    fontName='Helvetica-Bold'
)

subtitle_style = ParagraphStyle(
    'Subtitle',
    parent=styles['Normal'],
    fontSize=14,
    textColor=HexColor('#666666'),
    alignment=TA_CENTER,
    spaceAfter=20,
    fontName='Helvetica'
)

chapter_title = ParagraphStyle(
    'ChapterTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=HexColor('#1a1a1a'),
    spaceAfter=20,
    spaceBefore=30,
    fontName='Helvetica-Bold'
)

section_title = ParagraphStyle(
    'SectionTitle',
    parent=styles['Heading2'],
    fontSize=16,
    textColor=HexColor('#2c3e50'),
    spaceAfter=12,
    spaceBefore=20,
    fontName='Helvetica-Bold'
)

body_text = ParagraphStyle(
    'BodyText',
    parent=styles['Normal'],
    fontSize=11,
    textColor=HexColor('#2c3e50'),
    alignment=TA_JUSTIFY,
    spaceAfter=12,
    leading=18,
    fontName='Helvetica'
)

author_style = ParagraphStyle(
    'Author',
    parent=styles['Normal'],
    fontSize=10,
    textColor=HexColor('#666666'),
    fontName='Helvetica-Oblique',
    spaceAfter=20
)

story_number = ParagraphStyle(
    'StoryNumber',
    parent=styles['Normal'],
    fontSize=9,
    textColor=HexColor('#999999'),
    fontName='Helvetica',
    spaceAfter=10
)

# Title page
elements.append(Spacer(1, 100*mm))
elements.append(Paragraph("Små historier", title_style))
elements.append(Spacer(1, 20*mm))
elements.append(Paragraph("En samling af inspirerende fortællinger", subtitle_style))
elements.append(Spacer(1, 120*mm))
elements.append(Paragraph("Første udgave", subtitle_style))
elements.append(PageBreak())

# Table of Contents
elements.append(Paragraph("Indhold", chapter_title))
elements.append(Spacer(1, 20*mm))

# TOC table
toc_data = [
    ["Historie 1: Design af ikoniske produkter", "3"]
]

toc_table = Table(toc_data, colWidths=[140*mm, 20*mm])
toc_table.setStyle(TableStyle([
    ('ALIGN', (0,0), (0,-1), 'LEFT'),
    ('ALIGN', (1,0), (1,-1), 'RIGHT'),
    ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
    ('FONTSIZE', (0,0), (-1,-1), 11),
    ('TEXTCOLOR', (0,0), (-1,-1), HexColor('#333333')),
]))

elements.append(toc_table)
elements.append(PageBreak())

# Story 1
elements.append(Paragraph("HISTORIE 1", story_number))
elements.append(Paragraph("Design af ikoniske produkter", chapter_title))
elements.append(Paragraph("Af Linda Nhu Laursen, Aalborg Universitet", author_style))

# Story content
story_paragraphs = [
    "Velkommen til denne fortælling om, hvordan nogle af verdens bedste designere har skabt de mest ekstraordinære ikoniske produkter. Tænk på magretheskålen, PH-lampen eller Mini Cooperen – produkter der har bevaret deres design i årtier og fortsat forbliver relevante, elskede og værdsat. Dette er produkter, vi passer på og plejer, og som vi kan påstå er mere bæredygtige end mange andre.",

    "Hvordan finder designere egentlig på nye produkter? Mange kender til brainstormingsessioner med post-its, hvor man skal idégenerere bredt. Men sandheden er, at selv verdens bedste designere – top fem procent – får blokader ved overfladisk idégenerering. Deres idéer, koncepter og design er nemlig bygget på dybe indsigter.",

    "Forskerne Nigel Cross og Kees Dorst lavede et fascinerende protokolstudie med ni meget professionelle designere, som alle fik den samme opgave og information. Overraskende nok kom alle ni designere frem til præcis samme idé, som de hver især syntes var dybt original. Dette viser os, at det nytænkende og originale i design ikke nødvendigvis ligger i processen, men i de indsigter og informationer vi finder."
]

for para in story_paragraphs:
    elements.append(Paragraph(para, body_text))

elements.append(Paragraph("Mini Cooper – En evolution gennem tiden", section_title))

mini_cooper_paras = [
    "Mini Cooperen blev introduceret på markedet i 1957 efter Suezkrisen som en energieffektiv lille bil, der kunne rumme en hel familie. Den blev hurtigt ikonisk på det britiske marked og forblev populær i mange år.",

    "I 1994 købte BMW Rover Group og fik Minien med i købet – en bil der ikke var blevet opdateret i 40 år. Udfordringen var enorm: Hvordan fornyer man et britisk ikon uden at ødelægge det? Bilen skulle opdateres inden for tre år, ellers ville den blive taget af markedet på grund af sikkerhedskrav.",

    "BMW's løsning var unik og aldrig set før: De hyrede 15 designere fra hele verden, gav dem hver en måned til at designe og fem måneder til at modellere en fuld skala Mini. Designerne måtte ikke tale sammen. Efter et halvt år blev alle 15 biler udstillet, og én bil blev enstemmigt valgt – Frank Stephensons design.",

    "Stephensons tilgang var revolutionerende. I stedet for at bruge hele måneden på at designe den færdige bil, opdelte han tiden i årtier. Hver uge repræsenterede ti år: 1969, 1979, 1989 og 1999. Han brugte 80% af hver uge på at researche markedet, konteksten og brugerne for det pågældende årti, og kun 20% på selve designet. Faktisk brugte han kun tre dage på at designe den endelige bil.",

    "Gennem denne metode opdagede han vigtige indsigter: Folk var blevet 5 cm højere siden 1959, så kabinen skulle være højere. Køremønstrene havde ændret sig fra korte picnic-ture til længere rejser, så bagagerummet skulle være større. Og vigtigst: I 1999 var markedet fyldt med små biler, så Minien behøvede et unikt kendetegn – det blev det berømte 'bulldog-look' med den karakteristiske grill og brede stance."
]

for para in mini_cooper_paras:
    elements.append(Paragraph(para, body_text))

elements.append(Paragraph("LEGO Ninjago – At forstå børns meningsskabelse", section_title))

lego_paras = [
    "LEGO stod over for en anden udfordring: Hvordan fanger man action- og rollespilsinteresserede børn, som ikke naturligt er tiltrukket af byggeklodser? Tidligere havde de købt licenser som Star Wars, men nu ville de skabe deres eget univers.",

    "Designteamet startede med at lave mock-ups af forskellige universer – ørken, undervands, pirater og mere. De viste dem til 100 børn, men ikke for at få dem til at vælge. I stedet ville de forstå, hvordan børnene skabte mening med universerne.",

    "En lærerig observation kom, da en dreng placerede sin yndlingsdyr – en krokodille og en løve – i ørkenuniverset. Andre børn kunne ikke deltage i legen, fordi det ikke gav mening for dem. Teamet lærte, at et godt univers skal være tilgængeligt for mange børn, ikke kun enkelte.",

    "Ved at studere succesfulde universer som Lion King og Toy Story fandt de, at de bedste historier byggede på velkendte verdener med et twist. Ninja Turtles var ninjaer der var skildpadder. Kung Fu Panda var en tyk panda med martial arts-evner.",

    "Da de testede deres ninja-koncept i en moderne storby med drager som modstandere, opdagede de vigtige indsigter: Børnene elskede de futuristiske biler, men syntes det var unfair at kæmpe mod drager. Museumsartefakter som mål gav ingen mening for syvårige. Løsningen blev et gyldent sværd som mål, og dragerne skulle være på ninjaernes side, ikke imod dem."
]

for para in lego_paras:
    elements.append(Paragraph(para, body_text))

elements.append(Paragraph("To eksperttilgange til designindsigter", section_title))

conclusion_paras = [
    "Disse historier illustrerer to kraftfulde tilgange til at finde unikke designindsigter:",

    "<b>Første tilgang: Kom ud over dine antagelser.</b> Som Frank Stephenson viste, skal vi researche dybt i markedet, konteksten og brugernes udvikling over tid. Hvis vi kun ser det samme som andre har set, tegner vi det samme som andre har tegnet.",

    "<b>Anden tilgang: Forstå brugerens meningsskabelse.</b> Som LEGO Ninjago-teamet demonstrerede, kan vi ikke bare spørge brugere hvad de vil have. Som Henry Ford sagde: 'If I asked people what they want, they would have said a faster horse.' Vi må lave prototyper og mock-ups, ikke for at få brugerne til at vælge, men for at forstå hvad der giver mening for dem, hvad de afviser, og vigtigst – hvorfor.",

    "Disse to tilgange – at søge dybe, unikke indsigter og at forstå brugerens meningsskabelse – er hemmeligheden bag design af virkelig ikoniske produkter. Det er ikke nok at være kreativ; vi må forstå verden på nye måder for at skabe noget virkelig nytænkende."
]

for para in conclusion_paras:
    elements.append(Paragraph(para, body_text))

# Build the PDF
doc.build(elements)
print(f"PDF created successfully: {pdf_filename}")