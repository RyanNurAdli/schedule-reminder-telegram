from . import db


class ListJaksa(db.Model):
    __tablename__ = 'biodata_jaksa'
    id_jaksa = db.Column(db.Integer, primary_key=True)
    nama_jaksa = db.Column(db.String(110), nullable=False)
    nip_jaksa = db.Column(db.Integer, nullable=False)
    jabatan_jaksa = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            'id_jaksa': self.id_jaksa,
            'nama_jaksa': self.nama_jaksa,
            'nip_jaksa': self.nip_jaksa,
            'jabatan_jaksa': self.jabatan_jaksa
        }