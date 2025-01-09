from polls.models import Article

def populate_articles():
    articles = [
        {'title': 'Kolumba Street is Open Now', 'content': 'Details about the opening...'},
        {'title': 'Buildings Are Rising at Kępa Parnicka', 'content': 'Details about buildings...'},
        {'title': '55m Building Rising in Pomorzany', 'content': 'Details about the new building...'},
        {'title': 'Szczecin Goleniów Airport Renovation', 'content': 'Details about the renovation...'},
        {'title': 'New Flights and Connections from Szczecin', 'content': 'Details about new connections...'},
    ]

    for article in articles:
        Article.objects.create(**article)
    print("Articles populated!")
