from database import db_instance as db

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    judul = db.Column(db.String(255), nullable=False)
    penulis = db.Column(db.String(255), nullable=False)
    penerbit = db.Column(db.String(255), nullable=False)
    tahun_terbit = db.Column(db.String(10), nullable=False)
    
    def __init__(self, judul, penulis, penerbit, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.penerbit = penerbit
        self.tahun_terbit = tahun_terbit
        