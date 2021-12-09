


from discord_webhook import DiscordWebhook, DiscordEmbed
import time, logging, sys
import scraping




url="" # Insert Discord Webhook URL here





def main():
	scraper = scraping.CovidScraper()


	while True:

		discmessage = DiscordEmbed(title="Daily SG Covid-19 Update", color='ed2939')
    
        discmessage.set_footer(name='MohScraperBot by JiBot#7904')
    
        discmessage.set_timestamp()
        discmessage.add_embed_field(name="Update", value=scraper.getcontents())

    
        webhook = DiscordWebhook(url=url, username = "COVID-19 Updates")
        webhook.add_embed(discmessage)
        response = webhook.execute()

        scraper.quit()

        time.sleep(86400)

        scraper.reopen_page()


if __name__ == "__main__":
	main()