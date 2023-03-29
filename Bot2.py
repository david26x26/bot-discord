import json  # para trabajar con datos en formato  Json
import os  # para interactuar con el sistema operativo
# para definir los comandos que nuestro bot puede manejar
from discord.ext import commands
# para interactuar con la API de Discord(enviar y recibir mensajes, conectarse a canales de voz, etc)
import discord
# from discord.ext.commands import has_any_role // esto era parte de una prueba que estaba haciendo para agregar restricciones de rol a nuestros comandos


# Clase que contiene el mensaje de bienvenida que se envía al usuario al unirse al servidor.
class Welcome_Embed():
    def __init__(self, member):
        # Member = nickname del nuevo usuario
        self.member = member
    # Propiedad que contiene el titulo y primer párrafo del mensaje de bienvenida.

    @property
    def welcome(self):
        self.embed = discord.Embed(
            title=f"¡Hola,{self.member}!", description=" ¡Bienvenido a la comunidad de Discord de Neurona Corp! Nos complace tenerte como parte de la primera comunidad de inteligencia artificial en español de Latinoamérica. Aquí, encontrarás una comunidad de apasionados por la inteligencia artificial y el aprendizaje automático, donde podrás compartir tus ideas, conocimientos, dudas y descubrimientos con personas de todo el continente.. ", color=int("00913f", 16))
        return self.embed
    # Propiedad que contiene el segundo párrafo del mensaje de bienvenida.

    @property
    def second_paragraph(self):
        self.embed = discord.Embed(
            description="Nuestro objetivo es crear un espacio donde podamos aprender y crecer juntos en este emocionante campo, y estamos emocionados de tenerte a bordo. ", color=int("00913f", 16))
        return self.embed
    # Propiedad que contiene el tercer párrafo del mensaje de bienvenida.

    @property
    def third_paragraph(self):
        self.embed = discord.Embed(
            description="¡No dudes en presentarte en el canal de bienvenida y unirte a las discusiones en curso!  ", color=int("00913f", 16))
        return self.embed
    # Propiedad que contiene el cuarto párrafo del mensaje de bienvenida.

    @property
    def fourth_paragraph(self):
        self.embed = discord.Embed(
            description="¡Te deseamos lo mejor en esta aventura y esperamos verte pronto en la comunidad! ", color=int("00913f", 16))
        return self.embed

    # Propiedad que contiene las redes sociales de y la imagen .
    @property
    def info(self):
        self.embed = discord.Embed(
            title="Redes Sociales",
            color=int("00913f", 16))
        self.embed.set_image(
            url="https://discord.io/content/server/829852733334487070_TbOLUN9NlmnK.png")

        self.embed.add_field(
            name="Linkedin",
            value="[Haga clic aquí](https://www.linkedin.com/company/neurona-corp/?originalSubdomain=cl)",
            inline=False)
        self.embed.add_field(
            name="Youtube",
            value="[Haga clic aquí](https://www.youtube.com/channel/UCK9UW6YzXK4G2QNA70Io0kw)",
            inline=False)
        self.embed.add_field(
            name="Instagram",
            value="[Haga clic aquí](https://www.instagram.com/neuronacorp/)",
            inline=False)
        self.embed.add_field(
            name="Twitter",
            value="[Haga clic aquí](https://twitter.com/neurona_corp)",
            inline=False)

        return self.embed


def main():
    # crea un archivo de configuración "config.json" con un prefijo y un token para el bot
    def create_config_archive():
        template = {
            'prefix': '!',  # es opcionl para en caso quere en un futuro usar comandos con el bot
            'token': "aca va tu token",  # token del bot
        }
        with open('config.json', 'w') as f:
            json.dump(template, f)

    # lee el archivo de configuración y devuelve un diccionario con los datos
    def read_config_archive():
        with open('config.json') as f:
            config_data = json.load(f)
        return config_data
    # una condicional que verifica si el archivo "config.json" existe
    if not os.path.exists('config.json'):
        print('Creando archivo de configuración')
        create_config_archive()

    # Parametros iniciales
    config_data = read_config_archive()
    prefix = config_data["prefix"]
    token = config_data["token"]
    intents = discord.Intents.all()
    bot = commands.Bot(
        command_prefix=prefix,
        intents=intents,
        description="Moderator bot")

    # Commands  // proximas cosas que se podrian agregar:
    # osea que cuando el usuario ejecute el comando acepto se le agrega el rol de "usuario" a un miembro del servidor que envía un mensaje directo al bot
    """
    @bot.command(name='acepto', help='Te agrega el rol "usuario"')
    async def add_user_role(ctx):
        # Condicional para que este comando solo se ejecute en MD
        if isinstance(ctx.channel, discord.channel.DMChannel):
            # Obtenemos nuestro servidor mediante la ID
            server = bot.get_guild(1034267302989922436)
            # Obtenemos el rol de usuario de nuestro servidor
            rol = server.get_role(1085989669998710836)
            # Obtenemos al usuario de nuestro servidor mediante su id (la cual viene en el contexto)
            member = server.get_member(ctx.message.author.id)
            # Le asignamos el rol
            await member.add_roles(rol)
            # Le enviamos un mensaje de bienvenida al servidor
            await ctx.author.send('Te has unido al servidor correctamente, disfruta.')
   """
    # Events

    @bot.event
    async def on_member_join(member):
        # ID del canal de bienvenida
        welcome_channel = bot.get_channel("aca es tu ID")
        # Usamos la plantilla para crear la respuesta
        welcome_embed = Welcome_Embed(member.name)

        # Enviamos el embed
        # se refiere a la propiedad "welcome" de la clase "welcome_embed" que muestra el primer parrafo
        await member.send(embed=welcome_embed.welcome)
        # segundo parrafo
        await member.send(embed=welcome_embed.second_paragraph)
        # tercer parrafo
        await member.send(embed=welcome_embed.third_paragraph)
        # cuarto parrafo
        await member.send(embed=welcome_embed.fourth_paragraph)
        await member.send(embed=welcome_embed.info)  # redes sociales
        # Damos la bienvenida
        await welcome_channel.send(f'Bienvenido al servidor, {str(member.mention)}. Revisa tus mensajes privados .')

    @bot.event
    async def on_ready():  # se ejecuta cuando el bot está listo para usarse y establece la actividad del bot en "A moderar el servidor
        activity = discord.Game(name="A moderar el servidor.")
        await bot.change_presence(activity=activity)
        # mensaje que de salida que muestra que todo esta bien
        print('The bot is working correctly.')

    # corre el bot con el token pasado en "parametros iniciales " linea 93
    bot.run(token)


# se esta llamando sola la funcion osea se está ejecutando directamente desde la línea de comandos
if __name__ == '__main__':
    main()
