import csv
import const
from random import uniform
from model import Model
from cult import Cult
from berserk import Berserk

time = []
for i in range(const.RANGE):
    time.append(i)

with open("model_data_demons.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(time)
with open("model_data_gr_demons.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(time)
with open("model_data_cults.csv", mode="w", encoding='utf-8') as w_file:
    file_writer = csv.writer(w_file, delimiter=",", lineterminator="\r")
    file_writer.writerow(time)


def run():
    model = Model()
    world = model.world

    for i in range(50):
        c = Cult([uniform(0, 1000), uniform(0, 1000)], int(uniform(1, 40)), world)
    berserk = Berserk([uniform(0, 1000), uniform(30, 670)], (200, uniform(0, 360)), world)

    running = True
    step = 0.02
    s = step
    while running:
        s += step

        if model.time_of_life == const.TIME_END:
            with open("model_data_demons.csv", mode="a", encoding='utf-8') as a_file:
                file_writer = csv.writer(a_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(world.data_demons)
            with open("model_data_gr_demons.csv", mode="a", encoding='utf-8') as a_file:
                file_writer = csv.writer(a_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(world.data_gr_demons)
            with open("model_data_cults.csv", mode="a", encoding='utf-8') as a_file:
                file_writer = csv.writer(a_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow(world.data_cults)
            # print(f"{world.data_demons}\n{world.data_gr_demons}"
            #       f"\n{world.data_cults}\n{world.count_berserk}"
            #       f"\n{world.data_berserk}")
            running = False

        world.act(step)


for i in range(const.RANGE):
    run()
    print(i+1)