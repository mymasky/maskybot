# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.


from . import LOG_CHANNEL, Button, asst, ayra_cmd, eor, get_string

REPOMSG = """
◈ **Starlight-Ubot​** ◈\n
◈ Repo - [Click Here](https://github.com/mymasky/maskybot)
◈ Support - @Groupmasky
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/mymasky/maskybot"),
    ],
    [Button.url("Support Group", "t.me/Groupmasky")],
]

AYSTRING = """🎇 **Thanks for Deploying Starlight-Ubot**

• Here, are the Some Basic stuff from, where you can Know, about its Usage."""


@ayra_cmd(pattern="Repo$")
async def useAyra(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        rs.chat_id,
        AYSTRING,
        file="https://telegra.ph/file/b73200fd892741e05ef39.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[Click Here]({msg.message_link})**")
