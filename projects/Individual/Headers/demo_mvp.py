"""Demonstração offline da CLI com resposta HTTPS simulada por respx.

Execute: uv run python demo_mvp.py [--json | --verbose] [--weak]
A URL é fictícia e nenhuma requisição sai para a internet.
"""
import sys

import respx

from http_headers_scanner import main


def demo() -> int:
    """Executa a CLI real usando um servidor simulado para a gravação."""
    headers = {
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        "Content-Security-Policy": "default-src 'self'",
        "X-Content-Type-Options": "nosniff",
        "X-Frame-Options": "DENY",
        "Referrer-Policy": "no-referrer",
        "Permissions-Policy": "camera=(), microphone=()",
        "Cross-Origin-Opener-Policy": "same-origin",
        "X-Demo": "resposta simulada para demonstrar o MVP",
    }
    options = sys.argv[1:]
    if "--weak" in options:
        options.remove("--weak")
        headers.pop("Content-Security-Policy")
        headers["Cross-Origin-Opener-Policy"] = "unsafe-none"
    sys.argv = ["headers", "https://demo.test/", *options]
    with respx.mock:
        respx.get("https://demo.test/").respond(200, headers=headers)
        return main()


if __name__ == "__main__":
    sys.exit(demo())
