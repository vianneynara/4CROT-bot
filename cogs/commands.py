import asyncio
import disnake
import os
import random
import time
from datetime import datetime
from disnake.ext import commands

berhenti = False


class Commands(commands.Cog):
    def __init__(self, client):
        self.bot = client
        # self.task = client.loop.create_task(self.pingme())

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def help(self, ctx):
        embed = disnake.Embed(
            title='Help Commands',
            color=random.choice([0xfc0303, 0x03d3fc, 0x03fc07, 0xd7fc03]),
            description="""
**Commands:**
Help <- kamu sedang memakai commandnya sekarang
Poll [kalimat]: Membuat polling[alias: quickvote, vote, voting, polling]
whoami: melihat beberapa informasi tentangmu[pemakaian: >whoami @mention atau >whoami]
saran [kalimat]: bot akan mengirimkan saranmu ke sebuah private channel
kapan [kalimat]: Menanyakan kapan [kalimat] akan terjadi(Tidak Serius)
apakah [kalimat]: Menanyakan apakah [kalimat] benar atau tidak(tidak serius)
siapa [kalimat]: Memberi nama+tags secara acak
loli: Try me
remember [jumlah detik] [kalimat]: mengingatkan anda
sex [nama]: Croot moncroot!
sange sama kartun: mengirim video dedi kobuzer

**Moderator only:**
clear [jumlah]: menghapus [jumlah] pesan!
            
**Bot owner commands:**
cconsole
install
load
unload
reload
spam""")
        await ctx.reply(embed=embed, mention_author=False)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def remember(self, ctx, sec, *, kata):
        await ctx.reply(f"Aight bro igotchu to remember {kata}")
        await asyncio.sleep(int(sec))
        if random.randrange(1, 5) == 2:
            await ctx.reply(f'Broo i forgor to say {kata} to {ctx.author.name}!', mention_author=False)
            await asyncio.sleep(3)
            await ctx.reply(f"Jk bro, Hey <@{ctx.author.id}> remember to {kata}")
        else:
            await ctx.reply(f"Bro, remember to {kata}")

    @commands.command()
    @commands.is_owner()
    async def install(self, ctx, kode):
        await ctx.send("b-\nb-baik senpai, aku akan mendownloadnya >//<")
        # os.system(f"nhentai -D --id={kode} --output=D:\pekob\Dojin --threads=15")
        await ctx.send("s-\ns-sudah selesai senpai >//<")

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cal(self, ctx, hitung):
        await ctx.reply(eval(hitung))

    @commands.command(aliases=['quickvote', 'vote', 'voting', 'polling'])
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def poll(self, ctx, *, votet):
        #:white_check_mark::negative_squared_cross_mark:
        meseg = await ctx.send(f"VOTE!:white_check_mark::negative_squared_cross_mark:\n**{votet}**")
        await meseg.add_reaction("✅")
        await meseg.add_reaction("❎")
        # if user react a:
        # if user react to b
        # if user react b:
        # if user react to a
        # add reaction blablabla check react 5 detik
        # await asyncio.sleep(5)
        # await meseg.reply(f"Vote ended!!")

        # yes or no

    @commands.command()
    @commands.is_owner()
    async def cconsole(self, ctx):
        os.system("clear")
        await ctx.reply("Cleared Console")

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def whoami(self, ctx, user: disnake.User = None):
        if user is None:
            await ctx.reply(f"""
Your Name is: {ctx.author.name}
Your Display name is: {ctx.author.display_name}
Your UserID: {ctx.author.id}
Your account age: {ctx.author.created_at.strftime("Day: %d | Month: %m | Year: %Y | Hour: %H | Minute: %M")}
        """)
        else:
            await ctx.reply(f"""
his/her name is: {user.name}
his/her Display name is: {user.display_name}
his/her UserID is: {user.id}
his/her account age: {user.created_at.strftime("Day: %d | Month: %m | Year: %Y | Hour: %H | Minute: %M")}
        """)

    @commands.command(name='embed')
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def embedc(self, ctx, link):
        # role = discord.utils.find(lambda r: r.name == 'Builder', ctx.message.guild.roles)
        # role = discord.utils.get(ctx.message.guild.roles, id=896617220673785887), discord.utils.get(ctx.message.guild.roles, id=896617220673785887)
        # print(ctx.author.roles) # "896617220673785887" or "883722818888536094"
        if 896617220673785887 or 883722818888536094 in ctx.author.roles: # untuk cek apakah builder/staff
            ctx.command.reset_cooldown(ctx)
            pass
        if "tenor" in link:
            await ctx.reply("Maaf, tenor link gak didukung.", mention_author=False)
            return
        else:
            embed = disnake.Embed(color=disnake.Color.green(), timestamp=datetime.now())
            embed.set_image(url=link)
            embed.set_footer(text=f"by {ctx.author}", icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
            await ctx.message.delete()
            return

    @commands.command()
    @commands.is_owner()
    async def spam(self, ctx, user: disnake.User, juml):
        global berhenti
        for i in range(int(juml)):
            if berhenti == False:
                await user.send(f"<@{user.id}>")
            else:
                berhenti = True

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.is_owner()
    async def pingme(self, ctx, jumle):
        global berhenti
        #   berhenti = False
        if int(jumle) > 50:
            await ctx.reply("Kalo ngeping jangan banyak banyak")
        else:
            for i in range(int(jumle)):
                if berhenti == False:
                    await ctx.author.send(f"<@{ctx.author.id}>")

    #     else:
    #       berhenti = True

    # @commands.command()
    # @commands.is_owner()
    # async def pingstop(self, ctx):
    #  global berhenti
    #  berhenti = True

    @commands.command(name='saran')
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def saran(self, ctx, *, args):
        await ctx.reply("Saranmu sudah terkirim")
        channel = self.bot.get_channel(887908566382571580)
        await channel.send(f"[{datetime.now()}]{ctx.author.mention} saran: {args}")

    @commands.command(aliases=['gore', 'scat', 'shota', 'zoophilia'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def loli(self, ctx):
        await ctx.reply('https://cdn.discordapp.com/attachments/799121511470202921/888036846909673512/caption.gif')

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clear(self, ctx, amount=1):
        if ctx.author.guild_permissions.administrator or ctx.author.guild_permissions.manage_messages:
            await ctx.channel.purge(limit=amount + 1)

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kapan(self, ctx):
        kpn = [
            'taun depan',
            '2 hari lagi',
            '1 hari lagi',
            '3 hari lagi',
            'tahun depan',
            'satu abad lagi',
            'tidak akan terjadi',
            'bulan depan',
            'minggu depan',
            '3 minggu lagi',
            'kapan kapan'
        ]
        await ctx.reply(random.choice(kpn))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def siapa(self, ctx, *, spa):
        randomMember = random.choice(ctx.guild.members)
        await ctx.reply(f"si {randomMember.name}#{randomMember.discriminator} yang {spa}")

    @commands.command(name="apakah")
    @commands.cooldown(1, 20, commands.BucketType.user)
    async def apakah(self, ctx, *, arg):
        apkh = [
            'iya',
            'YNTKTS',
            'ga',
            'lu ngomong apasih gblk',
            'bisa di bilang ya',
            'kemungkinan iya',
            'kemungkinan tidak',
            'nggak lah',
            'tidak',
            'pasti',
            'gamungkin',
            'iya kayaknya',
            'ngga kayaknya',
            'kata siapa?',
            'ril',
            'btul',
            'fek',
            'apa iyh?'
        ]
        await ctx.reply(random.choice(apkh))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sex(self, ctx, user: disnake.User):
        await ctx.reply(
            f"Kamu sek dengan {user.name}. Moncroot\n{random.choice(['https://tenor.com/view/degrom-dance-idk-zumba-imen-gif-21292699', 'https://cdn.discordapp.com/attachments/880509666482860042/890878449567272970/20210924_090418.jpg'])}")

    @apakah.error
    async def apakah_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Sabar lagi cooldown")

    @cal.error
    async def cal_error(self, ctx, error):
        await ctx.reply("""
      Hitungan mungkin salah
      * = kali
      / = bagi
      + = tambah
      - = kurang
      contoh cara pemakaian: ``>cal 10*21(22+11)``
      """)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        # await message.add_reaction("<:rengginang:883274423359127593>")

        # listlink = 'jpg', 'jpeg', 'png', 'pneg', 'mp4', 'mp3', 'webp', 'amv', 'gif', 'wmv', 'wav'
        if 'http' in message.content.lower():
            if message.channel.guild.id == 880497534957658132:  # jika message ada di server 4crot
                channel = self.bot.get_channel(887908566382571580)  # log bot 4crot di 4crot
            elif message.channel.guild.id == 520809362525257748:  # jika message ada di server kub
                channel = self.bot.get_channel(940812191198773288)  # log bot 4crot di kub

            embedz = disnake.Embed(
                title='Media/link Sent!',
                color=random.choice([0xfc0303, 0x03d3fc, 0x03fc07, 0xd7fc03]),
                description=(f""" 
ID = {message.author.id}
User = {message.author.name}#{message.author.discriminator} alias <@{message.author.id}>
Display Name = {message.author.display_name}
Channel = <#{message.channel.id}>
==============================================="""))
            await channel.send(embed=embedz)
            await channel.send(f"sent: {message.content}")

        for a in message.attachments:
            channel = self.bot.get_channel(887908566382571580)
            embed = disnake.Embed(
                title='Media/link Sent!',
                color=random.choice([0xfc0303, 0x03d3fc, 0x03fc07, 0xd7fc03]),
                description=(f""" 
ID = {message.author.id}
User = {message.author.name}#{message.author.discriminator} alias <@{message.author.id}>
Display Name = {message.author.display_name}
channel = <#{message.channel.id}>
==============================================="""))
            await channel.send(embed=embed)
            await channel.send(f"sent: {a}")


def setup(client):
    client.add_cog(Commands(client))
    print("Loaded commands.")
