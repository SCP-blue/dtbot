import discord
import openpyxl

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("discord engine start")
    print("SCP 기록 서버 시동됨")
    print("SCP 기록 서버 자동저장")
    print("discord engine status")
    print("전체 시동완료")
    game = discord.Game("디스코드 통합봇 시동 점검중")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("저희 게임커뮤니티 재단에 오신것을 정말로 환영합니다. !명령어 하시면 각종 쓸수있는 명령어를 보여주게됩니다!")
    if message.content.startswith("!명령어"):
        await message.channel.send("!사진 | 적용된 사진은 현재 배경화면.jpg | 배경화면1.jpg 만 저장되있습니다. 만약에 사진을 원하신다면 | /사진 배경화면.jpg (/는 연속으로 쳐지는것을 방지하기위함입니다. /를 !라고 생각해주세요")
    if message.content.startswith("!사진목록"):
        await message.channel.send("현재 추가된 사진으로는 배경화면.jpg | 배경화면 1.jpg | 가 업로드가 되어있습니다. 앞으로 계속 추가될 예정입니다.")

    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))

    if message.content.startswith("!채널메시지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)

    if message.content.startswith("!DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await author.send(msg)

    if message.content.startswith("!뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="MUTE")
        await author.add_roles(role)

    if message.content.startswith("!언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="MUTE")
        await author.remove_roles(role)

    if message.content.startswith("!경고"):
        author = message.guild.get_member(int(message.content[4:22]))
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(author.id):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                file.save("경고.xlsx")
                if sheet["B" + str(i)].value == 3:
                    await message.guild.ban(author)
                    await message.channel.send("경고 3회 누적 추방절차 실행")
                else:
                    await message.channel.send("경고 1회 추가 완료")
                break
            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str (author.id)
                sheet["B" + str(i)].value = 1
                file.save("경고.xlsx")
                await message.channel.send("경고 1회 추가 완료")
                break
            i += 1

            if message.content.startswith(""):
                file = openpyxl.load_workbook("레벨.xlsx")
                sheet = file.active
                exp = [10, 20, 30, 40, 50]
                i = 1
                while True:
                    if sheet["A" + str(i)].value == str(message.author.id):
                        sheet["B" + str(i)].value = sheet["B" + str(i)].value + 1
                        if sheet ["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                            sheet ["C" + str(i)].value = sheet ["C" + (i)].value + 1
                            await messasge.channel.send("레벨상승! \n현재 레벨 : " + str(sheet["C" + str(i)].value) + "\n경험치 : " + str(sheet ["B" + str(i)].value))
                        file.save("레벨.xlsx")
                        break

                    if sheet["A" + str(i)].value == None:
                        sheet ["A" + str(i)].value = str(message.author.id)
                        sheet["B" + str(i)].value = 0
                        sheet["C" + str(i)].value = 1
                        break


                    i += 1
















client.run("NzQxODIwMjA4NDM1NTYwNDU5.Xy9H6A.LK9C8j4EJV5wqezw062NB0Bj2oA")