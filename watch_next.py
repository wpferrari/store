import spacy

nlp = spacy.load('en_core_web_md')
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati " \
              "trick Hulk into a shittle and launch him into space to a planet where the Hulk can live in peace. " \
              "Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator"
movies = []
with open('movies.txt', 'r') as db:
    for l in db.readlines():
        movies.append(l.strip().split(':'))

desc_to_compare = nlp(description)
higher_similarity = 0
for l in movies:
    similarity = nlp(l[1]).similarity(desc_to_compare)
    if similarity > higher_similarity:
        higher_similarity = similarity
        next_movie = l

print('Next movie to watch:')
print(next_movie[0], '-', next_movie[1])

