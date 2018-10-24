import discord
import os
import sys
import datetime
import random
import time as t
# このプログラムの存在するフォルダを指定しています。以下のフォルダ以外で動作する場合は指定しなおしてください。
os.chdir("/home/ec2-user/discord_bot")
home_dir = os.getcwd()
sys.path.append(home_dir)
import mymodule as mm

client = discord.Client()

# 以下はすべて  "1234567890"  のように指定してください。
# BOTが動くサーバーのIDを指定してください。
master_server = ""

# BOTが受け取ったDMを投稿するチャンネルのIDを指定してください。
dm_ch = ""

# 管理者がDMの返信文を書くチャンネルのIDを指定してください。DMを受信するチャンネルと同じでも構いません。
cmd_ch = ""

# 入退出のログを出力するチャンネルのIDを指定してください。
log_ch = ""

# BOTを介してDMを送信する場合に「ooからのメッセージです。」と表示されます。そのooの部分です。
default_author = "管理者"

# DMを受信したときに返信する内容
reply_content = "メッセージありがとうございます♪\n管理人さん達にお伝えしておきますね。"

# BOTのトークン(50文字越えの大文字小文字含む英数字)を指定してください。
Token = ""

# 各自で変更する必要があるのはここまで
#--------------------------------------------------------------
# 以下BOTで使用するメッセージ群
joined_content = """
時刻: {0}
参加メンバー名: {1}
メンション: <@{2}> (ID: {2})
現在のメンバー数: {3}
"""

left_content = """
時刻: {0}
退出メンバー名: {1}
メンション: <@{2}> (ID: {2})
現在のメンバー数: {3}
"""

dm_content = """
受信時間: {0}
送信者名: {1}
メンション: <@{2}> (ID: {2})
内容:
{3}
"""

dm_edit_content = """
【受信DMに編集が行われました】
元メッセージ受信時間: {0}
編集時間: {1}
送信者: {2}
メンション: <@{3}> (ID: {3})
内容:
{4}
"""

dm_delete_content = """
【受信DMが削除されました】
元メッセージ受信時間: {0}
削除時間: {1}
送信者: {2}
メンション: <@{3}> (ID: {3})
内容:
{4}
"""

check_dm = """
【送信確認】
送信先: <@{0}> (ID: {0})
添付ファイル: {1}件
内容:

{2}

送信してよろしければ⭕を、キャンセルするなら❌を選択してください。
"""
# BOT本文
class discord_bot():
    def save_msg(self, msg):
        file_dir = "./msg_log/" + msg.timestamp.strftime("%Y-%m") + "/" + msg.timestamp.strftime("%Y-%m-%d")
        if msg.channel.is_private:
            file_name = file_dir + "/DM.txt"
        else:
            file_name = file_dir + "/" + msg.channel.name + ".txt"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        else:
            pass
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("送信者: " + msg.author.name + "(ID: " + msg.author.id + ")\n")
            f.write("送信時間: " + msg.timestamp.strftime("%Y/%m/%d %H:%M:%S") + "(UTS)\n")
            f.write("メッセージID: " + msg.id + "\n")
            f.write("内容:\n" + msg.content + "\n")
            if msg.attachments != list():
                for fl in msg.attachments:
                    f.write("添付ファイルURL: " + fl["url"] + "\n")
                del fl
            else:
                pass
            f.write("----------------------------------------------------------\n")
        del file_dir
        del file_name
        del f

    def save_msg_edit(self, befor, after):
        file_dir = "./msg_edit_log/" + after.timestamp.strftime("%Y-%m") + "/" + after.timestamp.strftime("%Y-%m-%d")
        if after.channel.is_private:
            file_name = file_dir + "/DM.txt"
        else:
            file_name = file_dir + "/" + after.channel.name + ".txt"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        else:
            pass
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("送信者: " + after.author.name + "(ID: " + after.author.id + ")\n")
            f.write("元メッセージ送信時間: " + befor.timestamp.strftime("%Y-%m-%d") + "(UTS)\n")
            f.write("編集時間:　　　　　　 " + after.timestamp.strftime("%Y-%m-%d") + "(UTS)\n")
            f.write("メッセージID: " + befor.id + "\n")
            if after.attachments != list():
                for fl in after.attachments:
                    f.write("添付ファイルURL: " + fl["url"] + "\n")
                del fl
            else:
                pass
            f.write("元メッセージ:\n")
            f.write(befor.content)
            f.write("\n------------------------------------\n")
            f.write("新メッセージ:\n")
            f.write(after.content)
            f.write("\n----------------------------------------------------------\n")
        del file_name
        del file_dir
    
    def save_msg_del(self, msg):
        file_dir = "./msg_del_log/" + datetime.datetime.now().strftime("%Y-%m") + "/" + datetime.datetime.now().strftime("%Y-%m-%d")
        if msg.channel.is_private:
            file_name = file_dir + "/DM.txt"
        else:
            file_name = file_dir + "/" + msg.channel.name + ".txt"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        else:
            pass
        with open(file_name, "a", encoding="utf-8") as f:
            f.write("削除時間: " + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
            f.write("送信者: " + msg.author.name + "(ID: " + msg.author.id + ")\n")
            f.write("送信時間: " + msg.timestamp.strftime("%Y/%m/%d %H:%M:%S") + "(UTS)\n")
            f.write("メッセージID: " + msg.id + "\n")
            f.write("内容:\n" + msg.content + "\n")
            if msg.attachments != list():
                for fl in msg.attachments:
                    f.write("添付ファイルURL: " + fl["url"] + "\n")
                del fl
            else:
                pass
            f.write("----------------------------------------------------------\n")
        del file_dir
        del file_name
        del f

@client.event
async def on_ready():
    print("Complete!")

@client.event
async def on_member_join(member):
    if member.server.id == master_server:
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        count_member = member.server.member_count
        send_content = joined_content.format(now_time, member.name, member.id, count_member)
        await client.send_message(client.get_channel(log_ch), send_content)
        del now_time
        del count_member
        del send_content

@client.event
async def on_member_remove(member):
    if member.server.id == master_server:
        now_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        count_member = member.server.member_count
        send_content = left_content.format(now_time, member.name, member.id, count_member)
        await client.send_message(client.get_channel(log_ch), send_content)
        del now_time
        del count_member
        del send_content

@client.event
async def on_message(message):
    discord_bot().save_msg(message)
    if message.author != client.user:
        if message.channel.id == cmd_ch:
            if message.content.startswith("?help"):
                with open("help.txt", "r", encoding="utf-8") as f:
                    await client.send_message(message.channel, f.read())
                del f
            elif message.content.startswith("?send-dm"):
                content_dict = mm.split_function(content=message.content, start_line=2)
                if "userid" in content_dict:
                    try:
                        user = await client.get_user_info(content_dict["userid"])
                        if not content_dict.get("author") is None:
                            if str(content_dict.get("author").strip()) == "true":
                                if message.author.nick is None:
                                    author = message.author.name + "さんからのメッセージです。\n"
                                else:
                                    author = message.author.nick + "さんからのメッセージです。\n"
                            else:
                                author = default_author + "からのメッセージです。\n"
                        else:
                            author = default_author + "からのメッセージです。\n"
                        content = author + content_dict["rest_last"]
                        if message.attachments != list():
                            file_list = mm.file_action(message=message)
                        else:
                            file_list = list()
                        msg = await client.send_message(message.channel, check_dm.format(user.id, str(len(file_list)), content))
                        await client.add_reaction(msg, "⭕")
                        await client.add_reaction(msg, "❌")
                        time = 300
                        start_time = datetime.datetime.now()                      
                        while True:
                            target_reaction = await client.wait_for_reaction(message=msg, timeout=time)
                            if target_reaction == None: #timeout
                                await client.send_message(message.channel, "5分間選択がなかったため、送信せず終了します。")
                                deal = "cancel"
                                break
                            else:
                                if target_reaction.user != client.user:
                                    if target_reaction.reaction.emoji == "⭕":
                                        deal = "start"
                                        break
                                    elif target_reaction.reaction.emoji == "❌":
                                        await client.send_message(message.channel, "送信をキャンセルしました。")
                                        deal = "cancel"
                                        break
                                    else:
                                        await client.remove_reaction(msg, target_reaction.reaction.emoji, target_reaction.user)
                                        elapsed_time = datetime.datetime.now() - start_time #経過時間を計測
                                        time = time - int(elapsed_time.seconds)
                                        del elapsed_time
                                        if time > 0:
                                            pass
                                        else:
                                            await client.send_message(message.channel, "5分間選択がなかったため、送信せず終了します。")
                                            deal = "cancel"
                                            break
                                else:
                                    pass
                        if deal == "start":
                            try:
                                await client.send_message(user, content)
                                for fl in file_list:
                                    if fl["type"] == "file":
                                        await client.send_file(user, fl["file_name"])
                                        os.remove(fl["file_name"]) #delete_file
                                    elif fl["type"] == "url":
                                        await client.send_message(user, fl["url"])
                                    else:
                                        pass
                                await client.send_message(message.channel, "送信完了しました。")
                                try:
                                    del fl
                                except:
                                    pass
                            except:
                                await client.send_message(message.channel, "送信失敗\n対象者が同じサーバーのメンバーからのDMを受け付けていない可能性があります。")
                        del user
                        del author
                        del content
                        del file_list
                        del msg
                        del time
                        del start_time
                        del target_reaction
                        del deal
                    except discord.errors.NotFound:
                        await client.send_message(message.channel, "【エラー】\n存在しないユーザーIDです。IDを確認してください。")
                    except Exception as e:
                        print("エラー: \n", e)
                else:
                    await client.send_message(message.channel, "【エラー】\nuseridを指定してください。")
                del content_dict
            else:
                pass
        elif message.channel.is_private:
            ch = client.get_channel(dm_ch)
            await client.send_message(message.channel, reply_content)
            send_content = dm_content.format(message.timestamp.strftime("%Y/%m/%d %H:%M:%S"), message.author.name, message.author.id, message.content)
            if message.attachments != list():
                file_list = mm.file_action(message=message)
            else:
                file_list = list()
            await client.send_message(ch, send_content)
            for fl in file_list:
                if fl["type"] == "file":
                    await client.send_file(ch, fl["file_name"])
                    os.remove(fl["file_name"]) #delete_file
                elif fl["type"] == "url":
                    await client.send_message(ch, fl["url"])
                else:
                    pass
            del file_list
            try:
                del fl
            except:
                pass
            del send_content
            del ch
        else:
            pass
    else:
        pass

@client.event
async def on_message_edit(befor, after):
    discord_bot().save_msg_edit(befor=befor, after=after)
    if after.channel.is_private:
        ch = client.get_channel(dm_ch)
        send_content = dm_edit_content.format(befor.timestamp.strftime("%Y/%m/%d %H:%M:%S"), datetime.datetime().now().strftime("%Y/%m/%d %H:%M:%S"), after.author.name, after.author.id, after.content)
        await client.send_message(ch, send_content)
        del ch
        del send_content
    else:
        pass

@client.event
async def on_message_delete(message):
    discord_bot().save_msg_del(msg=message)
    if message.channel.is_private:
        ch = client.get_channel(dm_ch)
        send_content = dm_delete_content.format(message.timestamp.strftime("%Y/%m/%d %H:%M:%S"), datetime.datetime().now().strftime("%Y/%m/%d %H:%M:%S"), message.author.name, message.author.id, message.content)
        await client.send_message(ch, send_content)
        del ch
        del send_content
    else:
        pass

client.run(Token)
