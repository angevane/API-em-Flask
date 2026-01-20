from db import db

class AutorModel(db.Model):
    __tablename__ = "autores"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)

    livros = db.relationship(
        "LivroModel",
        back_populates="autor",
        cascade="all, delete-orphan"
    )
