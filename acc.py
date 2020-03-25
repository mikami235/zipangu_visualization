import pandas as pd
import numpy as np
import logging
import matplotlib.pyplot as plt
import argparse

import folium

def mapping_rover(latitude,longtude):
    #atitude = 35.710063
    #longtude = 139.8107
    name = "東京スカイツリー"
 
    map = folium.Map(location=[latitude, longtude], zoom_start=18)
    folium.Marker(location=[latitude, longtude], popup=name).add_to(map)
    
    map.save("map_skytree.html")



def get_args():
    parser = argparse.ArgumentParser()
    # parser=parser.add_parser("main")
    parser.add_argument('--use_acc', action='store_true',
                        help="Whether to visualize ax,ay,az or not")
    parser.add_argument('--use_magnetic', action='store_true',
                        help="Whether to visualize mx,my,mz or not")
    parser.add_argument('--use_gyro', action='store_true',
                        help="Whether to visualize wx,wy,wz or not")
    parser.add_argument('--use_P', action='store_true',
                        help="Whether to visualize P or not")
    parser.add_argument('--load_dir', default='log_example',
                        help="Whether to visualize P or not")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    # グラフに単位をつける。
    # 一枚のpngに、複数枚のグラフを用意する。
    # 関数化して、web_UIでアクセスできるようにする。

    args = get_args()
    print(args)
    data_dir = str(args.load_dir)
    logging.info(data_dir)
    acc_file_dir = data_dir + "/acc_gyro.csv"
    df_acc = pd.read_csv(acc_file_dir)
    logging.info("df_acc")
    logging.info(df_acc.shape)
    
    column_list = ["timestamp", "ax", "ay", "az", "wx", "wy", "wz", "mx", "my", "mz", "lat", "lng", "yaw"]
    df_acc.columns=column_list
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    X = df_acc["timestamp"]
    y_1 = df_acc["ax"]
    y_2 = df_acc["ay"]
    y_3 = df_acc["az"]
    ax.plot(X,y_1, label="ax")
    ax.plot(X,y_2)
    ax.plot(X,y_3)
    ax.legend(loc='best')

    plt.savefig("ax_sample_"+str(data_dir)+".png")


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    X = df_acc["timestamp"]
    y_1 = df_acc["wx"]
    y_2 = df_acc["wy"]
    y_3 = df_acc["wz"]
    ax.plot(X,y_1, label="wx")
    ax.plot(X,y_2, label="wy")
    ax.plot(X,y_3, label="wz")
    ax.legend(loc='best')

    plt.savefig("w_sample_"+str(data_dir)+".png")


    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    X = df_acc["timestamp"]
    y_1 = df_acc["mx"]
    y_2 = df_acc["my"]
    y_3 = df_acc["mz"]
    ax.plot(X,y_1, label="mx")
    ax.plot(X,y_2, label="my")
    ax.plot(X,y_3, label="mz")
    ax.legend(loc='best')

    plt.savefig("m_sample_"+str(data_dir)+".png")

    landing_file_dir = data_dir + "/landing_detection.csv"

    df_landing = pd.read_csv(landing_file_dir)

    logging.info("df_landing")
    logging.info(df_landing.shape)
    
    column_list_2 = ["timestamp", "elevation", "temperature", "power", "P(highest)", "P(freefall)", "P(landed_bytime)", "P(landed_byimpact)"]
    df_landing.columns=column_list_2
    
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    X = df_landing["timestamp"]
    y_1 = df_landing["P(highest)"]
    y_2 = df_landing["P(freefall)"]
    y_3 = df_landing["P(landed_bytime)"]
    y_4 = df_landing["P(landed_byimpact)"]

    ax.plot(X,y_1, label="ax")
    ax.plot(X,y_2)
    ax.plot(X,y_3)
    ax.plot(X,y_4)
    ax.legend(loc='best')

    plt.savefig("p_sample_"+str(data_dir)+".png")

    y_1 = df_acc["lat"][0]
    y_2 = df_acc["lng"][1]
    mapping_rover(y_1,y_2)