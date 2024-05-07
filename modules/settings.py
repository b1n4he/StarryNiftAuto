# StarryNift 邀请地址
REF_LINK = "https://starrynift.art?referralCode=TDf8VqByWS"

# 关注永续需要设置用户的ID，一下USER_IDS_TO_FOLLOW为需要关注的用户ID列表，你也可以设置自己的ID列表
# 每个帐户每天将关注1个未关注的用户
# 您可以使用“获取帐户统计信息”选项获取用户ID，设置自己的小号来关注
USER_IDS_TO_FOLLOW = [
    "6bwN6gPKwE",
    "wLCvTVtzC7",
    "gTSV3gtflS",
    "sZbhJ3m-S5",
    "qZiaScTXcp",
    "BvDh6oWLvv",
    "9ZkHSyATB0",
    "TciUEa7WV9",
    "GMC8KbdEXP",
    "k6r-Eeh1Ha",
    "sA9e90ApWU",
    "dgs7fK5YXN",
    "89B1uZG_a2",
    "zmnnh1mxzl",
    "oLxFYpMvTz",
    "lC2f0PduqS",
    "QgHXExKJKK",
    "KnK6dxUQRn",
    "7mT6s4-iVS",
    "_EiFdqJV1l",
    "3KElmquZzz",
    "eU2P0WiyLu",
    "E4MdLCmlHs",
    "hwTe4ekmCo",
    "LmeEU_m8Sq",
    "_YpzxoraSq",
    "bjyp7uE5sY",
    "Ut2-SP9vkK",
    "-KJVzigOzP",
    "NhZDgdRyRN",
    "AnzFNDe6_T",
    "tBXXXWMLUs",
    "z8tPhANWbZ",
    "G64Y2HZBix",
    "ENRSYgxcbg",
    "06LU5nZx_n",
    "ZY39pnH0sO",
    "BCO7TAo3YJ",
    "Lk47x2VK_C",
    "EKs0VON7v_",
    "gZoM7GBaIT",
    "CeJWB9d878",
    "dBt_77bSbq",
    "Na80WID3Ou",
    "rYpJRluc_l",
    "tGg7b_OL4x",
    "C-CbELi8RU",
    "aO7SJbh3Fi",
    "d71c3nmbg0",
    "OwZtyv3SxZ",
]

DISABLE_SSL = False

SHUFFLE_ACCOUNTS = False
RETRIES = 2

THREADS = 5

MIN_SLEEP = 30
MAX_SLEEP = 50

BNB_RPC = "https://bsc.publicnode.com"
OPBNB_RPC = "https://opbnb-rpc.publicnode.com"


# 以下无用，无需修改
#___________________________________________
# |             BINANCE 划转            |

BINANCE_API_KEY = ""
BINANCE_SECRET_KEY = ""

MIN_WITHDRAW = 0.01001
MAX_WITHDRAW = 0.0105

USE_PROXY_FOR_BINANCE = (
    False  # 如果为True你需要在binance的api中设置代理白名单，否则无法使用
)
