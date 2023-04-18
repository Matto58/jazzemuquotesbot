import asyncio
import discord
import random

quotes = [
	{"content": "Will the DVD logo come to life and hold me like I held my wife?", "song": "Still Waiting", "year": "2022"},
	{"content": "Maybe the CEO of Apple, Tim Cook, is secretly a potato who's worked his way up to the boardroom", "song": "Potato", "year": "2021"},
	{"content": "Bluetooth headphones weren't connected (that shit was blaring out)", "song": "Vibe It Out", "year": "2021"},
	{"content": "Friedrich Nietzsche, you can eat your heart out, I'm the ubermensch", "song": "Hench", "year": "2020"},
]
songs = [
	{"name": "Still Waiting", "year": "2022", "link": {
		"youtube": "https://www.youtube.com/watch?v=_ws0QtAiiXQ",
		"spotify": "https://open.spotify.com/track/6SgV1QuN8SS2sgke9csXUF",
		"applemusic": "https://music.apple.com/us/album/still-waiting/1629834319?i=1629834320",
	}},
	{"name": "Light Touch", "year": "2019", "link": {
		"youtube": "https://www.youtube.com/watch?v=oHlblAfSnnE",
		"spotify": "https://open.spotify.com/track/103JwfhF9fCfOczGPzOJeV",
		"applemusic": "https://music.apple.com/us/album/light-touch/1470486075?i=1470486076",
	}},
	{"name": "Funkbot 10,000", "year": "2022", "link": {
		"youtube": "https://www.youtube.com/watch?v=WjJ4ZplV-kw",
		"spotify": "https://open.spotify.com/track/4zshoFyr7RB7oOItKUQYtT",
		"applemusic": "https://music.apple.com/us/album/funkbot-10-000/1575507627?i=1575507628",
	}},
	{"name": "Allergic", "year": "2021", "link": {
		"youtube": "https://www.youtube.com/watch?v=uiH9GTkcWNI",
		"spotify": "https://open.spotify.com/track/5P6SUffypAPVBKPc2KYByU",
		"applemusic": "https://music.apple.com/us/album/allergic/1541033750?i=1541033752",
	}},
	{"name": "My Brothe", "year": "2021", "link": {
		"youtube": "https://www.youtube.com/watch?v=dmss2dJ__cI",
		"spotify": "https://open.spotify.com/track/4VcRyck8nIcqnYu3kfW8AC",
		"applemusic": "https://music.apple.com/us/album/my-brothe/1562336112?i=1562336113",
	}},
	{"name": "Sexier", "year": "2020", "link": {
		"youtube": "https://www.youtube.com/watch?v=3pdXvrxyVIA",
		"spotify": "https://open.spotify.com/track/3skRg9wYHlW9SCA4qpWNwZ",
		"applemusic": "https://music.apple.com/us/album/sexier/1493224176?i=1493224189",
	}},
	{"name": "Potato", "year": "2021", "link": {
		"youtube": "https://www.youtube.com/watch?v=4MEXP-DlDmA",
		"spotify": "https://open.spotify.com/track/2DR52dvz8GW9nE21T4LxVX",
		"applemusic": "https://music.apple.com/us/album/potato/1578797995?i=1578798005",
	}},
]
settings = {
	"quoteAutopop": "0",
	"pingOnOutput": "1",
	"songLink": "spotify",
}
prefix = "j!"
owner = 429289365361917963  # Matto58#8774
botId = 1097601477310173276 # Jazz Emu Quotes Bot#9292

class JazzEmuClient(discord.Client):
	async def on_ready(self):
		print(f"{self.user} is ready to funk up your server!")

	async def on_message(self, message: discord.Message):
		if message.content[:len(prefix)] == prefix:
			if message.author.id != botId:
				print(f"{message.guild.name}/#{message.channel.name}/{message.author.name}#{message.author.discriminator}: {message.content}")

			#print("Command detected!")
			cmdOut = self.JazzEmuBot_command(message.author, message.content[len(prefix):])
			#print(cmdOut)
			await message.channel.send(cmdOut)

	def JazzEmuBot_command(self, msgAuthor: discord.User, cmd: str):
		ln = cmd.split(" ")
		#print(ln[0])

		if ln[0] == "quote":
			if len(quotes) == 0:
				return f"{self.userping(msgAuthor)} | Hey <@{owner}>, your bot ran out of quotes! Restart it please!"

			quoteInx = random.randint(0, len(quotes)-1)
			#print(quoteInx)

			quote = quotes[quoteInx]

			(quoteContent, quoteSong, quoteYear) = (quote["content"], quote["song"], quote["year"])

			if settings["quoteAutopop"] == "1": quotes.pop(quoteInx)

			return (
				f"> *{quoteContent}*\n" +
				f"-- Jazz Emu in '{quoteSong}', {quoteYear}\n" +
				f"Quote requested by {self.userping(msgAuthor)}"
			)
		elif ln[0] == "song":
			song = random.choice(songs)

			(songName, songYear, songLink) = (song["name"], song["year"], song["link"][settings["songLink"]])

			return (
				f"**{songName}** ({songYear})\n" +
				f"{songLink}\n" +
				f"Song requested by {self.userping(msgAuthor)}"
			)
		elif ln[0] == "settings":
			if msgAuthor.id != owner:
				return f"{self.userping(msgAuthor)} | Only the owner of this bot ({self.get_user(owner).name}) can use this command!"
				
			oldValue = settings[ln[1]]
			newValue = " ".join(ln[2:])

			settings[ln[1]] = newValue

			return f"{self.userping(msgAuthor)} | Setting `{ln[1]}` has been set from `{oldValue}` to `{newValue}`!"
		elif ln[0] == "shutdown":
			if msgAuthor.id != owner:
				return f"{self.userping(msgAuthor)} | Only the owner of this bot ({self.get_user(owner).name}) can use this command!"
			
			exit(0)
			
		return f"{self.userping(msgAuthor)} | Unknown command: {ln[0]}"

	def userping(self, user: discord.User):
		return f"<@{user.id}>" if settings["pingOnOutput"] == "1" else f"**{user.display_name}**"


client = JazzEmuClient(intents=discord.Intents.all())

async def main():
	print("Jazz Emu Quotes Bot for Discord - funking up your server since 2023")

	try:
		tokenfl = open(".token", "r")
	except:
		print("File .token not found!")
		exit(1)

	await client.start(tokenfl.read())
	tokenfl.close()

if __name__ == "__main__":
	try:
		c = main()
		asyncio.run(c)
	except KeyboardInterrupt or SystemExit:
		pass
