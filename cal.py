import requests
from enum import IntEnum

class Mods(IntEnum):
    NOMOD = 0
    NOFAIL = 1 << 0
    EASY = 1 << 1
    TOUCHSCREEN = 1 << 2
    HIDDEN = 1 << 3
    HARDROCK = 1 << 4
    SUDDENDEATH = 1 << 5
    DOUBLETIME = 1 << 6
    RELAX = 1 << 7
    HALFTIME = 1 << 8
    NIGHTCORE = 1 << 9
    FLASHLIGHT = 1 << 10
    AUTOPLAY = 1 << 11
    SPUNOUT = 1 << 12
    RELAX2 = 1 << 13
    PERFECT = 1 << 14
    KEY4 = 1 << 15
    KEY5 = 1 << 16
    KEY6 = 1 << 17
    KEY7 = 1 << 18
    KEY8 = 1 << 19
    KEYMOD = 1 << 20
    FADEIN = 1 << 21
    RANDOM = 1 << 22
    LASTMOD = 1 << 23
    KEY9 = 1 << 24
    KEY10 = 1 << 25
    KEY1 = 1 << 26
    KEY3 = 1 << 27
    KEY2 = 1 << 28
    SCOREV2 = 1 << 29

def readableMods(m: int) -> str:
    """
    Return a string with readable std mods.
    Used to convert a mods number for oppai

    :param m: mods bitwise number
    :return: readable mods string, eg HDDT
    """

    if not m: return ''

    r: List[str] = []
    if m & Mods.NOFAIL:      r.append('NF')
    if m & Mods.EASY:        r.append('EZ')
    if m & Mods.TOUCHSCREEN: r.append('TD')
    if m & Mods.HIDDEN:      r.append('HD')
    if m & Mods.HARDROCK:    r.append('HR')
    if m & Mods.DOUBLETIME:  r.append('DT')
    if m & Mods.RELAX:       r.append('RX')
    if m & Mods.HALFTIME:    r.append('HT')
    if m & Mods.NIGHTCORE:   r.append('NC')
    if m & Mods.FLASHLIGHT:  r.append('FL')
    if m & Mods.SPUNOUT:     r.append('SO')
    if m & Mods.SCOREV2:     r.append('V2')
    return ''.join(r)

token = "token"
base_api = "https://osu.ppy.sh/api"
#https://osu.ppy.sh/beatmapsets/855677#osu/1787848
link = input("beatmap link: ")
bmid = []
if '#' in link:
    e = link.split('#')   
    for char in e[1]:
        if char.isnumeric():
            bmid.append(char)

#bmid = int(input("beatmap id: "))

params = {
	'k': token,
	'b': int(''.join(bmid)),
	'm': 0,
	'mods': 66
}

print(f"getting passes on this map with {readableMods(66)}\n")

d = requests.get(f"{base_api}/get_scores?", params=params)

def acc(count_300, count_100, count_50, count_miss):
	total = sum((int(count_300), int(count_100), int(count_50), int(count_miss)))
	d = 100.0 * sum((
	int(count_50) * 50.0,
	int(count_100) * 100.0,
	int(count_300) * 300.0
	)) / (total * 300.0)
	return round(d, 2)


for l in d.json():

	print(
		f"Username: {l['username']}\n"
		f"Max combo: {l['maxcombo']}\n"
		f"Acc: { acc(l['count300'], l['count100'], l['count50'], l['countmiss']) }%\n"
		f"Misses: {l['countmiss']}\n"
		f"Rank: {l['rank']}\n"
		f"PP: {round(float(l['pp']))}\n"
		)
