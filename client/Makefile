CLIENT_PORT=8080
SERVER_PORT=8000

run: decompressed_apk
	cd "$<"/assets/public && python3 -m http.server $(CLIENT_PORT)

decompressed_apk: base.apk
	unzip -d "$@" "$<"
	sed -Ei'' 's,https://appprevia2\.faurgs-ti\.com\.br,http://localhost:$(SERVER_PORT),g' "$@"/assets/public/main.523afac5b0f8e5adf708.js
