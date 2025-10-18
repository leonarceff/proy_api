import os
import sys

# Agrega la raíz del proyecto al sys.path para importar módulos
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from config.database import get_db_session
from models.territorio_model import Municipio, Territorio

def verificar_datos():
    session = get_db_session()
    try:
        # Buscar el municipio Neiva
        neiva = session.query(Municipio).filter(Municipio.nombre == "Neiva").first()

        if not neiva:
            print("❌ No se encontró el municipio 'Neiva'.")
            return

        print(f"✅ Municipio encontrado: {neiva.nombre}")
        print(f"Descripción: {neiva.descripcion}\n")

        # Buscar los territorios asociados
        territorios = session.query(Territorio).filter(Territorio.municipio_id == neiva.id).all()

        if not territorios:
            print("⚠️ No se encontraron territorios para este municipio.")
        else:
            print("🌍 Territorios asociados:")
            for t in territorios:
                print(f"- {t.nombre}: {t.producto}")
    finally:
        session.close()

if __name__ == "__main__":
    verificar_datos()
