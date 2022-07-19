from app import db
from app.routes import app
from app.models import ListJaksa
from app.models_sidang import ScheduleJaksa


@app.shell_context_processor
def make_shell_context_list_jaksa():
    return dict(db=db, ListJaksa=ListJaksa)


@app.shell_context_processor
def make_shell_context_sidang_jaksa():
    return dict(db=db, ScheduleJaksa=ScheduleJaksa)

# import os
# import requests
# import datetime
# from flask import jsonify, redirect, request, abort, render_template, url_for
#
#
# url = "https://api.telegram.org/bot5535111179:AAE4v7BiE2IAyqeM5M2ahigoV58qwU_f9kI/sendMessage"
#
# name = input("Masukkan Nama Anda: ")
# case_name = input("Masukkan Nama Kasus: ")
# nama_terdakwa = input("Masukkan Nama Terdakwa: ")
# nama_jaksa = input("Masukkan Nama Jaksa Penuntut Umum: ")
# # waktu_sidang = input(datetime.date("Masukkan Tanggal dan Jam Sidang: "))
# sidang_ke = input("Masukkan Sidang Ke- : ")
#
# reminder_message = "Yth. " + name + \
#                    "\nBerikut Jadwal Sidang Anda:\n" \
#                    "Nama Kasus: " + case_name + \
#                    "\nNama Terdakwa: " + nama_terdakwa + \
#                    "\nNama Jaksa Penuntut Umum: " + nama_jaksa +\
#                    "\nTahap Sidang Ke-: " + sidang_ke
#                    # "Tanggal dan Jam Sidang: \n"
#
#
# # 302097349
# message_telegram = f'chat_id=-788839646&text={reminder_message}'
# headers = {
#   'Content-Type': 'application/x-www-form-urlencoded'
# }
#
# response = requests.request("POST", url, headers=headers, data=message_telegram)
#
# print(response.text)