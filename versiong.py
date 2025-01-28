import scrapy

class NBALeaderSpider(scrapy.Spider):
    name = "nba_leaders"
    start_urls = ["https://basketball-reference.com/leagues/NBA_2025_leaders.html"]

    def parse(self, response):
        categories = {
            "Points": "leaders_pts",
            "Rebounds": "leaders_trb",
            "Assists": "leaders_ast",
            "Blocks": "leaders_blk"
        }

        # Créer une liste pour les phrases formatées
        phrases = []

        for category, div_id in categories.items():
            # Extraire le nom du joueur
            player_name = response.xpath(f'//div[@id="{div_id}"]//td[@class="who"]/a/text()').extract_first()
            
            # Extraire l'équipe du joueur
            team = response.xpath(f'//div[@id="{div_id}"]//td[@class="who"]/span[@class="desc"]/text()').extract_first()
            
            # Extraire la valeur de la statistique
            value = response.xpath(f'//div[@id="{div_id}"]//td[@class="value"]/text()').extract_first()

            # Construire une phrase formatée
            phrase = f"Le leader pour {category} est {player_name} de l'equipe {team} avec {value} {category.lower()}."
            phrases.append(phrase)

        # Ajouter une ligne vide entre chaque catégorie
        message = phrases

        # Afficher le message formaté avec des sauts de ligne
        self.log(f"\n{message}")

        # Retourner les résultats
        yield {'message': message}