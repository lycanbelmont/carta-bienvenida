"""
Servidor local para GM TechnoCorp – Carta de Bienvenida
========================================================
Ejecutar en la terminal con:
    python servidor.py

Luego abrir en el navegador:
    http://localhost:8080/v1.html   (Sin estilos)
    http://localhost:8080/v2.html   (Con estilos)

Cualquier cambio en empleados.xml o empresa.json
se reflejará al recargar la página.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIRECTORIO = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)

    def log_message(self, format, *args):
        # Mostrar peticiones en consola con formato limpio
        print(f"  [{self.address_string()}] {format % args}")

if __name__ == "__main__":
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 50)
        print("  GM TechnoCorp – Servidor Local")
        print("=" * 50)
        print(f"\n  Servidor corriendo en http://localhost:{PORT}")
        print(f"\n  V1 (Sin estilos): http://localhost:{PORT}/v1.html")
        print(f"  V2 (Con estilos): http://localhost:{PORT}/v2.html")
        print("\n  Presiona Ctrl+C para detener el servidor.")
        print("-" * 50)

        # Abrir automáticamente la versión con estilos
        webbrowser.open(f"http://localhost:{PORT}/v2.html")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n  Servidor detenido.")
