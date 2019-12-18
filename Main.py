import util.File as File
import os.path as op
import random
from functools import reduce


class MajorProcess:

    def __init__(self, total):
        self.__total = total
        self.__data = self.__packager()

    def __packager(self):
        doc_data = File.File.read_file(op.join('data', 'doc.txt'))
        tags_data = File.File.read_file(op.join('data', 'tags.txt'))
        return [[int(tags_data[i][0]), int(tags_data[i][2]), doc_data[i][:-1]] for i in range(len(doc_data))]

    def __create_start(self, page):
        """ 生成文章的开头
        """
        art = ""
        if page > int(self.__total / 2):
            parta = ['时间过得真快', '光阴似箭', '时光匆匆']
            art += random.choice(parta)
            art += '，'

        partb = ['这是实习的第 ' + str(page + 1),
                 '现在是实习的第 ' + str(page + 1),
                 '这周是实习的第 ' + str(page + 1),
                 ]
        if page > int(self.__total / 2):
            partb.append('这周已经是实习的第 ' + str(page + 1))
            partb.append('眨眼就到了实习的第 ' + str(page + 1))

        art += random.choice(partb)
        art += ' '

        partc = ['周', '个星期']
        art += random.choice(partc)
        art += '。'

        return art

    def __create_main(self, page, emotion):
        """ 生成文章主体

        :param page:
        :param emotion:
        :return:
        """
        if page == 0:
            result = list(filter(lambda item: item[0] == emotion and (item[1] == 0 or item[1] == 4), self.__data))
        elif page == self.__total-1:
            result = list(filter(lambda item: item[0] == emotion and (item[1] == 1 or item[1] == 4), self.__data))
        elif page <= int(self.__total/2):
            result = list(filter(lambda item: item[0] == emotion and (item[1] == 2 or item[1] == 4), self.__data))
        else:
            result = list(filter(lambda item: item[0] == emotion and (item[1] == 3 or item[1] == 4), self.__data))

        res = random.choices(result, k=5)
        art = ''
        for item in res:
            art += item[2]
        return art

    def __create_end(self, page, emotion):
        """ 生成文章的末尾

        :param page:
        :param emotion:
        :return:
        """
        if emotion == 0:
            if page == 0:
                part = ['挑战才刚刚开始。', '感觉未来的生活充满着挑战。']
                return random.choice(part)
            elif page == self.__total-1:
                part = ['尽管有诸多不如意，实习终归结束了。', '最后感谢这次的宝贵的实习机会。']
                return random.choice(part)
            elif page <= int(self.__total / 2):
                part = ['接下来，我会好好调整心态，直面困难。',
                        '感觉是应该好好反省一下自己了。',
                        '未来还有很多查漏补缺的地方，任重而道远啊。'
                        ]
                return random.choice(part)
            else:
                part = ['实习已经过了一大半了，剩下的时间要好好努力。',
                        '虽然实习中有很多挑困难，但是我成长了很多。']
                return random.choice(part)
        else:
            if page == 0:
                part = ['']
                return random.choice(part)
            elif page == self.__total - 1:
                part = ['到今天，实习就结束了，最后感谢在实习中帮助了我的人。',
                        '最后感谢这次的宝贵的实习机会。'
                        ]
                return random.choice(part)
            elif page <= int(self.__total / 2):
                part = ['剩下的时间要再接再厉。', '剩下的实习时间还有一大半，我会好好珍惜的。']
                return random.choice(part)
            else:
                part = ['过去的一段时间中，总的来说收获了很多。',
                        '不得不说，这次实习让我成长了许多。']
                return random.choice(part)

    def process(self):
        """ 生成指定数量的周志

        :return:
        """
        for page in range(self.__total):
            self.single_process(page)

    def single_process(self, week):
        """ 生成指定周的周志, 文章为总分总结构, 大于 200 字, week 从 0 开始计数

        :param week:
        :return:
        """
        emotions = [0, 1]
        emotion = random.choice(emotions)
        article = ""
        article += self.__create_start(week)
        article += self.__create_main(week, emotion)
        has_end = random.choice([0, 1, 2, 3])
        if has_end == 1 or week == 0 or week == self.__total-1:
            article += self.__create_end(week, emotion)
        File.File.write_file(op.join('article', str(week) + '.txt'), article)


if __name__ == '__main__':
    # 获得 10 周的全部周志
    MajorProcess(10).process()
    # 获得 10 周中第 3 周的周志
    MajorProcess(10).single_process(2)

