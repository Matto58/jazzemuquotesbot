import asyncio
import discord
import random

quotes = [
	{"content": "Will the DVD logo come to life and hold me like I held my wife?", "song": "Still Waiting", "year": "2022"},
	{"content": "Maybe the CEO of Apple, Tim Cook, is secretly a potato who's worked his way up to the boardroom", "song": "Potato", "year": "2021"},
	{"content": "Bluetooth headphones weren't connected (that shit was blaring out)", "song": "Vibe It Out", "year": "2021"}
]
settings = {
	"quoteAutopop": "0",
	"pingOnOutput": "1"
}
prefix = "j!"
owner = 429289365361917963  # Matto58#8774
botId = 1097601477310173276 # Jazz Emu Quotes Bot#9292

class JazzEmuClient(discord.Client):
	async def on_ready(self):
		print(f"{self.user} is ready to funk up your server!")

	async def on_message(self, message: discord.Message):
		if message.author.id != botId:
			print(f"{message.guild.name}/#{message.channel.name}/{message.author.name}#{message.author.discriminator}: {message.content}")

		if message.content[:len(prefix)] == prefix:
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
			
			print("Shutdown requested")
			exit(0)
			
		return f"{self.userping(msgAuthor)} | Unknown command: {ln[0]}"

	def userping(self, user: discord.User):
		return f"<@{user.id}>" if settings["pingOnOutput"] == "1" else user.display_name


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
