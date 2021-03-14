FROM python:2

RUN adduser internalalertuser

USER internalalertuser

WORKDIR /home/internalalertuser

COPY --chown=internalalertuser:internalalertuser internalalertsystem .

RUN pip install --user --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["-u", "MasterScript.py"]