#! python3
# Copyright (C) 2017 Logo-Kuo <logo@forblind.org.tw>
# Copyright (C) 2017 Hong Jen-Yee (PCMan) <pcman.tw@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


brl_ascii_dic = { # 包函英數模式下的字母、數字及鍵盤上的符號
    # 小寫字母
    "1": "a",
    "12": "b",
    "14": "c",
    "145": "d",
    "15": "e",
    "124": "f",
    "1245": "g",
    "125": "h",
    "24": "i",
    "245": "j",
    "13": "k",
    "123": "l",
    "134": "m",
    "1345": "n",
    "135": "o",
    "1234": "p",
    "12345": "q",
    "1235": "r",
    "234": "s",
    "2345": "t",
    "136": "u",
    "1236": "v",
    "2456": "w",
    "1346": "x",
    "13456": "y",
    "1356": "z",
    # 大寫字母
    "17": "A",
    "127": "B",
    "147": "C",
    "1457": "D",
    "157": "E",
    "1247": "F",
    "12457": "G",
    "1257": "H",
    "247": "I",
    "2457": "J",
    "137": "K",
    "1237": "L",
    "1347": "M",
    "13457": "N",
    "1357": "O",
    "12347": "P",
    "123457": "Q",
    "12357": "R",
    "2347": "S",
    "23457": "T",
    "1367": "U",
    "12367": "V",
    "24567": "W",
    "13467": "X",
    "134567": "Y",
    "13567": "Z",
    # 數字
    "2": "1",
    "23": "2",
    "25": "3",
    "256": "4",
    "26": "5",
    "235": "6",
    "2356": "7",
    "236": "8",
    "35": "9",
    "356": "0",
    # 英數鍵盤上的符號
    "4": "`",
    "45": "~",
    "2346": "!",
    "47": "@",
    "3456": "#",
    "1246": "$",
    "146": "%",
    "457": "^",
    "12346": "&",
    "16": "*",
    "12356": "(",
    "23456": ")",
    "36": "-",
    "123456": "=",
    "456": "_",
    "346": "+",
    "2467": "[",
    "124567": "]",
    "246": "{",
    "12456": "}",
    "56": ";",
    "3": "'",
    "156": ":",
    "5": "\"",
    "6": ",",
    "46": ".",
    "34": "/",
    "126": "<",
    "345": ">",
    "1456": "?",
    "12567": "\\",
    "1256": "|"
}

# 注音符號分類查表
_bopomofo_categories = {
	"聲母": set("ㄍㄎㄐㄑㄉㄊㄋㄅㄆㄇㄈㄗㄘㄙㄓㄔㄕㄏㄒㄌㄖ"),
	"介音": set("ㄧㄨㄩ"),
	"韻母": set("ㄚㄛㄜㄝㄟㄞㄠㄡㄢㄤㄣㄥㄦ"),
	"舌尖音": set("ㄓㄔㄕㄖㄗㄘㄙ")
}


# 檢查注音符號是否屬於某分類
def bopomofo_is_category(bopomofo, category):
	if category.endswith("疊韻"): # 檢查是否為疊韻 (不完全精確，沒有檢查是否為正確注音)
		return len(bopomofo) == 2 and bopomofo_is_category(bopomofo[0], "介音") and bopomofo_is_category(bopomofo[1], "韻母")
	return (bopomofo in _bopomofo_categories[category])


brl_phonic_dic = { # 共計 59 個 不函標點
    # 聲母
    '135':'ㄅ', # 與 ）、？同 區分方式用 space ？= 1345 + space, ）= 135 + space 就導讀軟體的六點輸入是這樣做 所以大部分人是可以習慣這樣操作的
    '1234':'ㄆ',
    '134':'ㄇ',
    '12345':'ㄈ',
    '145':'ㄉ',
    '124':'ㄊ',
    '1345':'ㄋ', # 加 space 變成 ？
    '14':'ㄌ',
    # '13':'ㄍ', # 接韻母 或 ㄨ 開頭的疊韻
    '123':'ㄎ', # 跟 ！相同 區別方式就是 ！= 123 + space 
    '1235':'ㄏ',
    # '13':'ㄐ', # 接疊韻 ㄧ 或 ㄩ 開頭
    # '245':'ㄑ', # 接疊韻 ㄧ 或 ㄩ 開頭
    # '15':'ㄒ', # 接疊韻 ㄧ 或 ㄩ 開頭
    # '1':'ㄓ', # 跟輕聲同 ˙ 區分方式是 前面沒注聲就是˙ 或者前面有完成的字是ㄓ 不然就直接列舉會打輕聲的韻母 或者後面接聲母就是˙ 
    '12':'ㄔ',
    '24':'ㄕ',
    '1245':'ㄖ',
    '125':'ㄗ',
    # '245':'ㄘ', # 接韻母 或 ㄨ 開頭的疊韻
    # '15':'ㄙ', # 接韻母 或 ㄨ 開頭的疊韻
    # 韻母 疊韻
    '16':'ㄧ',
    '34':'ㄨ',
    '1256':'ㄩ',
    # 韻母
    '345':'ㄚ',
    '126':'ㄛ',
    '2346':'ㄜ',
    # '26':'ㄝ', # 用不到 跟 ㄧㄞ 同 區別方式就是用不到 所以直接 = ㄧㄞ
    '2456':'ㄞ',
    # '356':'ㄟ', # 跟 ㄧㄛ 同 區別方式是 ㄧㄛ前面不會有聲母 或者列舉與ㄟ組合的聲母
    '146':'ㄠ',
    '12356':'ㄡ',
    '1236':'ㄢ',
    '136':'ㄣ',
    '1346':'ㄤ',
    '1356':'ㄥ',
    # '156':'ㄦ', # 也當作捲舌與不捲舌聲母單獨出現時所加的韻母 例 ㄓˊ = 1-156-2 顯示可不要有 ㄦ 但輸入時 要判斷直接接注聲就把 1-156 看成是 ㄓ
    # 疊韻 ㄧ 系列
    '23456':'ㄧㄚ',
    # '356':'ㄧㄛ', # 很少用 與 ㄟ 同 如 唷
    '346':'ㄧㄝ', 
    # '26':'ㄧㄞ', # 很少用 如 崖 與 ㄝ 同
    '246':'ㄧㄠ', # 與 （同 區分方式為 （= 246 + space 
    '234':'ㄧㄡ',
    '2345':'ㄧㄢ',
    '1456':'ㄧㄣ',
    '46':'ㄧㄤ',
    '13456':'ㄧㄥ',
    # 疊韻 ㄨ 系列
    '35':'ㄨㄚ',
    '25':'ㄨㄛ',
    '2356':'ㄨㄞ',
    '1246':'ㄨㄟ',
    '12456':'ㄨㄢ',
    '123456':'ㄨㄣ',
    '456':'ㄨㄤ',
    '12346':'ㄨㄥ',
    # 疊韻 ㄩ 系列
    '236':'ㄩㄝ',
    '45':'ㄩㄢ',
    '256':'ㄩㄣ',
    '235':'ㄩㄥ',
    '3':' ', # space key
    '2':'ˊ',
    '4':'ˇ',
    '5':'ˋ',
    # '1':'˙',

    # 一對多特例
    '356': 'CHECK_PREVIOUS', # ['ㄧㄛ', 'ㄟ']
    '26': 'ㄧㄞ', # ['ㄝ', 'ㄧㄞ']
    '15': 'CHECK_NEXT',  # ['ㄒ', 'ㄙ']
    '1': 'CHECK_PREVIOUS', # ['ㄓ', '˙']
    '13': 'CHECK_NEXT', # ['ㄍ', 'ㄐ']
    '245': 'CHECK_NEXT', # ['ㄑ', 'ㄘ'],
    # 其他特例
    '156': 'CHECK_PREVIOUS', #'ㄦ'
	
	# 標點符號
	'23': '<',  # ，: shift + ,
	'36': '>',  # 。: shift + .
}

# 注音後再按下 space key 可轉變為標點
brl_space_dic = {
	"ㄅ": ")", # "）",
	"ㄋ": "?", # "？",
	"ㄎ": "!", # "！",
	"ㄧㄠ": "(" # "（",
}
