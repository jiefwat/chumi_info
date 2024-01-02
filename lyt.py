import random


def auto_dialog():
    sentences_xiaoming = ['你是不是觉得自己极度的清醒？',
                          '自己总是可以在第一时间拨开迷雾看到本质。觉得洞悉了人类思想发展历程，感觉掌握了人类社会运行规律',
                          '而我们其他人都是一群身陷囹圄而不自知的愚民。你不但有异于常人的清醒，并且还有着知识分子特有的温柔与善良',
                          '试图拼尽全力拯救愚昧的大众。你说的每一句话，都是你看到愚昧的普罗大众后',
                          '哀其不幸怒其不争扼腕痛惜最后捶胸顿足所说的真理',
                          '都是你觉醒后独立思考的精髓',
                          '你就是这么觉得自己的对吧？！',
                          '我是一个高尚的人，一个纯粹的人，一个有道德的人，一个脱离了低级趣味的人，一个有益于人民的人。',
                          '自以为自己是冷静客观的剖析的',
                          '你是自以为自己是忠言对吗',
                          '你已经气的大脑跟不上了吧。想到什么词汇就赶紧丢群里，做着自己胜利占据主动权的春秋大梦呢',
                          '自己不觉得自己可笑吗',
                          '已经精神分裂了',
                          '干嘛艾特我们发你自己呀',
                          '还是自以为自己说的是事实',
                          '一个草包还好意思嘲笑别人是掉书袋啊',
                          '太监嘲笑别人阳痿',
                          '只能复制黏贴我说过的话了',
                          '说你肚子里没货一肚子只有草包',
                          '活在自己想象中的世界里',
                          '精神胜利法',
                          '你有沒有一次對我好好說話？每一次都侮辱謾罵詆毀地域，我感覺我現在對你講話都不正常',
                          '我不是你發洩的工具，我也不接受你一直這樣和我講話。你願意繼續說我退群。和你聊天沒有任何意義',
                          '你很阿Q'
                          ]

    sentences_xiaohong = ['看看，又开始顾左右而言他了',
                          '以为想到一个很好的反击点',
                          '故作坚强却有心无力的驳斥',
                          '你想到这个反击点，一定废了不少功夫吧',
                          '一定觉得自己很厉害吧👍',
                          '是不是觉得自己不尴尬的回击了对方',
                          '但我还是要说',
                          '草包就是草包',
                          '试图在自己的遮羞布被扯下',
                          '做一些无力的抵抗来防止尴尬',
                          '却不知自己的一言一行更能显示出自己的自卑与浅薄',
                          '抠脚了',
                          '尴尬吗？',
                          '求求你 别说了',
                          '极力挽尊',
                          '又来了 又开始臆想了',
                          '又觉得自己能行了',
                          '你这么菜 又这么跳',
                          '一定吃了不少苦吧',
                          '早干嘛去了 你好委屈啊',
                          '哭鼻子了吗',
                          '太弱了,我get不到你的反抗',
                          '就像 小孩子 ，攻击反弹',
                          '已经没办法从我们说的话里面做反驳了',
                          '我们都是理性讨论的，有的人破大防了',
                          '既然他说了，说明你自己很清楚你是什么货色',
                          '恰恰是你，无法有效组织语言，只能想到什么词汇就争先恐后的堆上来',
                          '生怕自己处于不利地位',
                          '你能把他放到这上面,说明你很清楚我的反驳语言是成体系的',
                          '你拼尽全力想做一些突破，但你自己也能发现。你做的尝试往往都建构在我搭建的逻辑体系上',
                          '你努力你突破,你又能说出什么花来呢？',
                          '之前就说过,你是个十足的草包',
                          '黔驴技穷'
                          ]
    used_sentences_xiaoming = []
    used_sentences_xiaohong = []
    round_num = 0
    while round_num < 5000:
        if round_num % 2 == 0:
            if len(used_sentences_xiaoming) == 0:
                print(f"小明：{random.choice(sentences_xiaoming)}")
            else:
                new_sentence = random.choice([s for s in sentences_xiaoming if s not in used_sentences_xiaoming])
                used_sentences_xiaoming.append(new_sentence)
        else:
            if len(used_sentences_xiaohong) == 0:
                print(f"小红：{random.choice(sentences_xiaohong)}")
            else:
                new_sentence = random.choice([s for s in sentences_xiaohong if s not in used_sentences_xiaohong])
                used_sentences_xiaohong.append(new_sentence)
        round_num += 1


if __name__ == "__main__":
    auto_dialog()
