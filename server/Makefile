run: .venv
	"$<"/bin/python main.py

.venv:
	virtualenv -p /usr/bin/python3 "$@"
	"$@"/bin/pip install -r requirements.txt
