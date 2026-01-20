from db import db

class LivroModel(db.Model):
    __tablename__ = "livros"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    ano = db.Column(db.Integer, nullable=False)

    autor_id = db.Column(
        db.Integer,
        db.ForeignKey("autores.id", ondelete="CASCADE"),
        nullable=False
    )

    autor = db.relationship("AutorModel", back_populates="livros")
