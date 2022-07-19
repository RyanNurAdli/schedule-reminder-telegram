from . import db
import datetime


class ScheduleJaksa(db.Model):
    __tablename__ = 'sidang_jaksa'
    id_kasus = db.Column(db.Integer, primary_key=True)
    nama_kasus = db.Column(db.String(300), nullable=False)
    nama_terdakwa = db.Column(db.String(150), nullable=False)
    id_jaksa = db.Column(db.Integer, foreign_key=True)
    nama_jaksa = db.Column(db.String(110), nullable=False)
    waktu_sidang = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    # waktu_sidang = db.Column(db.Datetime, nullable=False)
    sidang_ke = db.Column(db.Integer, nullable=False)

    def to_json(self):
        return {
            'id_kasus': self.id_kasus,
            'nama_kasus': self.nama_kasus,
            'nama_terdakwa': self.nama_terdakwa,
            'id_jaksa': self.id_jaksa,
            'nama_jaksa': self.nama_jaksa,
            'waktu_sidang': self.waktu_sidang,
            'sidang_ke': self.sidang_ke
        }