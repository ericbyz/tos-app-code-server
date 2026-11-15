#!/usr/bin/env python3
"""Generate code-server.lang for the TOS App Center (26 locales, English fill)."""
NAME_EN = "code-server"
AUTHOR = "ericbyz"
DESC_EN = (
    "Run VS Code on the TNAS and open it from any browser on the LAN "
    "(upstream coder/code-server, self-contained with its own Node runtime). "
    "Preconfigured on port 18225 with password authentication; the generated "
    "password is shown at install time and kept in /etc/code-server/config.yaml."
)
NOTE_EN = "1. Repackaged upstream coder/code-server for the TOS App Center."
NOTE_ZH = "1. 将上游 coder/code-server 封装为 TOS 应用中心应用。"

PRIMARY = [
    ("zh-cn", "code-server 网页版 VS Code",
     "在 NAS 上运行 VS Code,局域网内任意浏览器即可打开(上游 coder/code-server,"
     "自包含运行时,无需系统 Node)。预配置 18225 端口与密码认证,安装时自动生成密码"
     "并保存于 /etc/code-server/config.yaml。适合远程改配置、写脚本、轻量开发。"),
    ("zh-hk", "code-server 網頁版 VS Code",
     "在 NAS 上運行 VS Code,局域網內任意瀏覽器即可打開(上游 coder/code-server,"
     "自包含運行時,無需系統 Node)。預配置 18225 端口與密碼認證,安裝時自動生成密碼"
     "並保存於 /etc/code-server/config.yaml。適合遠程改配置、寫腳本、輕量開發。"),
]

ORDER = ["zh-cn", "zh-hk", "en-us", "ko-kr", "ja-jp", "de-de", "fr-fr", "it-it",
         "es-es", "hu-hu", "pl-pl", "tr-tr", "ru-ru", "pt-pt", "cs-cz", "da-dk",
         "nl-nl", "nb-no", "sv-se", "el-gr", "ro-ro", "th-th", "vi-vn", "id-id",
         "ar-sa", "he-il"]

NATIVE = {
    "ja-jp": "NAS 上で VS Code を動かし、LAN 内の任意のブラウザから開ける code-server(上流 coder/code-server、Node ランタイム同梱の自己完結パッケージ)。ポート 18225・パスワード認証を事前設定し、生成したパスワードは /etc/code-server/config.yaml に保存されます。",
    "ko-kr": "NAS에서 VS Code를 실행하고 LAN의 모든 브라우저에서 여는 code-server입니다(업스트림 coder/code-server, 자체 Node 런타임 포함). 포트 18225과 비밀번호 인증이 사전 구성되며, 생성된 비밀번호는 /etc/code-server/config.yaml에 저장됩니다.",
    "de-de": "VS Code auf der NAS ausführen und aus jedem Browser im LAN öffnen (upstream coder/code-server, eigenständig mit mitgelieferter Node-Laufzeit). Vorkonfiguriert auf Port 18225 mit Passwort-Authentifizierung; das generierte Passwort steht in /etc/code-server/config.yaml.",
    "fr-fr": "Exécutez VS Code sur le NAS et ouvrez-le depuis n'importe quel navigateur du LAN (upstream coder/code-server, autonome avec son runtime Node). Préconfiguré sur le port 18225 avec authentification par mot de passe ; le mot de passe généré est dans /etc/code-server/config.yaml.",
    "es-es": "Ejecute VS Code en la NAS y ábralo desde cualquier navegador de la LAN (upstream coder/code-server, autocontenido con su propio runtime Node). Preconfigurado en el puerto 18225 con autenticación por contraseña; la contraseña generada queda en /etc/code-server/config.yaml.",
    "ru-ru": "Запускайте VS Code на NAS и открывайте из любого браузера в LAN (upstream coder/code-server, самодостаточный со своим Node). Преднастроен на порт 18225 с паролем; сгенерированный пароль хранится в /etc/code-server/config.yaml.",
}

def main(out_path):
    lines = []
    for loc in ORDER:
        name, desc = NAME_EN, NATIVE.get(loc, DESC_EN)
        for l, n, d in PRIMARY:
            if l == loc:
                name, desc = n, d
                break
        note = NOTE_ZH if loc in ("zh-cn", "zh-hk") else NOTE_EN
        lines += [f"[{loc}]", f'name = "{name}"', f'auth = "{AUTHOR}"',
                  f'descript = "{desc}"', f'note = "{note}"', ""]
    open(out_path, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
    print("wrote", out_path, len(ORDER), "locales")

if __name__ == "__main__":
    main("code-server.lang")
