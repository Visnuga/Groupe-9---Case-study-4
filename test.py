from bs4 import BeautifulSoup
import difflib

# # Ouvrir le fichier HTML et le lire
# with open('example.html', 'r') as file:
#     html = file.read()

# # Créer un objet BeautifulSoup à partir du HTML
# soup = BeautifulSoup(html, 'html.parser')

# # Supprimer tous les scripts de la page
# for script in soup(["script", "style"]):
#     script.decompose()

# # Supprimer tous les styles de la page
# for style in soup(["style"]):
#     style.decompose()

# # Écrire le HTML nettoyé dans un nouveau fichier
# with open('cleaned.html', 'w') as file:
#     file.write(str(soup))

with open("example.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

# Suppression des balises de style (CSS)
for style in soup(["style"]):
    style.decompose()

# Suppression des scripts (JavaScript)
for script in soup(["script"]):
    script.decompose()

# Suppression des balises inutiles
for link in soup(["a", "link", "nav", "footer", "header", "section", "form", "noscript", "i", "button"]):
    link.decompose()

# Suppression de la div avec l'ID "col-fixed"
div_col_fixed = soup.find('div', {'id': 'col-fixed'})
if div_col_fixed:
    div_col_fixed.decompose()

# Suppression de la div avec l'ID "pc-policy-text"
div_col_fixed = soup.find('div', {'id': 'pc-policy-text'})
if div_col_fixed:
    div_col_fixed.decompose()

# Suppression de la div avec l'ID "apply-bottom-content"
div_col_fixed = soup.find('div', {'id': 'apply-bottom-content'})
if div_col_fixed:
    div_col_fixed.decompose()

# Suppression de la div avec l'ID "accept-recommended-container"
div_col_fixed = soup.find('div', {'id': 'accept-recommended-container'})
if div_col_fixed:
    div_col_fixed.decompose()

# Suppression de la h3 avec l'ID "pc-title"
div_col_fixed = soup.find('h3', {'id': 'pc-title'})
if div_col_fixed:
    div_col_fixed.decompose()

# Suppression de la h3 avec l'ID "seperate-bottom normal"
div_col_fixed = soup.find('p', {'class': 'seperate-bottom normal'})
if div_col_fixed:
    div_col_fixed.decompose()

# Récupération du texte restant
text = soup.get_text()

# text = " ".join(text.split())
text = "\n".join([line for line in text.split("\n") if line.strip()])

with open('cleaned.txt', 'w') as file:
    file.write(str(text))








# Ouvrir le fichier contenant les skills à chercher
with open("cleaned.txt", "r") as f:
    other_content = f.read()

# Trouver la partie de other_content qui suit la première occurrence de "Recommended Skills"
start_index = other_content.find("Recommended Skills")
if start_index != -1:
    other_content = other_content[start_index:]

# Ouvrir le fichier contenant le CV
with open("cv.txt", "r") as f:
    cv_content = f.read()

# Trouver la partie de cv_content qui suit la première occurrence de "Skills"
start_index = cv_content.find("Skills")
if start_index != -1:
    cv_content = cv_content[start_index:]

# Séparer les skills en une liste
other_skills = [skill.strip() for skill in other_content.split("\n") if len(skill.strip()) > 4]
cv_skills = [skill.strip() for skill in cv_content.split("\n") if len(skill.strip()) > 4]

# Trouver les correspondances les plus proches pour chaque skill
for skill in cv_skills:
    closest_matches = difflib.get_close_matches(skill, other_skills, n=1, cutoff=0.6)
    if closest_matches:
        print(f"Le skill '{skill}' a une correspondance proche avec '{closest_matches[0]}' dans l'autre fichier.")
    else:
        print(f"Le skill '{skill}' n'a pas de correspondance proche dans l'autre fichier.")

# Trouver les skills dans other_skills qui ne sont pas dans cv_skills
missing_skills = set(other_skills) - set(cv_skills)
if missing_skills:
    print("\nLes skills suivants sont dans l'autre fichier mais pas dans le CV :")
    for skill in missing_skills:
        print(f"- {skill}")
else:
    print("\nTous les skills de l'autre fichier sont dans le CV.")