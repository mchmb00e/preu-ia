from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Pregunta(Base):
    __tablename__ = 'preguntas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    evaluacion = Column(Integer, nullable=False)
    unidad = Column(String, nullable=False)
    numero = Column(String, nullable=False)
    enunciado = Column(String, nullable=False)
    figura = Column(Boolean, nullable=False) # evaluacion_numero.webp
    alternativas = Column(String, nullable=False)
    correcta = Column(String(1), nullable=False)

# Crear la base de datos SQLite y el motor
engine = create_engine('sqlite:///preguntas.db')

# Crear todas las tablas definidas en Base
Base.metadata.create_all(engine)

# Crear una sesión
Session = sessionmaker(bind=engine)
session = Session()


def add_pregunta(evaluacion: str, numero: int, enunciado: str, figura: bool, alternativas: str, correcta: str, unidad: str):
    new_pregunta = Pregunta(numero=numero,evaluacion=evaluacion , enunciado=enunciado, figura=figura, alternativas=alternativas, correcta=correcta, unidad=unidad)
    session.add(new_pregunta)
    session.commit()

def add_correcta(evaluacion: str, numero: int, correcta: str):
    global session
    pregunta = session.query(Pregunta).filter(Pregunta.evaluacion == evaluacion, Pregunta.numero == numero).first()
    pregunta.correcta = correcta
    session.commit()