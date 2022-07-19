import os
import requests
from . import db
from . import create_app
from .models import ListJaksa
from .models_sidang import ScheduleJaksa
from flask import jsonify, redirect, request, abort, render_template, url_for

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
url = "https://api.telegram.org/bot5535111179:AAE4v7BiE2IAyqeM5M2ahigoV58qwU_f9kI/sendMessage"


@app.route("/")
def index():
    list_jaksa = ScheduleJaksa.query.all()
    return render_template(".html", list_jaksa=list_jaksa)


@app.route('/tambah_jaksa/', methods=['POST'])
def tambah_jaksa():
    if not request.form:
        abort(400)
    tambahJaksa = ListJaksa(
        nama_jaksa=request.form.get('nama_jaksa'),
        nip=request.form.get('nip'),
        jabatan_jaksa=request.form.get('jabatan_jaksa')
    )
    db.session.add(tambahJaksa)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/jaksa/daftarjaksa", methods=["GET"])
def get_listJaksa():
    list_jaksa = ListJaksa.query.all()
    return jsonify([list_jaksa.to_json() for list_jaksa in list_jaksa])


@app.route('/edit_jaksa/<int:id_jaksa>', methods=['POST'])
def edit_jaksa(id_jaksa):
    if not request.form:
        abort(400)
    edit_jaksa = ListJaksa.query.get(id_jaksa)
    if edit_jaksa is None:
        abort(404)
    edit_jaksa.nama_jaksa = request.form.get('nama_jaksa', edit_jaksa.nama_jaksa)
    edit_jaksa.nip = request.form.get('nip', edit_jaksa.nip)
    edit_jaksa.jabatan_jaksa = request.form.get('jabatan_jaksa', edit_jaksa.jabatan_jaksa)
    db.session.commit()
    return redirect(url_for("index"))


@app.route('/tambah_sidangjaksa/', methods=['POST'])
def tambah_sidang_jaksa():
    if not request.form:
        abort(400)
    tambahSidangJaksa = ScheduleJaksa(
        nama_kasus=request.form.get('nama_kasus'),
        nama_terdakwa=request.form.get('nama_terdakwa'),
        nama_jaksa=request.form.get('nama_jaksa'),
        waktu_sidang=request.form.get('waktu_sidang'),
        sidang_ke=request.form.get('sidang_ke')
    )
    db.session.add(tambahSidangJaksa)
    db.session.commit()
    reminder_message = "Yth. " + tambahSidangJaksa.nama_jaksa + \
                       "\nBerikut Jadwal Sidang Anda:\n" \
                       "Nama Kasus: " + tambahSidangJaksa.nama_kasus + \
                       "\nNama Terdakwa: " + tambahSidangJaksa.nama_terdakwa + \
                       "\nNama Jaksa Penuntut Umum: " + tambahSidangJaksa.nama_jaksa + \
                       "\nTahap Sidang Ke-: " + tambahSidangJaksa.sidang_ke + \
                       "\nTanggal dan Jam Sidang: " + tambahSidangJaksa.waktu_sidang

    # 302097349
    message_telegram = f'chat_id=-788839646&text={reminder_message}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=message_telegram)
    print(response.text)
    return redirect(url_for("index"))


@app.route('/edit_jadwal/<int:id_kasus>', methods=['POST'])
def edit_jadwal_sidang(id_kasus):
    if not request.form:
        abort(400)
    edit_jadwal_sidang = ScheduleJaksa.query.get(id_kasus)
    if edit_jadwal_sidang is None:
        abort(404)
    edit_jadwal_sidang.nama_kasus = request.form.get('nama_kasus', edit_jadwal_sidang.nama_kasus)
    edit_jadwal_sidang.nama_terdakwa = request.form.get('nama_terdakwa', edit_jadwal_sidang.nama_terdakwa)
    edit_jadwal_sidang.nama_jaksa = request.form.get('nama_jaksa', edit_jadwal_sidang.nama_jaksa)
    edit_jadwal_sidang.waktu_sidang = request.form.get('waktu_sidang', edit_jadwal_sidang.waktu_sidang)
    edit_jadwal_sidang.sidang_ke = request.form.get('sidang_ke', edit_jadwal_sidang.sidang_ke)
    db.session.commit()
    return redirect(url_for("index"))


@app.route("/jaksa/daftar_sidangjaksa", methods=["GET"])
def get_listSidangJaksa():
    list_sidangJaksa = ScheduleJaksa.query.all()
    return jsonify([list_sidangJaksa.to_json() for list_sidangJaksa in list_sidangJaksa])