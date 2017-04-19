from bs4 import BeautifulSoup

# Open HTML file
soup = BeautifulSoup(open('index.html'), 'html.parser')

# Do some cleanup
[x.extract() for x in soup.find_all("a", class_="lien-retour-haut")]

# Retrieve programmes div
compa_div = soup.find_all(id="comparateur-de-programmes")[0]

# Retrieve program sections
sections = compa_div.find_all('section', class_="conteneur-large")

for section in sections:
    # Extract section title
    title = section.find_all("strong",
                             class_="titre-section")[0].get_text().strip()
    
    print("<section>")
    print("  <section>")
    print("    <h2>" + title + "</h2>")
    print("  </section>")

    # Extract questions
    questions = section.find_all("article")

    # Parse all questions
    for question in questions:
        
        # Extract question information
        qtitle = question.select("h2")[0].get_text().strip()
        qdescription = question.find_all("p",
                                         class_="paragraphe")[0].get_text().strip()
        qlink = question.find_all("a", class_="paragraphe")[0]

        print("<section>")
        print("<h3>" + qtitle + "</h3>")
        print("<blockquote>" + qdescription + "</blockquote>")

        # Extract answers
        answers = question.select("div.table-comparaison > div.groupement")

        print("<ul>")
        # Parse all answers
        for answer in answers:
            aposition = answer.select("span.position")[0].get_text().strip()
            acandidats = [ figure['data-filter'] for figure in
                          answer.select("figure.support-infobulle")]
            
            if len(acandidats) > 0 and aposition != "Pas de position publique connue":
                print("<li class='answer' data-candidat=\"" + str(acandidats) +
                      "\"><a href='javascript:void(0)'>" + aposition + "</a></li>")
        
        print("</ul>")
        print("</section>")

    print("</section>")
