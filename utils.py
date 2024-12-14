import random
import nextcord

popular_words = open("dict-popular.txt").read().splitlines()
all_words = set(word.strip() for word in open ("dict-sowpods.txt"))

EMOJI_CODES = {
    "yellow": {
        "a": "<:yellow_a:1317430589720231938>",
        "b": "<:yellow_b:1317430591469387797>",
        "c": "<:yellow_c:1317430594073788516>",
        "d": "<:yellow_d:1317430595105722420>",
        "e": "<:yellow_e:1317430596653289582>",
        "f": "<:yellow_f:1317430598045794355>",
        "g": "<:yellow_g:1317430626735095878>",
        "h": "<:yellow_h:1317430628114894918>",
        "i": "<:yellow_i:1317430629322723378>",
        "j": "<:yellow_j:1317430630757302334>",
        "k": "<:yellow_k:1317430631881248778>",
        "l": "<:yellow_l:1317430703113240606>",
        "m": "<:yellow_m:1317430732989272075>",
        "n": "<:yellow_n:1317430734209941566>",
        "o": "<:yellow_o:1317430633089208410>",
        "p": "<:yellow_p:1317430735581478994>",
        "q": "<:yellow_q:1317430656925438019>",
        "r": "<:yellow_r:1317430658393444382>",
        "s": "<:yellow_s:1317430659697999983>",
        "t": "<:yellow_t:1317430660927062037>",
        "u": "<:yellow_u:1317430662109724693>",
        "v": "<:yellow_v:1317430696360284160>",
        "w": "<:yellow_w:1317430698264494131>",
        "x": "<:yellow_x:1317430699522789448>",
        "y": "<:yellow_y:1317430700684607579>",
        "z": "<:yellow_z:1317430701938970676>",
    },
    "green": {
        "a": "<:green_a:1317429153112395816>",
        "b": "<:green_b:1317429247236636712>",
        "c": "<:green_c:1317429248918814741>",
        "d": "<:green_d:1317429250374238208>",
        "e": "<:green_e:1317429154370551839>",
        "f": "<:green_f:1317429283232415785>",
        "g": "<:green_g:1317429155943419955>",
        "h": "<:green_h:1317429157180866611>",
        "i": "<:green_i:1317429284264218645>",
        "j": "<:green_j:1317429158674042920>",
        "k": "<:green_k:1317429285786751006>",
        "l": "<:green_l:1317429159865356339>",
        "m": "<:green_m:1317429161001750579>",
        "n": "<:green_n:1317429286860357652>",
        "o": "<:green_o:1317429162222551050>",
        "p": "<:green_p:1317429200885387316>",
        "q": "<:green_q:1317429165363826698>",
        "r": "<:green_r:1317429288315650048>",
        "s": "<:green_s:1317429315087892490>",
        "t": "<:green_t:1317429221349523516>",
        "u": "<:green_u:1317429316258238505>",
        "v": "<:green_v:1317429244774846496>",
        "w": "<:green_w:1317429317419925514>",
        "x": "<:green_y:1317429348877340782>",
        "y": "<:green_y:1317429348877340782>",
        "z": "<:green_z:1317429246045454356>",
    },
    "gray": {
        "a": "<:gray_a:1317431638799552583>",
        "b": "<:gray_b:1317431640120754216>",
        "c": "<:gray_c:1317431641320325121>",
        "d": "<:gray_d:1317431642939330580>",
        "e": "<:gray_e:1317431644080177165>",
        "f": "<:gray_f:1317431645548187719>",
        "g": "<:gray_g:1317431646802149397>",
        "h": "<:gray_h:1317431692469731389>",
        "i": "<:gray_i:1317431693765775360>",
        "j": "<:gray_j:1317431695246360616>",
        "k": "<:gray_k:1317431696433614872>",
        "l": "<:gray_l:1317431697809215489>",
        "m": "<:gray_m:1317431699205787668>",
        "n": "<:gray_n:1317431701164654612>",
        "o": "<:gray_o:1317431702582333440>",
        "p": "<:gray_p:1317431743703289907>",
        "q": "<:gray_q:1317431744848330863>",
        "r": "<:gray_r:1317431746777583686>",
        "s": "<:gray_s:1317431748203646976>",
        "t": "<:gray_t:1317431749415931904>",
        "u": "<:gray_u:1317431750770688051>",
        "v": "<:gray_v:1317431752234500126>",
        "w": "<:gray_w:1317431780290072606>",
        "x": "<:gray_x:1317431781393170462>",
        "y": "<:gray_y:1317431782676889600>",
        "z": "<:gray_z:1317431784543223818>",
    }
}

def generate_blanks():
    """Return a string of 5 blank emoji characters"""
    return "\N{WHITE MEDIUM SQUARE}" * 5

def generate_puzzel_embed(user: nextcord.User, puzzel_id: int) -> nextcord.Embed:
    embed = nextcord.Embed(title="Wordle Clone")
    embed.description = "\n".join([generate_blanks()] * 6)
    embed.set_author(name=user.name, icon_url=user.display_avatar.url)
    embed.set_footer(
        text=f"ID: {puzzel_id} | To play, use the command /play!\n"
        "To guess, replay to this message whith a word."
    )
    return embed

def is_vaild_word(word: str) -> bool:
    """"check if this is a vaild word"""
    return word.lower() in all_words

def random_puzzel_id() -> int:
    return random.randint(0, len(popular_words) - 1)

def generate_colored_word(guess: str, answer: str) -> str:
    """Return a string of emojis with the letters colored"""
    colored_word = [EMOJI_CODES["gray"][letter] for letter in guess]
    guess_letters = list(guess)
    answer_letters = list(answer)
    # change colors to green if smae  letter and same place
    for i in range(len(guess_letters)):
        if guess_letters[i] == answer_letters[i]:
            colored_word[i] = EMOJI_CODES["green"][guess_letters[i]]
            answer_letters[i] = None
            guess_letters[i] = None
    # change colors yellow if same letter and not the same place
    for i in range(len(guess_letters)):
        if guess_letters[i] is not None and guess_letters[i] in answer_letters:
            colored_word[i] = EMOJI_CODES["yellow"][guess_letters[i]]
            answer_letters[answer_letters.index(guess_letters[i])] = None
    return "".join(colored_word)

def update_embed(embed: nextcord.Embed, guess: str) -> nextcord.Embed:
    puzzel_id = int(embed.footer.text.split()[1])
    answer = popular_words[puzzel_id]
    colored_word = generate_colored_word(guess, answer)
    empty_slot = generate_blanks()
    # replace the first blank with the colored word
    embed.description = embed.description.replace(empty_slot, colored_word, 1)
    # check for game over
    num_empty_slots = embed.description.count(empty_slot)
    if guess == answer:
        if num_empty_slots == 0:
            embed.description += "\n\nPhew!"
        if num_empty_slots == 1:
            embed.description += "\n\nGreat!"
        if num_empty_slots == 2:
            embed.description += "\n\nSplendid!"
        if num_empty_slots == 3:
            embed.description += "\n\nImpressive!"
        if num_empty_slots == 4:
            embed.description += "\n\nMagnificent!"
        if num_empty_slots == 5:
            embed.description += "\n\nGenius!"
    elif num_empty_slots == 0:
        embed.description += f"\n\nThe answer was {answer}"
    return embed

def is_game_over(embed: nextcord.Embed) -> bool:
    return "\n\n" in embed.description
